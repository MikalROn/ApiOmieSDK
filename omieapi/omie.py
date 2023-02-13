from requests import post
from json import JSONDecodeError


class Omie:

    def __init__(self, omie_app_key: str, omie_app_secret: str):
        """
        :param omie_app_key:              Chave api da omie
        :param omie_app_secret:           APi Secret da omie
        """
        self._endpoint = 'https://app.omie.com.br/api/v1/'
        self._appkey = omie_app_key
        self._appsecret = omie_app_secret
        self._head = {'Content-type': 'application/json'}

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


class Produtos(Omie):
    def listar_produtos(
            self, registros: int = 100, filtrar_pdv: bool = True, pagina: int = 1,
            apenas_importado_api: bool = False
    ) -> dict:

        apenas_importado_api = self._bool_para_sn(apenas_importado_api)
        filtrar_pdv = self._bool_para_sn(filtrar_pdv)

        return self._chamar_api(
            call='ListarProdutos',
            endpoint='geral/produtos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros,
                "apenas_importado_api": apenas_importado_api,
                "filtrar_apenas_omiepdv": filtrar_pdv
            }
        )


class CupomFiscal(Omie):
    def listar_cupomfiscal(self, metodo: str, nPagina: int, nRegPorPagina: int) -> dict:
        """
        :param metodo:           CuponsFiscais or CuponsItens or CuponsPagamentos    Meio de listagem

            :CuponsFiscais: -> Listagem dos itens dos cupons fiscais
            :CuponsItens:   -> Listagem dos pagamentos dos cupons fiscais
            :CuponsPagamentos: -> Listagem dos pagamentos dos cupons fiscais

        :param nPagina:         integer                                             numero da pagina
        :param nRegPorPagina:   integer                                             registros por página
        """
        self._gerencia_metodo(['CuponsFiscais', 'CuponsItens', 'CuponsPagamentos'], metodo)
        return self._chamar_api(
            call=metodo,
            endpoint='produtos/cupomfiscalconsultar/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina
            }
        )
    def incluir_NFCE(self, **kargs):
        ...

    def importar_NFCE(
            self,
            emiNome: str = None, emiVersao: str = None, emiId: str = None,
            chNFe: str = None, nfceXml: str = None, nfceMd5: str = None,
            cAcaoCliente: str = None, idCliente: int = None, idVendedor: int = None,
            idProjeto: int = None, idLocalEstoque: int = None, cNaoMovEstoque: str = None,
            cNaoGerarTitulo: str = None, cIncluirProduto: str = None
    ) -> dict:
        """
        :keyword emiNome:	        string20	Nome do aplicativo emissor do cupom fiscal.
        :keyword emiVersao:	        string20	Versão do aplicativo emissor do cupom fiscal.
        :keyword emiId:	            string20	Identificação do computador onde o aplicativo emissor do cupom fiscal está instalado. É o código do PDV.+
        :keyword chNFe:	            string44	Chave de Acesso da Nota Fiscal Consumidor Eletrônico.
        :keyword nfceXml:	        text	    XML da NFC-e enviada.
        :keyword nfceMd5:	        string32	MD5 do arquivo XML enviado em "nfceXml".
        :keyword cAcaoCliente: 	    string15 Ação a ser executada com relação a tag idCliente.
        :keyword idCliente:	        integer	Código do cliente.
        :keyword idVendedor:	    integer	Código do vendedor.
        :keyword idProjeto:	        integer	Código do projeto.
        :keyword idLocalEstoque:	integer	Código do Local do Estoque.
        :keyword cNaoMovEstoque:	string1	Indica que os items do Cupom Fiscal não devem movimentar o estoque.
        :keyword cNaoGerarTitulo:	string1	Indica que a parcela não deve gerar um título no financeiro.
        :keyword cIncluirProduto:	string1	Indica se na inclusão do cupom os produtos não existentes devem ser incluídos automaticamente.

        :return: dicionario com resultado da requisição ou erro
        """
        return self._chamar_api(
            call='ImportarNFCe',
            endpoint='produtos/nfce/',
            param={"emiNome": emiNome,
                   "emiVersao": emiVersao,
                   "emiId": emiId,
                   "chNFe": chNFe,
                   "nfceXml": nfceXml,
                   "nfceMd5": nfceMd5,
                   "cAcaoCliente": cAcaoCliente,
                   "idCliente": idCliente,
                   "idVendedor": idVendedor,
                   "idProjeto": idProjeto,
                   "idLocalEstoque": idLocalEstoque,
                   "cNaoMovEstoque": cNaoMovEstoque,
                   "cNaoGerarTitulo": cNaoGerarTitulo,
                   "cIncluirProduto": cIncluirProduto
                   }
        )
