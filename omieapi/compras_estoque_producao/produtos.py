from omieapi.omiebase import OmieBase


class Produtos(OmieBase):
    """ Todos os metodos relacionados a produtos """
    def listar_produtos(
            self, registros: int, filtrar_pdv: bool, pagina: int,
            apenas_importado_api: bool
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

    def alterar_produto(
            self, codigo_produto_integracao, codigo, descricao, unidade
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarProduto',
            endpoint='geral/produtos/',
            param={
                "codigo_produto_integracao": codigo_produto_integracao,
                "codigo": codigo,
                "descricao": descricao,
                "unidade": unidade
            }
        )

    def associar_cod_int_produto(
            self, codigo_produto, codigo_produto_integracao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AssociarCodIntProduto',
            endpoint='geral/produtos/',
            param={
                "codigo_produto": codigo_produto,
                "codigo_produto_integracao": codigo_produto_integracao
            }
        )

    def consultar_produto(
            self, codigo_produto, codigo_produto_integracao, codigo
    ) -> dict:
        """Consulta um produto."""
        return self._chamar_api(
            call='ConsultarProduto',
            endpoint='geral/produtos/',
            param={
                "codigo_produto": codigo_produto,
                "codigo_produto_integracao": codigo_produto_integracao,
                "codigo": codigo
            }
        )

    def excluir_produto(
            self, codigo_produto, codigo_produto_integracao, codigo
    ) -> dict:
        """Exclui um produto"""
        return self._chamar_api(
            call='ExcluirProduto',
            endpoint='geral/produtos/',
            param={
                "codigo_produto": codigo_produto,
                "codigo_produto_integracao": codigo_produto_integracao,
                "codigo": codigo
            }
        )

    def incluir_produto(
            self, codigo_produto_integracao, codigo, descricao, unidade
    ) -> dict:
        """Incluir um produto."""
        return self._chamar_api(
            call='IncluirProduto',
            endpoint='geral/produtos/',
            param={
                "codigo_produto_integracao": codigo_produto_integracao,
                "codigo": codigo,
                "descricao": descricao,
                "unidade": unidade
            }
        )

    def incluir_produtos_por_lote(
            self, lote, produto_servico_cadastro
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='IncluirProdutosPorLote',
            endpoint='geral/produtos/',
            param={
                "lote": lote,
                "produto_servico_cadastro": produto_servico_cadastro
            }
        )

    def listar_produtos_resumido(
            self, pagina, registros_por_pagina, apenas_importado_api, filtrar_apenas_omiepdv
    ) -> dict:
        """Lista os produtos cadastrados"""
        return self._chamar_api(
            call='ListarProdutosResumido',
            endpoint='geral/produtos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,
                "filtrar_apenas_omiepdv": filtrar_apenas_omiepdv
            }
        )

    def upsert_produto(
            self, codigo_produto_integracao, codigo, descricao, unidade
    ) -> dict:
        """"""
        return self._chamar_api(
            call='UpsertProduto',
            endpoint='geral/produtos/',
            param={
                "codigo_produto_integracao": codigo_produto_integracao,
                "codigo": codigo,
                "descricao": descricao,
                "unidade": unidade
            }
        )

    def upsert_produtos_por_lote(
            self, lote, produto_servico_cadastro
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='UpsertProdutosPorLote',
            endpoint='geral/produtos/',
            param={
                "lote": lote,
                "produto_servico_cadastro": produto_servico_cadastro
            }
        )

    def alterar_caract_produto(
            self, nCodProd, cCodIntProd, nCodCaract, cCodIntCaract, cConteudo, cExibirItemNF, cExibirItemPedido,
            cExibirOrdemProd
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarCaractProduto',
            endpoint='geral/prodcaract/',
            param={
                "nCodProd": nCodProd,
                "cCodIntProd": cCodIntProd,
                "nCodCaract": nCodCaract,
                "cCodIntCaract": cCodIntCaract,
                "cConteudo": cConteudo,
                "cExibirItemNF": cExibirItemNF,
                "cExibirItemPedido": cExibirItemPedido,
                "cExibirOrdemProd": cExibirOrdemProd
            }
        )

    def consultar_caract_produto(
            self, nCodProd, cCodIntProd, nCodCaract, cCodIntCaract
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarCaractProduto',
            endpoint='geral/prodcaract/',
            param={
                "nCodProd": nCodProd,
                "cCodIntProd": cCodIntProd,
                "nCodCaract": nCodCaract,
                "cCodIntCaract": cCodIntCaract
            }
        )

    def excluir_caract_produto(
            self, nCodProd, cCodIntProd, nCodCaract, cCodIntCaract
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirCaractProduto',
            endpoint='geral/prodcaract/',
            param={
                "nCodProd": nCodProd,
                "cCodIntProd": cCodIntProd,
                "nCodCaract": nCodCaract,
                "cCodIntCaract": cCodIntCaract
            }
        )

    def incluir_caract_produto(
            self, nCodProd, cCodIntProd, nCodCaract, cCodIntCaract, cConteudo, cExibirItemNF, cExibirItemPedido,
            cExibirOrdemProd
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirCaractProduto',
            endpoint='geral/prodcaract/',
            param={
                "nCodProd": nCodProd,
                "cCodIntProd": cCodIntProd,
                "nCodCaract": nCodCaract,
                "cCodIntCaract": cCodIntCaract,
                "cConteudo": cConteudo,
                "cExibirItemNF": cExibirItemNF,
                "cExibirItemPedido": cExibirItemPedido,
                "cExibirOrdemProd": cExibirOrdemProd
            }
        )

    def listar_caract_produto(
            self, nPagina, nRegPorPagina, nCodProd
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarCaractProduto',
            endpoint='geral/prodcaract/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,
                "nCodProd": nCodProd
            }
        )
