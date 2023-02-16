from ..core.omiebase import OmieBase


class NotaEntrada(OmieBase):
    """ Classe que carrega metodos de notas de entrada """
    def alterar_nota_ent(
            self, cabec, infAdic, produtos
    ) -> dict:
        """Alterar nota de entrada"""
        return self._chamar_api(
            call='AlterarNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "cabec": cabec,
                "infAdic": infAdic,
                "produtos": produtos
            }
        )

    def consultar_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Consultar nota de entrada"""
        return self._chamar_api(
            call='ConsultarNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt
            }
        )

    def excluir_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Excluir nota de entrada"""
        return self._chamar_api(
            call='ExcluirNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt
            }
        )

    def incluir_nota_ent(
            self, cabec, infAdic, produtos
    ) -> dict:
        """Incluir nota de entrada"""
        return self._chamar_api(
            call='IncluirNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "cabec": cabec,
                "infAdic": infAdic,
                "produtos": produtos
            }
        )

    def listar_nota_ent(
            self, nPagina, nRegistrosPorPagina
    ) -> dict:
        """Listagem de nota de entrada"""
        return self._chamar_api(
            call='ListarNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "nPagina": nPagina,
                "nRegistrosPorPagina": nRegistrosPorPagina
            }
        )

    def status_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Status de nota de entrada"""
        return self._chamar_api(
            call='StatusNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt
            }
        )

    def cancelar_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Cancelar nota de entrada"""
        return self._chamar_api(
            call='CancelarNotaEnt',
            endpoint='produtos/notaentradafat/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt
            }
        )

    def concluir_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Concluir nota de entrada"""
        return self._chamar_api(
            call='ConcluirNotaEnt',
            endpoint='produtos/notaentradafat/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt
            }
        )

    def conferir_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Conferir nota de entrada"""
        return self._chamar_api(
            call='ConferirNotaEnt',
            endpoint='produtos/notaentradafat/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt
            }
        )

    def duplicar_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Duplicar nota de entrada"""
        return self._chamar_api(
            call='DuplicarNotaEnt',
            endpoint='produtos/notaentradafat/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt
            }
        )

    def alterar_etapa_recebimento(
            self, nIdReceb, cChaveNfe, cEtapa
    ) -> dict:
        """Alterar etapa recebimento NFe"""
        return self._chamar_api(
            call='AlterarEtapaRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "nIdReceb": nIdReceb,
                "cChaveNfe": cChaveNfe,
                "cEtapa": cEtapa
            }
        )

    def alterar_recebimento(
            self, ide, itensRecebimentoEditar
    ) -> dict:
        """Alterar recebimento de NFe"""
        return self._chamar_api(
            call='AlterarRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "ide": ide,
                "itensRecebimentoEditar": itensRecebimentoEditar
            }
        )

    def concluir_recebimento(
            self, nIdReceb, cChaveNfe, cEtapa
    ) -> dict:
        """Concluir recebimento de NFe"""
        return self._chamar_api(
            call='ConcluirRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "nIdReceb": nIdReceb,
                "cChaveNfe": cChaveNfe,
                "cEtapa": cEtapa
            }
        )

    def consultar_recebimento(
            self, nIdReceb, cChaveNfe
    ) -> dict:
        """Consultar recebimento de NFe"""
        return self._chamar_api(
            call='ConsultarRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "nIdReceb": nIdReceb,
                "cChaveNfe": cChaveNfe
            }
        )

    def listar_recebimentos(
            self, nPagina, nRegistrosPorPagina
    ) -> dict:
        """Listar recebimento de NFe"""
        return self._chamar_api(
            call='ListarRecebimentos',
            endpoint='produtos/recebimentonfe/',
            param={
                "nPagina": nPagina,
                "nRegistrosPorPagina": nRegistrosPorPagina
            }
        )

    def reverter_recebimento(
            self, nIdReceb, cChaveNfe, cEtapa
    ) -> dict:
        """Reverter recebimento NFe"""
        return self._chamar_api(
            call='ReverterRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "nIdReceb": nIdReceb,
                "cChaveNfe": cChaveNfe,
                "cEtapa": cEtapa
            }
        )
    
    def obter_resumo_compra(
            self, dDataInicio, dDataFim
    ) -> dict:
        """Reverter recebimento NFe"""
        return self._chamar_api(
            call='ReverterRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "dDataInicio": dDataInicio,
                "dDataFim": dDataFim
            }
        )