from ..core.omiebase import OmieBase


class CupomFiscal(OmieBase):
    """ Classe que carrega todos os metodos relacionados a cupons fiscais """
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
        :keyword cAcaoCliente: 	    string15    Ação a ser executada com relação a tag idCliente.
        :keyword idCliente:	        integer	    Código do cliente.
        :keyword idVendedor:	    integer	    Código do vendedor.
        :keyword idProjeto:	        integer	    Código do projeto.
        :keyword idLocalEstoque:	integer	    Código do Local do Estoque.
        :keyword cNaoMovEstoque:	string1	    Indica que os items do Cupom Fiscal não devem movimentar o estoque.
        :keyword cNaoGerarTitulo:	string1	    Indica que a parcela não deve gerar um título no financeiro.
        :keyword cIncluirProduto:	string1	    Indica se na inclusão do cupom os produtos não existentes devem ser incluídos automaticamente.

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
