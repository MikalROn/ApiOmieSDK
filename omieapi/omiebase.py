from requests import post
from json import JSONDecodeError
from omieapi.scripts import pega_links_api


class OmieBase:

    def __init__(self, omie_app_key: str, omie_app_secret: str):
        """
        :param omie_app_key:              Chave api da omie
        :param omie_app_secret:           APi Secret da omie
        """
        self._endpoint = 'https://app.omie.com.br/api/v1/'
        self._appkey = omie_app_key
        self._appsecret = omie_app_secret
        self._head = {'Content-type': 'application/json'}

    @property
    def endpoint_api(self):
        """ Metodo que busca online todos os endpoints da api """
        return [link.replace('https://app.omie.com.br/api/v1/') for link in pega_links_api()]

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
            "param": [*param]
        }

    def _gerencia_metodo(self, lista_de_metodos: list, metodo):
        if metodo not in lista_de_metodos:
            raise ValueError(f'{metodo} Não existe!')

    @staticmethod
    def _bool_para_sn(boolean: bool):
        return 'S' if boolean else 'N'

    def _post_request(self, url: str, json: dict) -> dict:
        try:
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
                    'Mensagem': r.text
                }
        except Exception as erro:
            return {
                    'Error': 'Erro ao fazer requisição ',
                    'Mensagem': f'{erro}'
                }

    def _listar_padrao(
            self, call: str, endpoint: str, pagina: int, registros_por_pagina: int, apenas_importado_api: bool
    ) -> dict:
        apenas_importado_api = self._bool_para_sn(apenas_importado_api)
        return self._chamar_api(
            call=call,
            endpoint=endpoint,
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api
            }
        )

    def _chamar_api(self, endpoint: str = '', call: str = '', param: dict | tuple | list = None) -> dict:
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