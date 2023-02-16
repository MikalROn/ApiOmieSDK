from omieapi.omiebase import OmieBase


class Oportunidades(OmieBase):
    """ Classe que carrega todos os metodos relacionados a oportunidades """

    def alterar_oportunidade(
            self, identificacao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "identificacao": identificacao
            }
        )

    def consultar_oportunidade(
            self, nCodOp, cCodIntOp
    ) -> dict:
        """Consulta de oportunidade."""
        return self._chamar_api(
            call='ConsultarOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "nCodOp": nCodOp,
                "cCodIntOp": cCodIntOp
            }
        )

    def excluir_oportunidade(
            self, nCodOp, cCodIntOp
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "nCodOp": nCodOp,
                "cCodIntOp": cCodIntOp
            }
        )

    def incluir_oportunidade(
            self, identificacao
    ) -> dict:
        """Incluir uma oportunidade."""
        return self._chamar_api(
            call='IncluirOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "identificacao": identificacao
            }
        )

    def listar_oportunidades(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista de oportunidades."""
        return self._chamar_api(
            call='ListarOportunidades',
            endpoint='crm/oportunidades/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def upsert_oportunidade(
            self, identificacao
    ) -> dict:
        """Upsert de oportunidade."""
        return self._chamar_api(
            call='UpsertOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "identificacao": identificacao
            }
        )

    def obter_lista_op(
            self, cMesAno, cTemperatura
    ) -> dict:
        """Lista de Oportunidades."""
        return self._chamar_api(
            call='ObterListaOp',
            endpoint='crm/oportunidades-resumo/',
            param={
                "cMesAno": cMesAno,
                "cTemperatura": cTemperatura
            }
        )