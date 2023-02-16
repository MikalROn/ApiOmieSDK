from omieapi.omiebase import OmieBase


class Tarefas(OmieBase):
    """ Classe que carrrega todos os metodos relacionados a tarefas """

    def alterar_tarefa(
            self, nCodTarefa, nCodOp, cCodInt, nCodUsuario, dData, cHora, nCodNotif, nCodAtividade, cDescricao
    ) -> dict:
        """Altera uma tarefa."""
        return self._chamar_api(
            call='AlterarTarefa',
            endpoint='crm/tarefas/',
            param={
                "nCodTarefa": nCodTarefa,
                "nCodOp": nCodOp,
                "cCodInt": cCodInt,
                "nCodUsuario": nCodUsuario,
                "dData": dData,
                "cHora": cHora,
                "nCodNotif": nCodNotif,
                "nCodAtividade": nCodAtividade,
                "cDescricao": cDescricao
            }
        )

    def calendario_tarefas(
            self, email_vend, calendar_key
    ) -> dict:
        """"""
        return self._chamar_api(
            call='CalendarioTarefas',
            endpoint='crm/tarefas/',
            param={
                "email_vend": email_vend,
                "calendar_key": calendar_key
            }
        )

    def consultar_tarefa(
            self, nCodTarefa, nCodOp, cCodInt
    ) -> dict:
        """Consulta uma tarefa da oportunidade."""
        return self._chamar_api(
            call='ConsultarTarefa',
            endpoint='crm/tarefas/',
            param={
                "nCodTarefa": nCodTarefa,
                "nCodOp": nCodOp,
                "cCodInt": cCodInt
            }
        )

    def excluir_tarefa(
            self, nCodTarefa, nCodOp, cCodInt
    ) -> dict:
        """Exclui um tarefa."""
        return self._chamar_api(
            call='ExcluirTarefa',
            endpoint='crm/tarefas/',
            param={
                "nCodTarefa": nCodTarefa,
                "nCodOp": nCodOp,
                "cCodInt": cCodInt
            }
        )

    def incluir_tarefa(
            self, nCodOp, cCodInt, nCodUsuario, dData, cHora, nCodNotif, nCodAtividade, cDescricao
    ) -> dict:
        """Inclui uma tarefa na oportunidade."""
        return self._chamar_api(
            call='IncluirTarefa',
            endpoint='crm/tarefas/',
            param={
                "nCodOp": nCodOp,
                "cCodInt": cCodInt,
                "nCodUsuario": nCodUsuario,
                "dData": dData,
                "cHora": cHora,
                "nCodNotif": nCodNotif,
                "nCodAtividade": nCodAtividade,
                "cDescricao": cDescricao
            }
        )

    def listar_emails_tarefas(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista os  emails tarefas."""
        return self._chamar_api(
            call='ListarEmailsTarefas',
            endpoint='crm/tarefas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_tarefas(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Tarefas da oportunidade."""
        return self._chamar_api(
            call='ListarTarefas',
            endpoint='crm/tarefas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def upsert_tarefa(
            self, nCodTarefa, nCodOp, cCodInt, nCodUsuario, dData, cHora, nCodNotif, nCodAtividade, cDescricao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='UpsertTarefa',
            endpoint='crm/tarefas/',
            param={
                "nCodTarefa": nCodTarefa,
                "nCodOp": nCodOp,
                "cCodInt": cCodInt,
                "nCodUsuario": nCodUsuario,
                "dData": dData,
                "cHora": cHora,
                "nCodNotif": nCodNotif,
                "nCodAtividade": nCodAtividade,
                "cDescricao": cDescricao
            }
        )

    def obter_detalhes_tarefa(
            self, nIdOportunidade, nIdTarefa
    ) -> dict:
        """Consulta os detalhes de uma tafera."""
        return self._chamar_api(
            call='ObterDetalhesTarefa',
            endpoint='crm/tarefas-resumo/',
            param={
                "nIdOportunidade": nIdOportunidade,
                "nIdTarefa": nIdTarefa
            }
        )

    def obter_lista_tarefas(
            self, dDia
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ObterListaTarefas',
            endpoint='crm/tarefas-resumo/',
            param={
                "dDia": dDia
            }
        )

    def obter_resumo_tarefas(
            self, dDataInicio, dDataFim, cTipoTarefa
    ) -> dict:
        """Resumos das tarefas do CRM."""
        return self._chamar_api(
            call='ObterResumoTarefas',
            endpoint='crm/tarefas-resumo/',
            param={
                "dDataInicio": dDataInicio,
                "dDataFim": dDataFim,
                "cTipoTarefa": cTipoTarefa
            }
        )