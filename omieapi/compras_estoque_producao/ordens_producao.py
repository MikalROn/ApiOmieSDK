from ..core.omiebase import OmieBase


class OrdensProducao(OmieBase):
    """ Classe que carrega metodos de ordens de produção """
    def alterar_ordem_producao(
            self, identificacao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarOrdemProducao',
            endpoint='produtos/op/',
            param={
                "identificacao": identificacao
            }
        )

    def concluir_ordem_producao(
            self, cCodIntOP, nCodOP, dDtConclusao, nQtdeProduzida, cObsConclusao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConcluirOrdemProducao',
            endpoint='produtos/op/',
            param={
                "cCodIntOP": cCodIntOP,
                "nCodOP": nCodOP,
                "dDtConclusao": dDtConclusao,
                "nQtdeProduzida": nQtdeProduzida,
                "cObsConclusao": cObsConclusao
            }
        )

    def consultar_ordem_producao(
            self, cCodIntOP, nCodOP
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarOrdemProducao',
            endpoint='produtos/op/',
            param={
                "cCodIntOP": cCodIntOP,
                "nCodOP": nCodOP
            }
        )

    def excluir_ordem_producao(
            self, cCodIntOP, nCodOP
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirOrdemProducao',
            endpoint='produtos/op/',
            param={
                "cCodIntOP": cCodIntOP,
                "nCodOP": nCodOP
            }
        )

    def incluir_ordem_producao(
            self, identificacao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirOrdemProducao',
            endpoint='produtos/op/',
            param={
                "identificacao": identificacao
            }
        )

    def listar_ordem_producao(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarOrdemProducao',
            endpoint='produtos/op/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def reverter_ordem_producao(
            self, cCodIntOP, nCodOP
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ReverterOrdemProducao',
            endpoint='produtos/op/',
            param={
                "cCodIntOP": cCodIntOP,
                "nCodOP": nCodOP
            }
        )

    def upsert_ordem_producao(
            self, identificacao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='UpsertOrdemProducao',
            endpoint='produtos/op/',
            param={
                "identificacao": identificacao
            }
        )