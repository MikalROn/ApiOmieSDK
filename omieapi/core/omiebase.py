from requests import post, Session
from json import JSONDecodeError


class OmieBase:

    def __init__(self, omie_app_key: str, omie_app_secret: str, session: bool=False):
        """
        :param omie_app_key:              Chave api da omie
        :param omie_app_secret:           APi Secret da omie
        """
        self._endpoint = 'https://app.omie.com.br/api/v1/'
        self._appkey = omie_app_key
        self._appsecret = omie_app_secret
        self._head = {'Content-type': 'application/json'}
        self._has_session = False
        
        if session:
            self._session = Session()

    def conectar_api(self, metodo: str, endpoint: str, parametros: dict) -> dict:
        """
         ##> Metdodo geral para chamar a api
         > Para usar este metodo tenha como referencia a documentação oficial do omie
         > link: https://developer.omie.com.br/

        :param metodo:       Função a ser realizada disponivel na api omie EX:  'AssociarCodIntServico'
        :param endpoint:     Endpiot url da api EX:      'servicos/servico/'
        :param parametros:   Parametros usados na requisição, EX:  { "nCodServ": 0, "cCodIntServ": "" }
        :return: Retorna dicionario com resultados da requisição ou erro, erros com Tipos Complexos são gerenciados pela
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

    def _post_request(self, url: str, json: dict) -> dict:
            try:
                if self._has_session:
                    r = self._session.post(url, headers=self._head, json=json)
                else:
                    r = post(url, headers=self._head, json=json)
                    
                if r.status_code == 200:
                    try:
                        return r.json()
                    except JSONDecodeError as erro:
                        return {
                            'Error': 'JSON Decode Error',
                            'Message': f'{erro}'
                        }
                else:
                    return {
                        'Error': r.status_code,
                        'headers':  r.headers,
                        'Mensagem': r.json()
                    }
            except Exception as erro:
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

        :return:                 Resultado da Requisição ou erro
        """
        url = f'{self._endpoint}{endpoint}'
        json = self._gerar_json(call, param)
        return self._post_request(url, json)