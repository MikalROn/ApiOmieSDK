from ..core.omiebase import OmieBase


class ReqCompra(OmieBase):
    """ Classe que carrega metodos """

    def alterar_req(
            self, codCateg, codIntReqCompra, codProj, codReqCompra, dtSugestao, obsIntReqCompra, obsReqCompra,
            ItensReqCompra
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarReq',
            endpoint='produtos/requisicaocompra/',
            param={
                "codCateg": codCateg,
                "codIntReqCompra": codIntReqCompra,
                "codProj": codProj,
                "codReqCompra": codReqCompra,
                "dtSugestao": dtSugestao,
                "obsIntReqCompra": obsIntReqCompra,
                "obsReqCompra": obsReqCompra,
                "ItensReqCompra": ItensReqCompra
            }
        )

    def consultar_req(
            self, codIntReqCompra, codReqCompra
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarReq',
            endpoint='produtos/requisicaocompra/',
            param={
                "codIntReqCompra": codIntReqCompra,
                "codReqCompra": codReqCompra
            }
        )

    def excluir_req(
            self, codIntReqCompra, codReqCompra
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirReq',
            endpoint='produtos/requisicaocompra/',
            param={
                "codIntReqCompra": codIntReqCompra,
                "codReqCompra": codReqCompra
            }
        )

    def incluir_req(
            self, codCateg, codIntReqCompra, codProj, codReqCompra, dtSugestao, obsIntReqCompra, obsReqCompra,
            ItensReqCompra
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirReq',
            endpoint='produtos/requisicaocompra/',
            param={
                "codCateg": codCateg,
                "codIntReqCompra": codIntReqCompra,
                "codProj": codProj,
                "codReqCompra": codReqCompra,
                "dtSugestao": dtSugestao,
                "obsIntReqCompra": obsIntReqCompra,
                "obsReqCompra": obsReqCompra,
                "ItensReqCompra": ItensReqCompra
            }
        )

    def pesquisar_req(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='PesquisarReq',
            endpoint='produtos/requisicaocompra/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def upsert_req(
            self, codCateg, codIntReqCompra, codProj, codReqCompra, dtSugestao, obsIntReqCompra, obsReqCompra,
            ItensReqCompra
    ) -> dict:
        """"""
        return self._chamar_api(
            call='UpsertReq',
            endpoint='produtos/requisicaocompra/',
            param={
                "codCateg": codCateg,
                "codIntReqCompra": codIntReqCompra,
                "codProj": codProj,
                "codReqCompra": codReqCompra,
                "dtSugestao": dtSugestao,
                "obsIntReqCompra": obsIntReqCompra,
                "obsReqCompra": obsReqCompra,
                "ItensReqCompra": ItensReqCompra
            }
        )