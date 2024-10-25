import httpx, time

from requests import post, Session
from json import JSONDecodeError


class OmieBase:

    def __init__(self, omie_app_key: str, omie_app_secret: str, session: bool=False, use_httpx: bool=False, log: bool=False):
        """
        Inicializa a classe Omie com as credenciais e opções de configuração.

        :param omie_app_key: str          A chave de acesso da API Omie, usada para autenticação.
        :param omie_app_secret: str       O segredo da API Omie, usado para autenticação.
        :param session: bool, opcional    Indica se uma sessão persistente deve ser usada para as requisições (padrão: False).
        :param use_httpx: bool, opcional  Define se a biblioteca `httpx` deve ser usada em vez de `requests` para as requisições (padrão: False).
        :param log: bool, opcional        Gera log em um arquivo .txt
        """
        self._endpoint = 'https://app.omie.com.br/api/v1/'
        self._appkey = omie_app_key
        self._appsecret = omie_app_secret
        self._head = {'Content-type': 'application/json'}
        self._has_session = session
        self._httpx = use_httpx
        self._log = log
        

        if session:
            if self._httpx:
                self._session = httpx.Client()
            else:
                self._session = Session()
                
    def __enter__(self):
        if self._has_session:
            return self
        else:
            self.abrir_session()
            return self
    
    
    def __exit__(self, exc_type, exc_value, trace):
        self.fechar_session()
    
    
    def fechar_session(self):
        """
        Fecha a sessão aberta na inicialização
        """
        if self._has_session:
            self._has_session = False
            self._session.close()
        
        else:
            raise RuntimeError("Não exite sessão aberta")
    
    
    def abrir_session(self):
        """ Cria nova  session """
        if not self._has_session:
            self._has_session = True
            
            if self._httpx:
                self._session = httpx.Client()
            else:
                self._session = Session()
        else:
            raise RuntimeError("Session já está aberta")
        

    def conectar_api(self, metodo: str, endpoint: str, parametros: dict) -> dict:
        """
         ##> Metdodo geral para chamar a api
         > Para usar este metodo tenha como referencia a documentação oficial do omie
         > link: https://developer.omie.com.br/

        :param metodo:       Função a ser realizada disponivel na api omie EX:  'AssociarCodIntServico'
        :param endpoint:     Endpiot url da api EX:      'servicos/servico/'
        :param parametros:   Parametros usados na requisição, EX:  { "nCodServ": 0, "cCodIntServ": "" }
        :return:  Retorna dicionario com resultados da requisição ou erro, erros com Tipos Complexos são gerenciados pela
         api.
        """
        return self._chamar_api(
            call=metodo,
            endpoint=endpoint,
            param=parametros
        )

    def _gerar_json(self, call: str, param: dict | tuple | list) -> dict:
        return {
            "call": call,
            "app_key": self._appkey,
            "app_secret": self._appsecret,
            "param": [param]
        }

    def _gerencia_metodo(self, lista_de_metodos: list, metodo: str) -> None:
        if metodo not in lista_de_metodos:
            raise ValueError(f'{metodo} Não existe!')

    def _gerar_log(self, r) -> None:
        if r.status_code == 200:
            with open('log.txt', 'a') as file:
                file.write(f"'status_code': {r.status_code}, 'headers':  {r.headers}, 'Mensagem': 'Sucesso'\n")
        else:
            with open('log.txt', 'a') as file:
                file.write(f"'status_code': {r.status_code}, 'headers':  {r.headers}, 'Mensagem': {r.json()}\n")
        

    def _post_request(self, url: str, json: dict) -> dict:
            try:
                
                if self._has_session:
                    r = self._session.post(url, headers=self._head, json=json, timeout=(300.0, 300.0))
                elif self._httpx:
                    r = httpx.post(url, headers=self._head, json=json, timeout=(300.0, 300.0))
                else:
                    r = post(url, headers=self._head, json=json, timeout=(300.0, 300.0))
                
                if self._log:
                    self._gerar_log(r)
                
                if r.status_code == 200:
                    try:
                        return r.json()
                    except JSONDecodeError as erro:
                        return {
                            'Error': 'JSON Decode Error',
                            'Message': f'{erro}'
                        }
                
                elif r.status_code == 429:
                    time.sleep(60)
                    return self._post_request(url, json)
                
                elif r.status_code == 425:
                    startSlice = str(r.content).find('Tente novamente em')+19
                    endSlice = str(r.content)[startSlice:].find(' ') + startSlice
                    wait = str(r.content)[startSlice:endSlice]
                    time.sleep(int(wait))
                    return self._post_request(url, json)
                
                elif r.status_code == 500:
                    if "Broken response from Application Server" in str(r.content):
                        return self._post_request(url, json)
                    elif "OmieAPI-Error': '6" in str(r.content):
                        startSlice = str(r.content).find('Aguarde')+8
                        endSlice = str(r.content)[startSlice:].find(' ') + startSlice
                        wait = str(r.content)[startSlice:endSlice]
                        time.sleep(int(wait))
                        return self._post_request(url, json)
                    elif "OmieAPI-Error': '8020" in str(r.content):
                        time.sleep(60)
                        return self._post_request(url, json)
                    else:
                        return {
                            'Error': r.status_code,
                            'headers':  r.headers,
                            'Mensagem': r.json()
                        }    
                else:
                    return {
                        'Error': r.status_code,
                        'headers':  r.headers,
                        'Mensagem': r.json()
                    }
            except Exception as erro:
                if "Connection aborted" in erro:
                    return self._post_request(url, json)
                else:
                    return {
                            'Error': 'Erro ao fazer requisição ',
                            'Mensagem': f'{erro}'
                        }

    def _chamar_api(self, endpoint: str = None, call: str = None, param: dict | tuple | list = None) -> dict:
        """
        :keyword endpoint:         Final da url EX: geral/contacorrente/
        :keyword call:             Chamada para api  EX: ListarContasCorrentes
        :keyword param:            Parametros para a chamada
                                   Ex:{"pagina": 1, "registros_por_pagina": 100, "apenas_importado_api": "N"}

        :return:                  Resultado da Requisição ou erro
        """
        url = f'{self._endpoint}{endpoint}'
        json = self._gerar_json(call, param)
        return self._post_request(url, json)