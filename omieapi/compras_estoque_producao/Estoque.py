from ..core import OmieBase


class Estoque(OmieBase):
    def alterar_estoque_minimo(
            self, codigo_local_estoque, id_prod, cod_int, quan_min
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarEstoqueMinimo',
            endpoint='estoque/ajuste/',
            param={
                "codigo_local_estoque": codigo_local_estoque,
                "id_prod": id_prod,
                "cod_int": cod_int,
                "quan_min": quan_min
            }
        )

    def excluir_ajuste_estoque(
            self, id_ajuste
    ) -> dict:
        """Excluir um Movimento de Ajuste de Estoque"""
        return self._chamar_api(
            call='ExcluirAjusteEstoque',
            endpoint='estoque/ajuste/',
            param={
                "id_ajuste": id_ajuste
            }
        )

    def incluir_ajuste_estoque(
            self, codigo_local_estoque, id_prod, data, quan, obs, origem, tipo, motivo, valor
    ) -> dict:
        """Incluir um Ajuste de Estoque"""
        return self._chamar_api(
            call='IncluirAjusteEstoque',
            endpoint='estoque/ajuste/',
            param={
                "codigo_local_estoque": codigo_local_estoque,
                "id_prod": id_prod,
                "data": data,
                "quan": quan,
                "obs": obs,
                "origem": origem,
                "tipo": tipo,
                "motivo": motivo,
                "valor": valor
            }
        )

    def listar_ajuste_estoque(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Listar os ajuste de estoque."""
        return self._chamar_api(
            call='ListarAjusteEstoque',
            endpoint='estoque/ajuste/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api
            }
        )

    def listar_movimento_estoque(
            self, nPagina, nRegPorPagina, codigo_local_estoque, idProd, dDtInicial, dDtFinal, lista_local_estoque
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarMovimentoEstoque',
            endpoint='estoque/consulta/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,
                "codigo_local_estoque": codigo_local_estoque,
                "idProd": idProd,
                "dDtInicial": dDtInicial,
                "dDtFinal": dDtFinal,
                "lista_local_estoque": lista_local_estoque
            }
        )

    def listar_pos_estoque(
            self, nPagina, nRegPorPagina, dDataPosicao, cExibeTodos, codigo_local_estoque
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarPosEstoque',
            endpoint='estoque/consulta/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,
                "dDataPosicao": dDataPosicao,
                "cExibeTodos": cExibeTodos,
                "codigo_local_estoque": codigo_local_estoque
            }
        )

    def listar_saldo_pendente(
            self, pagina, registros_por_pagina, codigo_local_estoque, id_prod, tipo
    ) -> dict:
        """Lista o saldo pendente de estoque."""
        return self._chamar_api(
            call='ListarSaldoPendente',
            endpoint='estoque/consulta/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "codigo_local_estoque": codigo_local_estoque,
                "id_prod": id_prod,
                "tipo": tipo
            }
        )

    def movimento_estoque(
            self, codigo_local_estoque, id_prod, cod_int, dataInicial, dataFinal
    ) -> dict:
        """Consulta do Movimento de Estoque"""
        return self._chamar_api(
            call='MovimentoEstoque',
            endpoint='estoque/consulta/',
            param={
                "codigo_local_estoque": codigo_local_estoque,
                "id_prod": id_prod,
                "cod_int": cod_int,
                "dataInicial": dataInicial,
                "dataFinal": dataFinal
            }
        )

    def posicao_estoque(
            self, codigo_local_estoque, id_prod, cod_int, data
    ) -> dict:
        """"""
        return self._chamar_api(
            call='PosicaoEstoque',
            endpoint='estoque/consulta/',
            param={
                "codigo_local_estoque": codigo_local_estoque,
                "id_prod": id_prod,
                "cod_int": cod_int,
                "data": data
            }
        )

    def consultar_previsao(
            self, nCodProd
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarPrevisao',
            endpoint='estoque/movestoque/',
            param={
                "nCodProd": nCodProd
            }
        )

    def listar_movimentos(
            self, pagina, registros_por_pagina, codigo_local_estoque
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarMovimentos',
            endpoint='estoque/movestoque/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "codigo_local_estoque": codigo_local_estoque
            }
        )

    def listar_locais_estoque(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """Lista os Locais de Estoque encontrados."""
        return self._chamar_api(
            call='ListarLocaisEstoque',
            endpoint='estoque/local/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina
            }
        )

    def obter_estoque_produto(
            self, cEAN, nIdProduto, cCodigo, dDia
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ObterEstoqueProduto',
            endpoint='estoque/resumo/',
            param={
                "cEAN": cEAN,
                "nIdProduto": nIdProduto,
                "cCodigo": cCodigo,
                "dDia": dDia
            }
        )