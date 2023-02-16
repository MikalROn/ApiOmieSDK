from ..core.omiebase import OmieBase


class PedidoCompra(OmieBase):
    """ Classe que carrega metodos de pedidos de compra """

    def altera_ped_compra(
            self, cabecalho_alterar, frete_alterar, departamentos_alterar, produtos_alterar
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlteraPedCompra',
            endpoint='produtos/pedidocompra/',
            param={
                "cabecalho_alterar": cabecalho_alterar,
                "frete_alterar": frete_alterar,
                "departamentos_alterar": departamentos_alterar,
                "produtos_alterar": produtos_alterar
            }
        )

    def consultar_ped_compra(
            self, nCodPed, cCodIntPed, cNumero
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarPedCompra',
            endpoint='produtos/pedidocompra/',
            param={
                "nCodPed": nCodPed,
                "cCodIntPed": cCodIntPed,
                "cNumero": cNumero
            }
        )

    def excluir_ped_compra(
            self, nCodPed, cCodIntPed
    ) -> dict:
        """Excluir um Pedido de Compra"""
        return self._chamar_api(
            call='ExcluirPedCompra',
            endpoint='produtos/pedidocompra/',
            param={
                "nCodPed": nCodPed,
                "cCodIntPed": cCodIntPed
            }
        )

    def incluir_ped_compra(
            self, cabecalho_incluir, frete_incluir, departamentos_incluir, produtos_incluir
    ) -> dict:
        """Incluir um Pedido de Compra"""
        return self._chamar_api(
            call='IncluirPedCompra',
            endpoint='produtos/pedidocompra/',
            param={
                "cabecalho_incluir": cabecalho_incluir,
                "frete_incluir": frete_incluir,
                "departamentos_incluir": departamentos_incluir,
                "produtos_incluir": produtos_incluir
            }
        )

    def pesquisar_ped_compra(
            self, nPagina, nRegsPorPagina, lApenasImportadoApi, lExibirPedidosPendentes, lExibirPedidosFaturados,
            lExibirPedidosRecebidos, lExibirPedidosCancelados, lExibirPedidosEncerrados, lExibirPedidosRecParciais,
            lExibirPedidosFatParciais, dDataInicial, dDataFinal, lApenasAlterados
    ) -> dict:
        """"""
        return self._chamar_api(
            call='PesquisarPedCompra',
            endpoint='produtos/pedidocompra/',
            param={
                "nPagina": nPagina,
                "nRegsPorPagina": nRegsPorPagina,
                "lApenasImportadoApi": lApenasImportadoApi,
                "lExibirPedidosPendentes": lExibirPedidosPendentes,
                "lExibirPedidosFaturados": lExibirPedidosFaturados,
                "lExibirPedidosRecebidos": lExibirPedidosRecebidos,
                "lExibirPedidosCancelados": lExibirPedidosCancelados,
                "lExibirPedidosEncerrados": lExibirPedidosEncerrados,
                "lExibirPedidosRecParciais": lExibirPedidosRecParciais,
                "lExibirPedidosFatParciais": lExibirPedidosFatParciais,
                "dDataInicial": dDataInicial,
                "dDataFinal": dDataFinal,
                "lApenasAlterados": lApenasAlterados
            }
        )

    def upsert_ped_compra(
            self, cabecalho_upsert, frete_upsert, departamentos_upsert, produtos_upsert
    ) -> dict:
        """"""
        return self._chamar_api(
            call='UpsertPedCompra',
            endpoint='produtos/pedidocompra/',
            param={
                "cabecalho_upsert": cabecalho_upsert,
                "frete_upsert": frete_upsert,
                "departamentos_upsert": departamentos_upsert,
                "produtos_upsert": produtos_upsert
            }
        )