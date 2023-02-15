from omiebase import OmieBase

class Cliente( OmieBase ):
    """ Todos os metodos relacionados """
    def alterar_cliente(
            self, codigo_cliente_integracao, email, razao_social, nome_fantasia
    ) -> dict:
        """Altera os dados do cliente"""
        return self._chamar_api(
            call='AlterarCliente',
            endpoint='geral/clientes/',
            param={
                "codigo_cliente_integracao": codigo_cliente_integracao,
                "email": email,
                "razao_social": razao_social,
                "nome_fantasia": nome_fantasia,

            }
        )

    def AssociarCodIntCliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AssociarCodIntCliente',
            endpoint='geral/clientes/',
            param={
                "codigo_cliente_omie": codigo_cliente_omie,
                "codigo_cliente_integracao": codigo_cliente_integracao,
            }
        )

    def Consultar_Cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
    ) -> dict:
        """Consulta os dados de um cliente"""
        return self._chamar_api(
            call='ConsultarCliente',
            endpoint='geral/clientes/',
            param={
                "codigo_cliente_omie": codigo_cliente_omie,
                "codigo_cliente_integracao": codigo_cliente_integracao,

            }
        )

    def Excluir_Cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
    ) -> dict:
        """Exclui um cliente da base de dados."""
        return self._chamar_api(
            call='ExcluirCliente',
            endpoint='geral/clientes/',
            param={
                "codigo_cliente_omie": codigo_cliente_omie,
                "codigo_cliente_integracao": codigo_cliente_integracao,

            }
        )

    def Incluir_Cliente(
            self, codigo_cliente_integracao, email, razao_social, nome_fantasia
    ) -> dict:
        """Inclui o cliente no Omie"""
        return self._chamar_api(
            call='IncluirCliente',
            endpoint='geral/clientes/',
            param={
                "codigo_cliente_integracao": codigo_cliente_integracao,
                "email": email,
                "razao_social": razao_social,
                "nome_fantasia": nome_fantasia,

            }
        )

    def Incluir_Clientes_Por_Lote(
            self, clientes_cadastro, lote
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='IncluirClientesPorLote',
            endpoint='geral/clientes/',
            param={
                "clientes_cadastro": clientes_cadastro,
                "lote": lote,

            }
        )

    def Listar_Clientes(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Lista os clientes cadastrados"""
        return self._chamar_api(
            call='ListarClientes',
            endpoint='geral/clientes/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def Listar_Clientes_Resumido(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Realiza pesquisa dos clientes"""
        return self._chamar_api(
            call='ListarClientesResumido',
            endpoint='geral/clientes/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def Upsert_Cliente(
            self, codigo_cliente_integracao, email, razao_social, nome_fantasia
    ) -> dict:
        """"""
        return self._chamar_api(
            call='UpsertCliente',
            endpoint='geral/clientes/',
            param={
                "codigo_cliente_integracao": codigo_cliente_integracao,
                "email": email,
                "razao_social": razao_social,
                "nome_fantasia": nome_fantasia,

            }
        )

    def Upsert_Cliente_Cpf_Cnpj(
            self, cnpj_cpf, email, razao_social, nome_fantasia
    ) -> dict:
        """"""
        return self._chamar_api(
            call='UpsertClienteCpfCnpj',
            endpoint='geral/clientes/',
            param={
                "cnpj_cpf": cnpj_cpf,
                "email": email,
                "razao_social": razao_social,
                "nome_fantasia": nome_fantasia,

            }
        )

    def Upsert_Clientes_Por_Lote(
            self, clientes_cadastro, lote
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='UpsertClientesPorLote',
            endpoint='geral/clientes/',
            param={
                "clientes_cadastro": clientes_cadastro,
                "lote": lote,

            }
        )

    def Alterar_Caract_Cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao, campo, conteudo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarCaractCliente',
            endpoint='geral/clientescaract/',
            param={
                "codigo_cliente_omie": codigo_cliente_omie,
                "codigo_cliente_integracao": codigo_cliente_integracao,
                "campo": campo,
                "conteudo": conteudo,

            }
        )

    def Consultar_Caract_Cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarCaractCliente',
            endpoint='geral/clientescaract/',
            param={
                "codigo_cliente_omie": codigo_cliente_omie,
                "codigo_cliente_integracao": codigo_cliente_integracao,

            }
        )

    def Excluir_Caract_Cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao, campo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirCaractCliente',
            endpoint='geral/clientescaract/',
            param={
                "codigo_cliente_omie": codigo_cliente_omie,
                "codigo_cliente_integracao": codigo_cliente_integracao,
                "campo": campo,

            }
        )

    def Excluir_Todas_Caract_Cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirTodasCaractCliente',
            endpoint='geral/clientescaract/',
            param={
                "codigo_cliente_omie": codigo_cliente_omie,
                "codigo_cliente_integracao": codigo_cliente_integracao,

            }
        )

    def Incluir_Caract_Cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao, campo, conteudo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirCaractCliente',
            endpoint='geral/clientescaract/',
            param={
                "codigo_cliente_omie": codigo_cliente_omie,
                "codigo_cliente_integracao": codigo_cliente_integracao,
                "campo": campo,
                "conteudo": conteudo,

            }
        )