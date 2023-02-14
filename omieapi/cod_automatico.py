from omieapi import Omie


# Aviso -> antes de usar confira se não a oq vc precisa já feito no codigo principal,
# o codigo autogerdo pode conter erros não detectados ainda
class CodigoAutoGerado(Omie):
    """ Este codigo foi automaticamente geredo por um script de scrap """

    def AlterarCliente(
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

    def ConsultarCliente(
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

    def ExcluirCliente(
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

    def IncluirCliente(
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

    def IncluirClientesPorLote(
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

    def ListarClientes(
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

    def ListarClientesResumido(
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

    def UpsertCliente(
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

    def UpsertClienteCpfCnpj(
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

    def UpsertClientesPorLote(
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

    def AlterarCaractCliente(
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

    def ConsultarCaractCliente(
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

    def ExcluirCaractCliente(
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

    def ExcluirTodasCaractCliente(
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

    def IncluirCaractCliente(
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

    def ExcluirTags(
            self, nCodCliente, cCodIntCliente, tags
    ) -> dict:
        """Remove tags associadas a um cliente."""
        return self._chamar_api(
            call='ExcluirTags',
            endpoint='geral/clientetag/',
            param={
                "nCodCliente": nCodCliente,
                "cCodIntCliente": cCodIntCliente,
                "tags": tags,

            }
        )

    def ExcluirTodas(
            self, nCodCliente, cCodIntCliente
    ) -> dict:
        """Remove todas as tags associadas a um cliente."""
        return self._chamar_api(
            call='ExcluirTodas',
            endpoint='geral/clientetag/',
            param={
                "nCodCliente": nCodCliente,
                "cCodIntCliente": cCodIntCliente,

            }
        )

    def IncluirTags(
            self, nCodCliente, cCodIntCliente, tags
    ) -> dict:
        """Associa tags a um cliente."""
        return self._chamar_api(
            call='IncluirTags',
            endpoint='geral/clientetag/',
            param={
                "nCodCliente": nCodCliente,
                "cCodIntCliente": cCodIntCliente,
                "tags": tags,

            }
        )

    def ListarTags(
            self, nCodCliente, cCodIntCliente
    ) -> dict:
        """Lista as tags de um determinado cliente."""
        return self._chamar_api(
            call='ListarTags',
            endpoint='geral/clientetag/',
            param={
                "nCodCliente": nCodCliente,
                "cCodIntCliente": cCodIntCliente,

            }
        )

    def AlterarProjeto(
            self, codigo, codint, nome, inativo
    ) -> dict:
        """Altera um projeto"""
        return self._chamar_api(
            call='AlterarProjeto',
            endpoint='geral/projetos/',
            param={
                "codigo": codigo,
                "codint": codint,
                "nome": nome,
                "inativo": inativo,

            }
        )

    def ConsultarProjeto(
            self, codigo, codint
    ) -> dict:
        """Consulta um projeto"""
        return self._chamar_api(
            call='ConsultarProjeto',
            endpoint='geral/projetos/',
            param={
                "codigo": codigo,
                "codint": codint,

            }
        )

    def ExcluirProjeto(
            self, codigo, codint
    ) -> dict:
        """Exclui um projeto"""
        return self._chamar_api(
            call='ExcluirProjeto',
            endpoint='geral/projetos/',
            param={
                "codigo": codigo,
                "codint": codint,

            }
        )

    def IncluirProjeto(
            self, codint, nome, inativo
    ) -> dict:
        """Inclui um novo projeto"""
        return self._chamar_api(
            call='IncluirProjeto',
            endpoint='geral/projetos/',
            param={
                "codint": codint,
                "nome": nome,
                "inativo": inativo,

            }
        )

    def ListarProjetos(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Lista os projetos cadastrados"""
        return self._chamar_api(
            call='ListarProjetos',
            endpoint='geral/projetos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def UpsertProjeto(
            self, codigo, codint, nome, inativo
    ) -> dict:
        """Inclui / Altera um projeto."""
        return self._chamar_api(
            call='UpsertProjeto',
            endpoint='geral/projetos/',
            param={
                "codigo": codigo,
                "codint": codint,
                "nome": nome,
                "inativo": inativo,

            }
        )

    def ConsultarEmpresa(
            self, codigo_empresa
    ) -> dict:
        """Realiza a consulta de um registro especifico"""
        return self._chamar_api(
            call='ConsultarEmpresa',
            endpoint='geral/empresas/',
            param={
                "codigo_empresa": codigo_empresa,

            }
        )

    def ListarEmpresas(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Lista as empresas cadastradas no Omie."""
        return self._chamar_api(
            call='ListarEmpresas',
            endpoint='geral/empresas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def ConsultarDepartamento(
            self, codigo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarDepartamento',
            endpoint='geral/departamentos/',
            param={
                "codigo": codigo,

            }
        )

    def ListarDepatartamentos(
            self, pagina, registros_por_pagina
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='ListarDepatartamentos',
            endpoint='geral/departamentos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ConsultarCategoria(
            self, codigo
    ) -> dict:
        """Consulta uma categoria"""
        return self._chamar_api(
            call='ConsultarCategoria',
            endpoint='geral/categorias/',
            param={
                "codigo": codigo,

            }
        )

    def ListarCategorias(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista as categorias cadastradas"""
        return self._chamar_api(
            call='ListarCategorias',
            endpoint='geral/categorias/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarParcelas(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista de Parcelas cadastradas."""
        return self._chamar_api(
            call='ListarParcelas',
            endpoint='geral/parcelas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarTipoAtiv(
            self, filtrar_por_codigo, filtrar_por_descricao
    ) -> dict:
        """Listar Tipos de Atividade."""
        return self._chamar_api(
            call='ListarTipoAtiv',
            endpoint='geral/tpativ/',
            param={
                "filtrar_por_codigo": filtrar_por_codigo,
                "filtrar_por_descricao": filtrar_por_descricao,

            }
        )

    def ListarCNAE(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar os CNAEs cadastrados"""
        return self._chamar_api(
            call='ListarCNAE',
            endpoint='produtos/cnae/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def PesquisarCidades(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='PesquisarCidades',
            endpoint='geral/cidades/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarPaises(
            self, filtrar_por_codigo, filtrar_por_descricao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarPaises',
            endpoint='geral/paises/',
            param={
                "filtrar_por_codigo": filtrar_por_codigo,
                "filtrar_por_descricao": filtrar_por_descricao,

            }
        )

    def ListarTiposAnexos(
            self, codigo
    ) -> dict:
        """Listagem de tipos de anexos."""
        return self._chamar_api(
            call='ListarTiposAnexos',
            endpoint='geral/tiposanexo/',
            param={
                "codigo": codigo,

            }
        )

    def IncluirAnexo(
            self, cCodIntAnexo, cTabela, nId, cNomeArquivo, cTipoArquivo, cArquivo, cMd5
    ) -> dict:
        """Inclui o anexo para um documento."""
        return self._chamar_api(
            call='IncluirAnexo',
            endpoint='geral/anexo/',
            param={
                "cCodIntAnexo": cCodIntAnexo,
                "cTabela": cTabela,
                "nId": nId,
                "cNomeArquivo": cNomeArquivo,
                "cTipoArquivo": cTipoArquivo,
                "cArquivo": cArquivo,
                "cMd5": cMd5,

            }
        )

    def AlterarTipoEntrega(
            self, nCodEntrega, cCodIntEntrega, cDescricao, cInativo
    ) -> dict:
        """Alterar tipo de entrega"""
        return self._chamar_api(
            call='AlterarTipoEntrega',
            endpoint='geral/tiposentrega/',
            param={
                "nCodEntrega": nCodEntrega,
                "cCodIntEntrega": cCodIntEntrega,
                "cDescricao": cDescricao,
                "cInativo": cInativo,

            }
        )

    def ConsultarTipoEntrega(
            self, nCodEntrega, cCodIntEntrega
    ) -> dict:
        """Consultar tipo de entrega"""
        return self._chamar_api(
            call='ConsultarTipoEntrega',
            endpoint='geral/tiposentrega/',
            param={
                "nCodEntrega": nCodEntrega,
                "cCodIntEntrega": cCodIntEntrega,

            }
        )

    def ExcluirTipoEntrega(
            self, nCodEntrega, cCodIntEntrega
    ) -> dict:
        """Excluir tipo de entrega"""
        return self._chamar_api(
            call='ExcluirTipoEntrega',
            endpoint='geral/tiposentrega/',
            param={
                "nCodEntrega": nCodEntrega,
                "cCodIntEntrega": cCodIntEntrega,

            }
        )

    def IncluirTipoEntrega(
            self, nCodTransp, cCodIntEntrega, cDescricao, cInativo
    ) -> dict:
        """Incluir tipo de entrega"""
        return self._chamar_api(
            call='IncluirTipoEntrega',
            endpoint='geral/tiposentrega/',
            param={
                "nCodTransp": nCodTransp,
                "cCodIntEntrega": cCodIntEntrega,
                "cDescricao": cDescricao,
                "cInativo": cInativo,

            }
        )

    def ListarTipoEntrega(
            self, nPagina, nRegistrosPorPagina, nCodTransp
    ) -> dict:
        """Listar tipo de entrega"""
        return self._chamar_api(
            call='ListarTipoEntrega',
            endpoint='geral/tiposentrega/',
            param={
                "nPagina": nPagina,
                "nRegistrosPorPagina": nRegistrosPorPagina,
                "nCodTransp": nCodTransp,

            }
        )

    def ListarTipoAssinante(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista os tipos de assinante"""
        return self._chamar_api(
            call='ListarTipoAssinante',
            endpoint='geral/tipoassinante/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarContas(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista as contas do CRM."""
        return self._chamar_api(
            call='ListarContas',
            endpoint='crm/contas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def VerificarConta(
            self, cNome, cEmail
    ) -> dict:
        """Verifica se uma conta foi criada a partir do nome e e-mail."""
        return self._chamar_api(
            call='VerificarConta',
            endpoint='crm/contas/',
            param={
                "cNome": cNome,
                "cEmail": cEmail,

            }
        )

    def AlterarCaractConta(
            self, nCod, cCodInt, campo, conteudo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarCaractConta',
            endpoint='crm/contascaract/',
            param={
                "nCod": nCod,
                "cCodInt": cCodInt,
                "campo": campo,
                "conteudo": conteudo,

            }
        )

    def ConsultarCaractConta(
            self, nCod, cCodInt
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarCaractConta',
            endpoint='crm/contascaract/',
            param={
                "nCod": nCod,
                "cCodInt": cCodInt,

            }
        )

    def ExcluirCaractConta(
            self, nCod, cCodInt, campo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirCaractConta',
            endpoint='crm/contascaract/',
            param={
                "nCod": nCod,
                "cCodInt": cCodInt,
                "campo": campo,

            }
        )

    def ExcluirTodasCaractConta(
            self, nCod, cCodInt
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirTodasCaractConta',
            endpoint='crm/contascaract/',
            param={
                "nCod": nCod,
                "cCodInt": cCodInt,

            }
        )

    def IncluirCaractConta(
            self, nCod, cCodInt, campo, conteudo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirCaractConta',
            endpoint='crm/contascaract/',
            param={
                "nCod": nCod,
                "cCodInt": cCodInt,
                "campo": campo,
                "conteudo": conteudo,

            }
        )

    def ConsultarContato(
            self, nCod, cCodInt
    ) -> dict:
        """Consulta o Contato"""
        return self._chamar_api(
            call='ConsultarContato',
            endpoint='crm/contatos/',
            param={
                "nCod": nCod,
                "cCodInt": cCodInt,

            }
        )

    def IncluirContato(
            self, identificacao, endereco, telefone_email
    ) -> dict:
        """Inclui um novo Contato"""
        return self._chamar_api(
            call='IncluirContato',
            endpoint='crm/contatos/',
            param={
                "identificacao": identificacao,
                "endereco": endereco,
                "telefone_email": telefone_email,

            }
        )

    def ListarContatos(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista os contatos do CRM."""
        return self._chamar_api(
            call='ListarContatos',
            endpoint='crm/contatos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def UpsertContato(
            self, identificacao, endereco, telefone_email
    ) -> dict:
        """Upsert do contato"""
        return self._chamar_api(
            call='UpsertContato',
            endpoint='crm/contatos/',
            param={
                "identificacao": identificacao,
                "endereco": endereco,
                "telefone_email": telefone_email,

            }
        )

    def VerificarContato(
            self, cNome, cEmail
    ) -> dict:
        """"""
        return self._chamar_api(
            call='VerificarContato',
            endpoint='crm/contatos/',
            param={
                "cNome": cNome,
                "cEmail": cEmail,

            }
        )

    def AlterarOportunidade(
            self, identificacao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "identificacao": identificacao,

            }
        )

    def ConsultarOportunidade(
            self, nCodOp, cCodIntOp
    ) -> dict:
        """Consulta de oportunidade."""
        return self._chamar_api(
            call='ConsultarOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "nCodOp": nCodOp,
                "cCodIntOp": cCodIntOp,

            }
        )

    def ExcluirOportunidade(
            self, nCodOp, cCodIntOp
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "nCodOp": nCodOp,
                "cCodIntOp": cCodIntOp,

            }
        )

    def IncluirOportunidade(
            self, identificacao
    ) -> dict:
        """Incluir uma oportunidade."""
        return self._chamar_api(
            call='IncluirOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "identificacao": identificacao,

            }
        )

    def ListarOportunidades(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista de oportunidades."""
        return self._chamar_api(
            call='ListarOportunidades',
            endpoint='crm/oportunidades/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def UpsertOportunidade(
            self, identificacao
    ) -> dict:
        """Upsert de oportunidade."""
        return self._chamar_api(
            call='UpsertOportunidade',
            endpoint='crm/oportunidades/',
            param={
                "identificacao": identificacao,

            }
        )

    def ObterListaOp(
            self, cMesAno, cTemperatura
    ) -> dict:
        """Lista de Oportunidades."""
        return self._chamar_api(
            call='ObterListaOp',
            endpoint='crm/oportunidades-resumo/',
            param={
                "cMesAno": cMesAno,
                "cTemperatura": cTemperatura,

            }
        )

    def AlterarTarefa(
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
                "cDescricao": cDescricao,

            }
        )

    def CalendarioTarefas(
            self, email_vend, calendar_key
    ) -> dict:
        """"""
        return self._chamar_api(
            call='CalendarioTarefas',
            endpoint='crm/tarefas/',
            param={
                "email_vend": email_vend,
                "calendar_key": calendar_key,

            }
        )

    def ConsultarTarefa(
            self, nCodTarefa, nCodOp, cCodInt
    ) -> dict:
        """Consulta uma tarefa da oportunidade."""
        return self._chamar_api(
            call='ConsultarTarefa',
            endpoint='crm/tarefas/',
            param={
                "nCodTarefa": nCodTarefa,
                "nCodOp": nCodOp,
                "cCodInt": cCodInt,

            }
        )

    def ExcluirTarefa(
            self, nCodTarefa, nCodOp, cCodInt
    ) -> dict:
        """Exclui um tarefa."""
        return self._chamar_api(
            call='ExcluirTarefa',
            endpoint='crm/tarefas/',
            param={
                "nCodTarefa": nCodTarefa,
                "nCodOp": nCodOp,
                "cCodInt": cCodInt,

            }
        )

    def IncluirTarefa(
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
                "cDescricao": cDescricao,

            }
        )

    def ListarEmailsTarefas(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista os  emails tarefas."""
        return self._chamar_api(
            call='ListarEmailsTarefas',
            endpoint='crm/tarefas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarTarefas(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Tarefas da oportunidade."""
        return self._chamar_api(
            call='ListarTarefas',
            endpoint='crm/tarefas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def UpsertTarefa(
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
                "cDescricao": cDescricao,

            }
        )

    def ObterDetalhesTarefa(
            self, nIdOportunidade, nIdTarefa
    ) -> dict:
        """Consulta os detalhes de uma tafera."""
        return self._chamar_api(
            call='ObterDetalhesTarefa',
            endpoint='crm/tarefas-resumo/',
            param={
                "nIdOportunidade": nIdOportunidade,
                "nIdTarefa": nIdTarefa,

            }
        )

    def ObterListaTarefas(
            self, dDia
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ObterListaTarefas',
            endpoint='crm/tarefas-resumo/',
            param={
                "dDia": dDia,

            }
        )

    def ObterResumoTarefas(
            self, dDataInicio, dDataFim, cTipoTarefa
    ) -> dict:
        """Resumos das tarefas do CRM."""
        return self._chamar_api(
            call='ObterResumoTarefas',
            endpoint='crm/tarefas-resumo/',
            param={
                "dDataInicio": dDataInicio,
                "dDataFim": dDataFim,
                "cTipoTarefa": cTipoTarefa,

            }
        )

    def ListarSolucoes(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarSolucoes',
            endpoint='crm/solucoes/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarFases(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Fases da Oportunidade"""
        return self._chamar_api(
            call='ListarFases',
            endpoint='crm/fases/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarUsuarios(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarUsuarios',
            endpoint='crm/usuarios/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ObterUsuarios(
            self, cExibirTodos
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ObterUsuarios',
            endpoint='crm/usuarios/',
            param={
                "cExibirTodos": cExibirTodos,

            }
        )

    def ListarStatus(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Status da oportunidade."""
        return self._chamar_api(
            call='ListarStatus',
            endpoint='crm/status/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarMotivos(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Motivos da oportunidade."""
        return self._chamar_api(
            call='ListarMotivos',
            endpoint='crm/motivos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarTipos(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Tipos de oportunidades."""
        return self._chamar_api(
            call='ListarTipos',
            endpoint='crm/tipos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarParceiros(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Parceiros e equipes da oportunidade."""
        return self._chamar_api(
            call='ListarParceiros',
            endpoint='crm/parceiros/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarFinders(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Finders da oportunidade."""
        return self._chamar_api(
            call='ListarFinders',
            endpoint='crm/finders/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarOrigens(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Origens da oportunidade."""
        return self._chamar_api(
            call='ListarOrigens',
            endpoint='crm/origens/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarConcorrentes(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Concorrentes da oportunidade."""
        return self._chamar_api(
            call='ListarConcorrentes',
            endpoint='crm/concorrentes/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarVerticais(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista as verticais cadastradas."""
        return self._chamar_api(
            call='ListarVerticais',
            endpoint='crm/verticais/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def AlterarVendedor(
            self, codigo, codInt, nome, inativo, email, fatura_pedido, visualiza_pedido, comissao
    ) -> dict:
        """Altera os dados de um vendedor"""
        return self._chamar_api(
            call='AlterarVendedor',
            endpoint='geral/vendedores/',
            param={
                "codigo": codigo,
                "codInt": codInt,
                "nome": nome,
                "inativo": inativo,
                "email": email,
                "fatura_pedido": fatura_pedido,
                "visualiza_pedido": visualiza_pedido,
                "comissao": comissao,

            }
        )

    def ConsultarVendedor(
            self, codigo, codInt
    ) -> dict:
        """Consulta os dados de um vendedor"""
        return self._chamar_api(
            call='ConsultarVendedor',
            endpoint='geral/vendedores/',
            param={
                "codigo": codigo,
                "codInt": codInt,

            }
        )

    def ExcluirVendedor(
            self, codigo, codInt
    ) -> dict:
        """Exclui um vendedor"""
        return self._chamar_api(
            call='ExcluirVendedor',
            endpoint='geral/vendedores/',
            param={
                "codigo": codigo,
                "codInt": codInt,

            }
        )

    def IncluirVendedor(
            self, codInt, nome, inativo, email, fatura_pedido, visualiza_pedido, comissao
    ) -> dict:
        """Inclui um vendedor"""
        return self._chamar_api(
            call='IncluirVendedor',
            endpoint='geral/vendedores/',
            param={
                "codInt": codInt,
                "nome": nome,
                "inativo": inativo,
                "email": email,
                "fatura_pedido": fatura_pedido,
                "visualiza_pedido": visualiza_pedido,
                "comissao": comissao,

            }
        )

    def ListarVendedores(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Listagem de Vendedores"""
        return self._chamar_api(
            call='ListarVendedores',
            endpoint='geral/vendedores/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def UpsertVendedor(
            self, codigo, codInt, nome, inativo, email, fatura_pedido, visualiza_pedido, comissao
    ) -> dict:
        """Inclui / Altera um vendedor"""
        return self._chamar_api(
            call='UpsertVendedor',
            endpoint='geral/vendedores/',
            param={
                "codigo": codigo,
                "codInt": codInt,
                "nome": nome,
                "inativo": inativo,
                "email": email,
                "fatura_pedido": fatura_pedido,
                "visualiza_pedido": visualiza_pedido,
                "comissao": comissao,

            }
        )

    def ConsultarTipoTarefa(
            self, nIdTipoTarefa
    ) -> dict:
        """Consulta tipo de tarefa"""
        return self._chamar_api(
            call='ConsultarTipoTarefa',
            endpoint='crm/tipostarefa/',
            param={
                "nIdTipoTarefa": nIdTipoTarefa,

            }
        )

    def ExcluirTipoTarefa(
            self, nIdTipoTarefa
    ) -> dict:
        """Excluir tipo de tarefa"""
        return self._chamar_api(
            call='ExcluirTipoTarefa',
            endpoint='crm/tipostarefa/',
            param={
                "nIdTipoTarefa": nIdTipoTarefa,

            }
        )

    def ListarTiposTarefa(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista tipos de tarefa"""
        return self._chamar_api(
            call='ListarTiposTarefa',
            endpoint='crm/tipostarefa/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def AlterarContaCorrente(
            self, cCodCCInt, tipo_conta_corrente, codigo_banco, descricao, saldo_inicial
    ) -> dict:
        """Altera a Conta Corrente"""
        return self._chamar_api(
            call='AlterarContaCorrente',
            endpoint='geral/contacorrente/',
            param={
                "cCodCCInt": cCodCCInt,
                "tipo_conta_corrente": tipo_conta_corrente,
                "codigo_banco": codigo_banco,
                "descricao": descricao,
                "saldo_inicial": saldo_inicial,

            }
        )

    def ConsultarContaCorrente(
            self, nCodCC, cCodCCInt
    ) -> dict:
        """Realiza a consulta de uma conta corrente"""
        return self._chamar_api(
            call='ConsultarContaCorrente',
            endpoint='geral/contacorrente/',
            param={
                "nCodCC": nCodCC,
                "cCodCCInt": cCodCCInt,

            }
        )

    def ExcluirContaCorrente(
            self, nCodCC, cCodCCInt
    ) -> dict:
        """Excluir a Conta Corrente"""
        return self._chamar_api(
            call='ExcluirContaCorrente',
            endpoint='geral/contacorrente/',
            param={
                "nCodCC": nCodCC,
                "cCodCCInt": cCodCCInt,

            }
        )

    def IncluirContaCorrente(
            self, cCodCCInt, tipo_conta_corrente, codigo_banco, descricao, saldo_inicial
    ) -> dict:
        """Inclui uma conta corrente"""
        return self._chamar_api(
            call='IncluirContaCorrente',
            endpoint='geral/contacorrente/',
            param={
                "cCodCCInt": cCodCCInt,
                "tipo_conta_corrente": tipo_conta_corrente,
                "codigo_banco": codigo_banco,
                "descricao": descricao,
                "saldo_inicial": saldo_inicial,

            }
        )

    def ListarContasCorrentes(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Listar Contas Correntes"""
        return self._chamar_api(
            call='ListarContasCorrentes',
            endpoint='geral/contacorrente/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def ListarResumoContasCorrentes(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Listar resumida de Contas correntes."""
        return self._chamar_api(
            call='ListarResumoContasCorrentes',
            endpoint='geral/contacorrente/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def PesquisarContaCorrente(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='PesquisarContaCorrente',
            endpoint='geral/contacorrente/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def UpsertContaCorrente(
            self, cCodCCInt, tipo_conta_corrente, codigo_banco, descricao, saldo_inicial
    ) -> dict:
        """Upsert da Conta Corrente"""
        return self._chamar_api(
            call='UpsertContaCorrente',
            endpoint='geral/contacorrente/',
            param={
                "cCodCCInt": cCodCCInt,
                "tipo_conta_corrente": tipo_conta_corrente,
                "codigo_banco": codigo_banco,
                "descricao": descricao,
                "saldo_inicial": saldo_inicial,

            }
        )

    def UpsertContaCorrentePorLote(
            self, lote, fin_conta_corrente_cadastro
    ) -> dict:
        """Upsert por lote de Conta Corrente"""
        return self._chamar_api(
            call='UpsertContaCorrentePorLote',
            endpoint='geral/contacorrente/',
            param={
                "lote": lote,
                "fin_conta_corrente_cadastro": fin_conta_corrente_cadastro,

            }
        )

    def AlterarLancCC(
            self, cCodIntLanc, cabecalho, detalhes
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarLancCC',
            endpoint='financas/contacorrentelancamentos/',
            param={
                "cCodIntLanc": cCodIntLanc,
                "cabecalho": cabecalho,
                "detalhes": detalhes,

            }
        )

    def ConsultaLancCC(
            self, nCodLanc, cCodIntLanc
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultaLancCC',
            endpoint='financas/contacorrentelancamentos/',
            param={
                "nCodLanc": nCodLanc,
                "cCodIntLanc": cCodIntLanc,

            }
        )

    def ExcluirLancCC(
            self, nCodLanc, cCodIntLanc
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirLancCC',
            endpoint='financas/contacorrentelancamentos/',
            param={
                "nCodLanc": nCodLanc,
                "cCodIntLanc": cCodIntLanc,

            }
        )

    def IncluirLancCC(
            self, cCodIntLanc, cabecalho, detalhes
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirLancCC',
            endpoint='financas/contacorrentelancamentos/',
            param={
                "cCodIntLanc": cCodIntLanc,
                "cabecalho": cabecalho,
                "detalhes": detalhes,

            }
        )

    def ListarLancCC(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarLancCC',
            endpoint='financas/contacorrentelancamentos/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def AlterarContaPagar(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento,
            codigo_categoria, data_previsao, id_conta_corrente
    ) -> dict:
        """Altera uma conta a pagar"""
        return self._chamar_api(
            call='AlterarContaPagar',
            endpoint='financas/contapagar/',
            param={
                "codigo_lancamento_integracao": codigo_lancamento_integracao,
                "codigo_cliente_fornecedor": codigo_cliente_fornecedor,
                "data_vencimento": data_vencimento,
                "valor_documento": valor_documento,
                "codigo_categoria": codigo_categoria,
                "data_previsao": data_previsao,
                "id_conta_corrente": id_conta_corrente,

            }
        )

    def CancelarPagamento(
            self, codigo_baixa
    ) -> dict:
        """Cancela um pagamento realizado no Contas a Pagar"""
        return self._chamar_api(
            call='CancelarPagamento',
            endpoint='financas/contapagar/',
            param={
                "codigo_baixa": codigo_baixa,

            }
        )

    def ConsultarContaPagar(
            self, codigo_lancamento_omie, codigo_lancamento_integracao
    ) -> dict:
        """Consulta uma conta a pagar"""
        return self._chamar_api(
            call='ConsultarContaPagar',
            endpoint='financas/contapagar/',
            param={
                "codigo_lancamento_omie": codigo_lancamento_omie,
                "codigo_lancamento_integracao": codigo_lancamento_integracao,

            }
        )

    def ExcluirContaPagar(
            self, codigo_lancamento_omie, codigo_lancamento_integracao
    ) -> dict:
        """Exclui uma conta a pagar"""
        return self._chamar_api(
            call='ExcluirContaPagar',
            endpoint='financas/contapagar/',
            param={
                "codigo_lancamento_omie": codigo_lancamento_omie,
                "codigo_lancamento_integracao": codigo_lancamento_integracao,

            }
        )

    def IncluirContaPagar(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento,
            codigo_categoria, data_previsao, id_conta_corrente
    ) -> dict:
        """Inclui uma conta a Pagar."""
        return self._chamar_api(
            call='IncluirContaPagar',
            endpoint='financas/contapagar/',
            param={
                "codigo_lancamento_integracao": codigo_lancamento_integracao,
                "codigo_cliente_fornecedor": codigo_cliente_fornecedor,
                "data_vencimento": data_vencimento,
                "valor_documento": valor_documento,
                "codigo_categoria": codigo_categoria,
                "data_previsao": data_previsao,
                "id_conta_corrente": id_conta_corrente,

            }
        )

    def IncluirContaPagarPorLote(
            self, lote, conta_pagar_cadastro
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirContaPagarPorLote',
            endpoint='financas/contapagar/',
            param={
                "lote": lote,
                "conta_pagar_cadastro": conta_pagar_cadastro,

            }
        )

    def LancarPagamento(
            self, codigo_lancamento, codigo_lancamento_integracao, codigo_baixa_integracao, codigo_conta_corrente,
            valor, desconto, juros, multa, data, observacao
    ) -> dict:
        """Efetua a baixa de um pagamento do contas a pagar."""
        return self._chamar_api(
            call='LancarPagamento',
            endpoint='financas/contapagar/',
            param={
                "codigo_lancamento": codigo_lancamento,
                "codigo_lancamento_integracao": codigo_lancamento_integracao,
                "codigo_baixa_integracao": codigo_baixa_integracao,
                "codigo_conta_corrente": codigo_conta_corrente,
                "valor": valor,
                "desconto": desconto,
                "juros": juros,
                "multa": multa,
                "data": data,
                "observacao": observacao,

            }
        )

    def ListarContasPagar(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Listar as Contas a Pagar"""
        return self._chamar_api(
            call='ListarContasPagar',
            endpoint='financas/contapagar/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def UpsertContaPagar(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento,
            codigo_categoria, data_previsao, id_conta_corrente
    ) -> dict:
        """Upsert do Contas a Pagar"""
        return self._chamar_api(
            call='UpsertContaPagar',
            endpoint='financas/contapagar/',
            param={
                "codigo_lancamento_integracao": codigo_lancamento_integracao,
                "codigo_cliente_fornecedor": codigo_cliente_fornecedor,
                "data_vencimento": data_vencimento,
                "valor_documento": valor_documento,
                "codigo_categoria": codigo_categoria,
                "data_previsao": data_previsao,
                "id_conta_corrente": id_conta_corrente,

            }
        )

    def UpsertContaPagarPorLote(
            self, lote, conta_pagar_cadastro
    ) -> dict:
        """Efetua o UPSERT do Contas a Pagar por Lote"""
        return self._chamar_api(
            call='UpsertContaPagarPorLote',
            endpoint='financas/contapagar/',
            param={
                "lote": lote,
                "conta_pagar_cadastro": conta_pagar_cadastro,

            }
        )

    def AlterarContaReceber(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento,
            codigo_categoria, data_previsao, id_conta_corrente
    ) -> dict:
        """Altera um conta a receber"""
        return self._chamar_api(
            call='AlterarContaReceber',
            endpoint='financas/contareceber/',
            param={
                "codigo_lancamento_integracao": codigo_lancamento_integracao,
                "codigo_cliente_fornecedor": codigo_cliente_fornecedor,
                "data_vencimento": data_vencimento,
                "valor_documento": valor_documento,
                "codigo_categoria": codigo_categoria,
                "data_previsao": data_previsao,
                "id_conta_corrente": id_conta_corrente,

            }
        )

    def CancelarContaReceber(
            self, chave_lancamento
    ) -> dict:
        """Cancelamento do boleto gerado de uma conta a receber"""
        return self._chamar_api(
            call='CancelarContaReceber',
            endpoint='financas/contareceber/',
            param={
                "chave_lancamento": chave_lancamento,

            }
        )

    def CancelarRecebimento(
            self, codigo_baixa
    ) -> dict:
        """Efetua o cancelamento de um recebimento de Contas a Receber."""
        return self._chamar_api(
            call='CancelarRecebimento',
            endpoint='financas/contareceber/',
            param={
                "codigo_baixa": codigo_baixa,

            }
        )

    def ConciliarRecebimento(
            self, codigo_baixa
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConciliarRecebimento',
            endpoint='financas/contareceber/',
            param={
                "codigo_baixa": codigo_baixa,

            }
        )

    def ConsultarContaReceber(
            self, codigo_lancamento_omie, codigo_lancamento_integracao
    ) -> dict:
        """Consulta uma Conta a Pagar"""
        return self._chamar_api(
            call='ConsultarContaReceber',
            endpoint='financas/contareceber/',
            param={
                "codigo_lancamento_omie": codigo_lancamento_omie,
                "codigo_lancamento_integracao": codigo_lancamento_integracao,

            }
        )

    def DesconciliarRecebimento(
            self, codigo_baixa
    ) -> dict:
        """Desconciliar o Recebimento"""
        return self._chamar_api(
            call='DesconciliarRecebimento',
            endpoint='financas/contareceber/',
            param={
                "codigo_baixa": codigo_baixa,

            }
        )

    def ExcluirContaReceber(
            self, chave_lancamento
    ) -> dict:
        """Exclui uma conta a receber"""
        return self._chamar_api(
            call='ExcluirContaReceber',
            endpoint='financas/contareceber/',
            param={
                "chave_lancamento": chave_lancamento,

            }
        )

    def IncluirContaReceber(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento,
            codigo_categoria, data_previsao, id_conta_corrente
    ) -> dict:
        """Inclui uma conta a Receber"""
        return self._chamar_api(
            call='IncluirContaReceber',
            endpoint='financas/contareceber/',
            param={
                "codigo_lancamento_integracao": codigo_lancamento_integracao,
                "codigo_cliente_fornecedor": codigo_cliente_fornecedor,
                "data_vencimento": data_vencimento,
                "valor_documento": valor_documento,
                "codigo_categoria": codigo_categoria,
                "data_previsao": data_previsao,
                "id_conta_corrente": id_conta_corrente,

            }
        )

    def IncluirContaReceberPorLote(
            self, lote, conta_receber_cadastro
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirContaReceberPorLote',
            endpoint='financas/contareceber/',
            param={
                "lote": lote,
                "conta_receber_cadastro": conta_receber_cadastro,

            }
        )

    def LancarRecebimento(
            self, codigo_lancamento, codigo_baixa, codigo_conta_corrente, valor, data, observacao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='LancarRecebimento',
            endpoint='financas/contareceber/',
            param={
                "codigo_lancamento": codigo_lancamento,
                "codigo_baixa": codigo_baixa,
                "codigo_conta_corrente": codigo_conta_corrente,
                "valor": valor,
                "data": data,
                "observacao": observacao,

            }
        )

    def ListarContasReceber(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Lista as contas a receber cadastradas."""
        return self._chamar_api(
            call='ListarContasReceber',
            endpoint='financas/contareceber/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def UpsertContaReceber(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento,
            codigo_categoria, data_previsao, id_conta_corrente
    ) -> dict:
        """Executa o Upsert do Contas a receber"""
        return self._chamar_api(
            call='UpsertContaReceber',
            endpoint='financas/contareceber/',
            param={
                "codigo_lancamento_integracao": codigo_lancamento_integracao,
                "codigo_cliente_fornecedor": codigo_cliente_fornecedor,
                "data_vencimento": data_vencimento,
                "valor_documento": valor_documento,
                "codigo_categoria": codigo_categoria,
                "data_previsao": data_previsao,
                "id_conta_corrente": id_conta_corrente,

            }
        )

    def UpsertContaReceberPorLote(
            self, lote, conta_receber_cadastro
    ) -> dict:
        """Efetua o UPSERT do Contas a Receber por Lote."""
        return self._chamar_api(
            call='UpsertContaReceberPorLote',
            endpoint='financas/contareceber/',
            param={
                "lote": lote,
                "conta_receber_cadastro": conta_receber_cadastro,

            }
        )

    def CancelarBoleto(
            self, nCodTitulo, cCodIntTitulo
    ) -> dict:
        """Cancela o Boleto."""
        return self._chamar_api(
            call='CancelarBoleto',
            endpoint='financas/contareceberboleto/',
            param={
                "nCodTitulo": nCodTitulo,
                "cCodIntTitulo": cCodIntTitulo,

            }
        )

    def GerarBoleto(
            self, nCodTitulo, cCodIntTitulo
    ) -> dict:
        """Gera um Boleto referente a um Contas a Receber."""
        return self._chamar_api(
            call='GerarBoleto',
            endpoint='financas/contareceberboleto/',
            param={
                "nCodTitulo": nCodTitulo,
                "cCodIntTitulo": cCodIntTitulo,

            }
        )

    def ObterBoleto(
            self, nCodTitulo, cCodIntTitulo
    ) -> dict:
        """Disponibiliza o link de Download do Boleto."""
        return self._chamar_api(
            call='ObterBoleto',
            endpoint='financas/contareceberboleto/',
            param={
                "nCodTitulo": nCodTitulo,
                "cCodIntTitulo": cCodIntTitulo,

            }
        )

    def ProrrogarBoleto(
            self, nCodTitulo, cCodIntTitulo, dDtVenc
    ) -> dict:
        """Prorroga o vencimento do Boleto."""
        return self._chamar_api(
            call='ProrrogarBoleto',
            endpoint='financas/contareceberboleto/',
            param={
                "nCodTitulo": nCodTitulo,
                "cCodIntTitulo": cCodIntTitulo,
                "dDtVenc": dDtVenc,

            }
        )

    def ListarExtrato(
            self, nCodCC, cCodIntCC, dPeriodoInicial, dPeriodoFinal
    ) -> dict:
        """Listagem do Extrato"""
        return self._chamar_api(
            call='ListarExtrato',
            endpoint='financas/extrato/',
            param={
                "nCodCC": nCodCC,
                "cCodIntCC": cCodIntCC,
                "dPeriodoInicial": dPeriodoInicial,
                "dPeriodoFinal": dPeriodoFinal,

            }
        )

    def ListarOrcamentos(
            self, nAno, nMes
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarOrcamentos',
            endpoint='financas/caixa/',
            param={
                "nAno": nAno,
                "nMes": nMes,

            }
        )

    def ObterURLBoleto(
            self, nCodTitulo, cCodIntTitulo
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='ObterURLBoleto',
            endpoint='financas/pesquisartitulos/',
            param={
                "nCodTitulo": nCodTitulo,
                "cCodIntTitulo": cCodIntTitulo,

            }
        )

    def PesquisarExcluidos(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='PesquisarExcluidos',
            endpoint='financas/pesquisartitulos/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def PesquisarLancamentos(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='PesquisarLancamentos',
            endpoint='financas/pesquisartitulos/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def ObterResumoContador(
            self, dDataInicio, dDataFim
    ) -> dict:
        """Obtem o resumo do painel do contador."""
        return self._chamar_api(
            call='ObterResumoContador',
            endpoint='contador/resumo/',
            param={
                "dDataInicio": dDataInicio,
                "dDataFim": dDataFim,

            }
        )

    def ConsultarBanco(
            self, codigo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarBanco',
            endpoint='geral/bancos/',
            param={
                "codigo": codigo,

            }
        )

    def ListarBancos(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Exibe uma lista com os banco cadastrados."""
        return self._chamar_api(
            call='ListarBancos',
            endpoint='geral/bancos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ConsultarTipoDocumento(
            self, codigo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarTipoDocumento',
            endpoint='geral/tiposdoc/',
            param={
                "codigo": codigo,

            }
        )

    def PesquisarTipoDocumento(
            self, codigo
    ) -> dict:
        """Pesquisa o tipo de documento"""
        return self._chamar_api(
            call='PesquisarTipoDocumento',
            endpoint='geral/tiposdoc/',
            param={
                "codigo": codigo,

            }
        )

    def ListarTiposCC(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar os tipos de contas correntes."""
        return self._chamar_api(
            call='ListarTiposCC',
            endpoint='geral/tipocc/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarCadastroDRE(
            self, apenasContasAtivas
    ) -> dict:
        """Lista as contas do DRE"""
        return self._chamar_api(
            call='ListarCadastroDRE',
            endpoint='geral/dre/',
            param={
                "apenasContasAtivas": apenasContasAtivas,

            }
        )

    def ConsultarFinalTransf(
            self, banco, codigo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarFinalTransf',
            endpoint='geral/finaltransf/',
            param={
                "banco": banco,
                "codigo": codigo,

            }
        )

    def ListarFinalTransf(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarFinalTransf',
            endpoint='geral/finaltransf/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def AlterarProduto(
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
                "unidade": unidade,

            }
        )

    def AssociarCodIntProduto(
            self, codigo_produto, codigo_produto_integracao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AssociarCodIntProduto',
            endpoint='geral/produtos/',
            param={
                "codigo_produto": codigo_produto,
                "codigo_produto_integracao": codigo_produto_integracao,

            }
        )

    def ConsultarProduto(
            self, codigo_produto, codigo_produto_integracao, codigo
    ) -> dict:
        """Consulta um produto."""
        return self._chamar_api(
            call='ConsultarProduto',
            endpoint='geral/produtos/',
            param={
                "codigo_produto": codigo_produto,
                "codigo_produto_integracao": codigo_produto_integracao,
                "codigo": codigo,

            }
        )

    def ExcluirProduto(
            self, codigo_produto, codigo_produto_integracao, codigo
    ) -> dict:
        """Exclui um produto"""
        return self._chamar_api(
            call='ExcluirProduto',
            endpoint='geral/produtos/',
            param={
                "codigo_produto": codigo_produto,
                "codigo_produto_integracao": codigo_produto_integracao,
                "codigo": codigo,

            }
        )

    def IncluirProduto(
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
                "unidade": unidade,

            }
        )

    def IncluirProdutosPorLote(
            self, lote, produto_servico_cadastro
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='IncluirProdutosPorLote',
            endpoint='geral/produtos/',
            param={
                "lote": lote,
                "produto_servico_cadastro": produto_servico_cadastro,

            }
        )

    def ListarProdutos(
            self, pagina, registros_por_pagina, apenas_importado_api, filtrar_apenas_omiepdv
    ) -> dict:
        """Lista completa do cadastro de produtos"""
        return self._chamar_api(
            call='ListarProdutos',
            endpoint='geral/produtos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,
                "filtrar_apenas_omiepdv": filtrar_apenas_omiepdv,

            }
        )

    def ListarProdutosResumido(
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
                "filtrar_apenas_omiepdv": filtrar_apenas_omiepdv,

            }
        )

    def UpsertProduto(
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
                "unidade": unidade,

            }
        )

    def UpsertProdutosPorLote(
            self, lote, produto_servico_cadastro
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='UpsertProdutosPorLote',
            endpoint='geral/produtos/',
            param={
                "lote": lote,
                "produto_servico_cadastro": produto_servico_cadastro,

            }
        )

    def AlterarCaractProduto(
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
                "cExibirOrdemProd": cExibirOrdemProd,

            }
        )

    def ConsultarCaractProduto(
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
                "cCodIntCaract": cCodIntCaract,

            }
        )

    def ExcluirCaractProduto(
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
                "cCodIntCaract": cCodIntCaract,

            }
        )

    def IncluirCaractProduto(
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
                "cExibirOrdemProd": cExibirOrdemProd,

            }
        )

    def ListarCaractProduto(
            self, nPagina, nRegPorPagina, nCodProd
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarCaractProduto',
            endpoint='geral/prodcaract/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,
                "nCodProd": nCodProd,

            }
        )

    def AlterarEstrutura(
            self, idProduto, intProduto, itemMalhaAlterar
    ) -> dict:
        """Alterar a estrutura de um produto."""
        return self._chamar_api(
            call='AlterarEstrutura',
            endpoint='geral/malha/',
            param={
                "idProduto": idProduto,
                "intProduto": intProduto,
                "itemMalhaAlterar": itemMalhaAlterar,

            }
        )

    def ConsultarEstrutura(
            self, idProduto, intProduto, codProduto
    ) -> dict:
        """Consulta a estrutura do produto."""
        return self._chamar_api(
            call='ConsultarEstrutura',
            endpoint='geral/malha/',
            param={
                "idProduto": idProduto,
                "intProduto": intProduto,
                "codProduto": codProduto,

            }
        )

    def ExcluirEstrutura(
            self, idProduto, intProduto, idMalha, intMalha
    ) -> dict:
        """Excluir item da estrutura de um produto."""
        return self._chamar_api(
            call='ExcluirEstrutura',
            endpoint='geral/malha/',
            param={
                "idProduto": idProduto,
                "intProduto": intProduto,
                "idMalha": idMalha,
                "intMalha": intMalha,

            }
        )

    def IncluirEstrutura(
            self, idProduto, intProduto, itemMalhaIncluir
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirEstrutura',
            endpoint='geral/malha/',
            param={
                "idProduto": idProduto,
                "intProduto": intProduto,
                "itemMalhaIncluir": itemMalhaIncluir,

            }
        )

    def ListarEstruturas(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """Lista as estruturas de produtos."""
        return self._chamar_api(
            call='ListarEstruturas',
            endpoint='geral/malha/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def AlterarComponentesKit(
            self, codigo_produto, componentes_kit
    ) -> dict:
        """Inclui/Altera/Exclui os componentes do KIT."""
        return self._chamar_api(
            call='AlterarComponentesKit',
            endpoint='geral/produtoskit/',
            param={
                "codigo_produto": codigo_produto,
                "componentes_kit": componentes_kit,

            }
        )

    def AlterarReq(
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
                "ItensReqCompra": ItensReqCompra,

            }
        )

    def ConsultarReq(
            self, codIntReqCompra, codReqCompra
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarReq',
            endpoint='produtos/requisicaocompra/',
            param={
                "codIntReqCompra": codIntReqCompra,
                "codReqCompra": codReqCompra,

            }
        )

    def ExcluirReq(
            self, codIntReqCompra, codReqCompra
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirReq',
            endpoint='produtos/requisicaocompra/',
            param={
                "codIntReqCompra": codIntReqCompra,
                "codReqCompra": codReqCompra,

            }
        )

    def IncluirReq(
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
                "ItensReqCompra": ItensReqCompra,

            }
        )

    def PesquisarReq(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='PesquisarReq',
            endpoint='produtos/requisicaocompra/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def UpsertReq(
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
                "ItensReqCompra": ItensReqCompra,

            }
        )

    def AlteraPedCompra(
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
                "produtos_alterar": produtos_alterar,

            }
        )

    def ConsultarPedCompra(
            self, nCodPed, cCodIntPed, cNumero
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarPedCompra',
            endpoint='produtos/pedidocompra/',
            param={
                "nCodPed": nCodPed,
                "cCodIntPed": cCodIntPed,
                "cNumero": cNumero,

            }
        )

    def ExcluirPedCompra(
            self, nCodPed, cCodIntPed
    ) -> dict:
        """Excluir um Pedido de Compra"""
        return self._chamar_api(
            call='ExcluirPedCompra',
            endpoint='produtos/pedidocompra/',
            param={
                "nCodPed": nCodPed,
                "cCodIntPed": cCodIntPed,

            }
        )

    def IncluirPedCompra(
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
                "produtos_incluir": produtos_incluir,

            }
        )

    def PesquisarPedCompra(
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
                "lApenasAlterados": lApenasAlterados,

            }
        )

    def UpsertPedCompra(
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
                "produtos_upsert": produtos_upsert,

            }
        )

    def AlterarOrdemProducao(
            self, identificacao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarOrdemProducao',
            endpoint='produtos/op/',
            param={
                "identificacao": identificacao,

            }
        )

    def ConcluirOrdemProducao(
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
                "cObsConclusao": cObsConclusao,

            }
        )

    def ConsultarOrdemProducao(
            self, cCodIntOP, nCodOP
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarOrdemProducao',
            endpoint='produtos/op/',
            param={
                "cCodIntOP": cCodIntOP,
                "nCodOP": nCodOP,

            }
        )

    def ExcluirOrdemProducao(
            self, cCodIntOP, nCodOP
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirOrdemProducao',
            endpoint='produtos/op/',
            param={
                "cCodIntOP": cCodIntOP,
                "nCodOP": nCodOP,

            }
        )

    def IncluirOrdemProducao(
            self, identificacao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirOrdemProducao',
            endpoint='produtos/op/',
            param={
                "identificacao": identificacao,

            }
        )

    def ListarOrdemProducao(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarOrdemProducao',
            endpoint='produtos/op/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ReverterOrdemProducao(
            self, cCodIntOP, nCodOP
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ReverterOrdemProducao',
            endpoint='produtos/op/',
            param={
                "cCodIntOP": cCodIntOP,
                "nCodOP": nCodOP,

            }
        )

    def UpsertOrdemProducao(
            self, identificacao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='UpsertOrdemProducao',
            endpoint='produtos/op/',
            param={
                "identificacao": identificacao,

            }
        )

    def AlterarNotaEnt(
            self, cabec, infAdic, produtos
    ) -> dict:
        """Alterar nota de entrada"""
        return self._chamar_api(
            call='AlterarNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "cabec": cabec,
                "infAdic": infAdic,
                "produtos": produtos,

            }
        )

    def ConsultarNotaEnt(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Consultar nota de entrada"""
        return self._chamar_api(
            call='ConsultarNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt,

            }
        )

    def ExcluirNotaEnt(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Excluir nota de entrada"""
        return self._chamar_api(
            call='ExcluirNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt,

            }
        )

    def IncluirNotaEnt(
            self, cabec, infAdic, produtos
    ) -> dict:
        """Incluir nota de entrada"""
        return self._chamar_api(
            call='IncluirNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "cabec": cabec,
                "infAdic": infAdic,
                "produtos": produtos,

            }
        )

    def ListarNotaEnt(
            self, nPagina, nRegistrosPorPagina
    ) -> dict:
        """Listagem de nota de entrada"""
        return self._chamar_api(
            call='ListarNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "nPagina": nPagina,
                "nRegistrosPorPagina": nRegistrosPorPagina,

            }
        )

    def StatusNotaEnt(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Status de nota de entrada"""
        return self._chamar_api(
            call='StatusNotaEnt',
            endpoint='produtos/notaentrada/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt,

            }
        )

    def CancelarNotaEnt(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Cancelar nota de entrada"""
        return self._chamar_api(
            call='CancelarNotaEnt',
            endpoint='produtos/notaentradafat/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt,

            }
        )

    def ConcluirNotaEnt(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Concluir nota de entrada"""
        return self._chamar_api(
            call='ConcluirNotaEnt',
            endpoint='produtos/notaentradafat/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt,

            }
        )

    def ConferirNotaEnt(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Conferir nota de entrada"""
        return self._chamar_api(
            call='ConferirNotaEnt',
            endpoint='produtos/notaentradafat/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt,

            }
        )

    def DuplicarNotaEnt(
            self, nCodNotaEnt, cCodIntNotaEnt
    ) -> dict:
        """Duplicar nota de entrada"""
        return self._chamar_api(
            call='DuplicarNotaEnt',
            endpoint='produtos/notaentradafat/',
            param={
                "nCodNotaEnt": nCodNotaEnt,
                "cCodIntNotaEnt": cCodIntNotaEnt,

            }
        )

    def AlterarEtapaRecebimento(
            self, nIdReceb, cChaveNfe, cEtapa
    ) -> dict:
        """Alterar etapa recebimento NFe"""
        return self._chamar_api(
            call='AlterarEtapaRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "nIdReceb": nIdReceb,
                "cChaveNfe": cChaveNfe,
                "cEtapa": cEtapa,

            }
        )

    def AlterarRecebimento(
            self, ide, itensRecebimentoEditar
    ) -> dict:
        """Alterar recebimento de NFe"""
        return self._chamar_api(
            call='AlterarRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "ide": ide,
                "itensRecebimentoEditar": itensRecebimentoEditar,

            }
        )

    def ConcluirRecebimento(
            self, nIdReceb, cChaveNfe, cEtapa
    ) -> dict:
        """Concluir recebimento de NFe"""
        return self._chamar_api(
            call='ConcluirRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "nIdReceb": nIdReceb,
                "cChaveNfe": cChaveNfe,
                "cEtapa": cEtapa,

            }
        )

    def ConsultarRecebimento(
            self, nIdReceb, cChaveNfe
    ) -> dict:
        """Consultar recebimento de NFe"""
        return self._chamar_api(
            call='ConsultarRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "nIdReceb": nIdReceb,
                "cChaveNfe": cChaveNfe,

            }
        )

    def ListarRecebimentos(
            self, nPagina, nRegistrosPorPagina
    ) -> dict:
        """Listar recebimento de NFe"""
        return self._chamar_api(
            call='ListarRecebimentos',
            endpoint='produtos/recebimentonfe/',
            param={
                "nPagina": nPagina,
                "nRegistrosPorPagina": nRegistrosPorPagina,

            }
        )

    def ReverterRecebimento(
            self, nIdReceb, cChaveNfe, cEtapa
    ) -> dict:
        """Reverter recebimento NFe"""
        return self._chamar_api(
            call='ReverterRecebimento',
            endpoint='produtos/recebimentonfe/',
            param={
                "nIdReceb": nIdReceb,
                "cChaveNfe": cChaveNfe,
                "cEtapa": cEtapa,

            }
        )

    def AlterarFamilia(
            self, codigo, codInt, codFamilia, nomeFamilia, inativo
    ) -> dict:
        """Altera uma familia de produto"""
        return self._chamar_api(
            call='AlterarFamilia',
            endpoint='geral/familias/',
            param={
                "codigo": codigo,
                "codInt": codInt,
                "codFamilia": codFamilia,
                "nomeFamilia": nomeFamilia,
                "inativo": inativo,

            }
        )

    def ConsultarFamilia(
            self, codigo, codInt
    ) -> dict:
        """Consulta uma familia de produto"""
        return self._chamar_api(
            call='ConsultarFamilia',
            endpoint='geral/familias/',
            param={
                "codigo": codigo,
                "codInt": codInt,

            }
        )

    def ExcluirFamilia(
            self, codigo, codInt
    ) -> dict:
        """Exclui uma familia de produto"""
        return self._chamar_api(
            call='ExcluirFamilia',
            endpoint='geral/familias/',
            param={
                "codigo": codigo,
                "codInt": codInt,

            }
        )

    def IncluirFamilia(
            self, codInt, codFamilia, nomeFamilia, inativo
    ) -> dict:
        """Inclui uma familia de produto"""
        return self._chamar_api(
            call='IncluirFamilia',
            endpoint='geral/familias/',
            param={
                "codInt": codInt,
                "codFamilia": codFamilia,
                "nomeFamilia": nomeFamilia,
                "inativo": inativo,

            }
        )

    def PesquisarFamilias(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listagem de familias cadastradas"""
        return self._chamar_api(
            call='PesquisarFamilias',
            endpoint='geral/familias/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def UpsertFamilia(
            self, codigo, codInt, codFamilia, nomeFamilia, inativo
    ) -> dict:
        """Inclui / Altera uma familia de produto"""
        return self._chamar_api(
            call='UpsertFamilia',
            endpoint='geral/familias/',
            param={
                "codigo": codigo,
                "codInt": codInt,
                "codFamilia": codFamilia,
                "nomeFamilia": nomeFamilia,
                "inativo": inativo,

            }
        )

    def ListarUnidades(
            self, codigo
    ) -> dict:
        """Lista as unidades de medidas"""
        return self._chamar_api(
            call='ListarUnidades',
            endpoint='geral/unidade/',
            param={
                "codigo": codigo,

            }
        )

    def ListarCompradores(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista os compradores cadastrados."""
        return self._chamar_api(
            call='ListarCompradores',
            endpoint='estoque/comprador/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarProdutoFornecedor(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar os produtos por fornecedores."""
        return self._chamar_api(
            call='ListarProdutoFornecedor',
            endpoint='estoque/produtofornecedor/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarFormasPagVendas(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista as formas de pagmento de vendas."""
        return self._chamar_api(
            call='ListarFormasPagVendas',
            endpoint='produtos/formaspagvendas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ConsultarNCM(
            self, cCodigo
    ) -> dict:
        """Consulta um NCM"""
        return self._chamar_api(
            call='ConsultarNCM',
            endpoint='produtos/ncm/',
            param={
                "cCodigo": cCodigo,

            }
        )

    def ListarNCM(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """Lista os NCMs cadastrados."""
        return self._chamar_api(
            call='ListarNCM',
            endpoint='produtos/ncm/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def ListarCenarios(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarCenarios',
            endpoint='geral/cenarios/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def ListarImpostosCenario(
            self, codigo_cliente_integracao, consumo_final, codigo_produto_integracao, codigo_cenario
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarImpostosCenario',
            endpoint='geral/cenarios/',
            param={
                "codigo_cliente_integracao": codigo_cliente_integracao,
                "consumo_final": consumo_final,
                "codigo_produto_integracao": codigo_produto_integracao,
                "codigo_cenario": codigo_cenario,

            }
        )

    def ListarCFOP(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar as CFOPs"""
        return self._chamar_api(
            call='ListarCFOP',
            endpoint='produtos/cfop/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarCST(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar os CSTs do ICMS"""
        return self._chamar_api(
            call='ListarCST',
            endpoint='produtos/icmscst/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarCSOSN(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar os CSOSN do ICMS."""
        return self._chamar_api(
            call='ListarCSOSN',
            endpoint='produtos/icmscsosn/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarOrigMerc(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar a origem da mercadoria do ICMS."""
        return self._chamar_api(
            call='ListarOrigMerc',
            endpoint='produtos/icmsorigem/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarCstPis(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar o CST do PIS."""
        return self._chamar_api(
            call='ListarCstPis',
            endpoint='produtos/piscst/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarCstCofins(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar CST do COFINS."""
        return self._chamar_api(
            call='ListarCstCofins',
            endpoint='produtos/cofinscst/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarCstIpi(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar CST do IPI."""
        return self._chamar_api(
            call='ListarCstIpi',
            endpoint='produtos/ipicst/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarEnqIpi(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar Enquadramento do IPI."""
        return self._chamar_api(
            call='ListarEnqIpi',
            endpoint='produtos/ipienq/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarTpCalc(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarTpCalc',
            endpoint='produtos/tpcalc/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarCEST(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar CEST."""
        return self._chamar_api(
            call='ListarCEST',
            endpoint='produtos/cest/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def AlterarEstoqueMinimo(
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
                "quan_min": quan_min,

            }
        )

    def ExcluirAjusteEstoque(
            self, id_ajuste
    ) -> dict:
        """Excluir um Movimento de Ajuste de Estoque"""
        return self._chamar_api(
            call='ExcluirAjusteEstoque',
            endpoint='estoque/ajuste/',
            param={
                "id_ajuste": id_ajuste,

            }
        )

    def IncluirAjusteEstoque(
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
                "valor": valor,

            }
        )

    def ListarAjusteEstoque(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Listar os ajuste de estoque."""
        return self._chamar_api(
            call='ListarAjusteEstoque',
            endpoint='estoque/ajuste/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def ListarMovimentoEstoque(
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
                "lista_local_estoque": lista_local_estoque,

            }
        )

    def ListarPosEstoque(
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
                "codigo_local_estoque": codigo_local_estoque,

            }
        )

    def ListarSaldoPendente(
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
                "tipo": tipo,

            }
        )

    def MovimentoEstoque(
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
                "dataFinal": dataFinal,

            }
        )

    def PosicaoEstoque(
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
                "data": data,

            }
        )

    def ConsultarPrevisao(
            self, nCodProd
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarPrevisao',
            endpoint='estoque/movestoque/',
            param={
                "nCodProd": nCodProd,

            }
        )

    def ListarMovimentos(
            self, pagina, registros_por_pagina, codigo_local_estoque
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarMovimentos',
            endpoint='estoque/movestoque/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "codigo_local_estoque": codigo_local_estoque,

            }
        )

    def ListarLocaisEstoque(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """Lista os Locais de Estoque encontrados."""
        return self._chamar_api(
            call='ListarLocaisEstoque',
            endpoint='estoque/local/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def ObterEstoqueProduto(
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
                "dDia": dDia,

            }
        )

    def AlterarPedFaturado(
            self, codigo_pedido, codigo_pedido_integracao, codigo_rastreio, previsao_entrega, obs_venda
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarPedFaturado',
            endpoint='produtos/pedido/',
            param={
                "codigo_pedido": codigo_pedido,
                "codigo_pedido_integracao": codigo_pedido_integracao,
                "codigo_rastreio": codigo_rastreio,
                "previsao_entrega": previsao_entrega,
                "obs_venda": obs_venda,

            }
        )

    def AlterarPedidoVenda(
            self, cabecalho, det, informacoes_adicionais, lista_parcelas, total_pedido
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarPedidoVenda',
            endpoint='produtos/pedido/',
            param={
                "cabecalho": cabecalho,
                "det": det,
                "informacoes_adicionais": informacoes_adicionais,
                "lista_parcelas": lista_parcelas,
                "total_pedido": total_pedido,

            }
        )

    def ConsultarPedido(
            self, codigo_pedido
    ) -> dict:
        """Consulta de Pedido de Venda de Produto"""
        return self._chamar_api(
            call='ConsultarPedido',
            endpoint='produtos/pedido/',
            param={
                "codigo_pedido": codigo_pedido,

            }
        )

    def ExcluirPedido(
            self, codigo_pedido, codigo_pedido_integracao
    ) -> dict:
        """Excluir pedido de venda de produto"""
        return self._chamar_api(
            call='ExcluirPedido',
            endpoint='produtos/pedido/',
            param={
                "codigo_pedido": codigo_pedido,
                "codigo_pedido_integracao": codigo_pedido_integracao,

            }
        )

    def IncluirPedido(
            self, cabecalho, det, frete, informacoes_adicionais, lista_parcelas
    ) -> dict:
        """Inclui um pedido de venda de produto"""
        return self._chamar_api(
            call='IncluirPedido',
            endpoint='produtos/pedido/',
            param={
                "cabecalho": cabecalho,
                "det": det,
                "frete": frete,
                "informacoes_adicionais": informacoes_adicionais,
                "lista_parcelas": lista_parcelas,

            }
        )

    def ListarPedidos(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Listar os pedidos de venda de produto"""
        return self._chamar_api(
            call='ListarPedidos',
            endpoint='produtos/pedido/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def SimularImpostos(
            self, codigo_cliente, consumidor_final, frete_simul, det_simul
    ) -> dict:
        """Simula os impostos de um pedido de venda."""
        return self._chamar_api(
            call='SimularImpostos',
            endpoint='produtos/pedido/',
            param={
                "codigo_cliente": codigo_cliente,
                "consumidor_final": consumidor_final,
                "frete_simul": frete_simul,
                "det_simul": det_simul,

            }
        )

    def StatusPedido(
            self, codigo_pedido, codigo_pedido_integracao
    ) -> dict:
        """Consulta do Status do Pedido"""
        return self._chamar_api(
            call='StatusPedido',
            endpoint='produtos/pedido/',
            param={
                "codigo_pedido": codigo_pedido,
                "codigo_pedido_integracao": codigo_pedido_integracao,

            }
        )

    def TrocarEtapaPedido(
            self, codigo_pedido, codigo_pedido_integracao, etapa
    ) -> dict:
        """Troca etapa do pedido."""
        return self._chamar_api(
            call='TrocarEtapaPedido',
            endpoint='produtos/pedido/',
            param={
                "codigo_pedido": codigo_pedido,
                "codigo_pedido_integracao": codigo_pedido_integracao,
                "etapa": etapa,

            }
        )

    def AssociarCodIntPedidoVenda(
            self, cCodIntPed, nCodPed
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AssociarCodIntPedidoVenda',
            endpoint='produtos/pedidovendafat/',
            param={
                "cCodIntPed": cCodIntPed,
                "nCodPed": nCodPed,

            }
        )

    def CancelarPedidoVenda(
            self, cCodIntPed, nCodPed
    ) -> dict:
        """Cancela um pedido de venda de produto."""
        return self._chamar_api(
            call='CancelarPedidoVenda',
            endpoint='produtos/pedidovendafat/',
            param={
                "cCodIntPed": cCodIntPed,
                "nCodPed": nCodPed,

            }
        )

    def DuplicarPedidoVenda(
            self, cCodIntPed, nCodPed
    ) -> dict:
        """Duplica um pedido de venda de produto."""
        return self._chamar_api(
            call='DuplicarPedidoVenda',
            endpoint='produtos/pedidovendafat/',
            param={
                "cCodIntPed": cCodIntPed,
                "nCodPed": nCodPed,

            }
        )

    def FaturarPedidoVenda(
            self, cCodIntPed, nCodPed
    ) -> dict:
        """Fatura um pedido de venda de produto."""
        return self._chamar_api(
            call='FaturarPedidoVenda',
            endpoint='produtos/pedidovendafat/',
            param={
                "cCodIntPed": cCodIntPed,
                "nCodPed": nCodPed,

            }
        )

    def ObterPedidosVenda(
            self, cEtapa
    ) -> dict:
        """Retorna a lista de pedidos de venda a serem faturados."""
        return self._chamar_api(
            call='ObterPedidosVenda',
            endpoint='produtos/pedidovendafat/',
            param={
                "cEtapa": cEtapa,

            }
        )

    def ValidarPedidoVenda(
            self, cCodIntPed, nCodPed
    ) -> dict:
        """Valida um pedido de venda de produto para faturamento."""
        return self._chamar_api(
            call='ValidarPedidoVenda',
            endpoint='produtos/pedidovendafat/',
            param={
                "cCodIntPed": cCodIntPed,
                "nCodPed": nCodPed,

            }
        )

    def ListarEtapasPedido(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """Lista as etapas do Pedido de Venda de Produtos."""
        return self._chamar_api(
            call='ListarEtapasPedido',
            endpoint='produtos/pedidoetapas/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def AverbacaoCTe(
            self, cAppNome, cAppVersao, cAppId, cChaveCte, cXmlCteAverb, cMd5CteAverb
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AverbacaoCTe',
            endpoint='produtos/cte/',
            param={
                "cAppNome": cAppNome,
                "cAppVersao": cAppVersao,
                "cAppId": cAppId,
                "cChaveCte": cChaveCte,
                "cXmlCteAverb": cXmlCteAverb,
                "cMd5CteAverb": cMd5CteAverb,

            }
        )

    def CancelarCTe(
            self, cAppNome, cAppVersao, cAppId, cChaveCte, cXmlCteCanc, cMd5CteCanc
    ) -> dict:
        """Cancela um CT-e."""
        return self._chamar_api(
            call='CancelarCTe',
            endpoint='produtos/cte/',
            param={
                "cAppNome": cAppNome,
                "cAppVersao": cAppVersao,
                "cAppId": cAppId,
                "cChaveCte": cChaveCte,
                "cXmlCteCanc": cXmlCteCanc,
                "cMd5CteCanc": cMd5CteCanc,

            }
        )

    def CartaCorrecaoCTe(
            self, cAppNome, cAppVersao, cAppId, cChaveCte, cXmlCteCC, cMd5CteCC
    ) -> dict:
        """"""
        return self._chamar_api(
            call='CartaCorrecaoCTe',
            endpoint='produtos/cte/',
            param={
                "cAppNome": cAppNome,
                "cAppVersao": cAppVersao,
                "cAppId": cAppId,
                "cChaveCte": cChaveCte,
                "cXmlCteCC": cXmlCteCC,
                "cMd5CteCC": cMd5CteCC,

            }
        )

    def ExcluirFaturaCTe(
            self, cAppNome, cAppVersao, cAppId, nIdFaturamento
    ) -> dict:
        """Exclui uma fatura de um grupo de CT-es."""
        return self._chamar_api(
            call='ExcluirFaturaCTe',
            endpoint='produtos/cte/',
            param={
                "cAppNome": cAppNome,
                "cAppVersao": cAppVersao,
                "cAppId": cAppId,
                "nIdFaturamento": nIdFaturamento,

            }
        )

    def FaturarCTe(
            self, cAppNome, cAppVersao, cAppId, CNPJCliente, cCategoria, nContaCorrente, dVencimento, nValorFatura,
            itensFatura
    ) -> dict:
        """Gera uma fatura para um grupo de CT-es."""
        return self._chamar_api(
            call='FaturarCTe',
            endpoint='produtos/cte/',
            param={
                "cAppNome": cAppNome,
                "cAppVersao": cAppVersao,
                "cAppId": cAppId,
                "CNPJCliente": CNPJCliente,
                "cCategoria": cCategoria,
                "nContaCorrente": nContaCorrente,
                "dVencimento": dVencimento,
                "nValorFatura": nValorFatura,
                "itensFatura": itensFatura,

            }
        )

    def FaturarLoteCTe(
            self, cAppNome, cAppVersao, cAppId, nIdFaturamento, CNPJCliente, cConcluirFatura, itensFatura
    ) -> dict:
        """Gera uma fatura por lote para um grupo de CT-es."""
        return self._chamar_api(
            call='FaturarLoteCTe',
            endpoint='produtos/cte/',
            param={
                "cAppNome": cAppNome,
                "cAppVersao": cAppVersao,
                "cAppId": cAppId,
                "nIdFaturamento": nIdFaturamento,
                "CNPJCliente": CNPJCliente,
                "cConcluirFatura": cConcluirFatura,
                "itensFatura": itensFatura,

            }
        )

    def ImportarCTe(
            self, cAppNome, cAppVersao, cAppId, cChaveCte, cXmlCte, cMd5Cte, cCategoria, nContaCorrente
    ) -> dict:
        """Importar o XML de um CT-e."""
        return self._chamar_api(
            call='ImportarCTe',
            endpoint='produtos/cte/',
            param={
                "cAppNome": cAppNome,
                "cAppVersao": cAppVersao,
                "cAppId": cAppId,
                "cChaveCte": cChaveCte,
                "cXmlCte": cXmlCte,
                "cMd5Cte": cMd5Cte,
                "cCategoria": cCategoria,
                "nContaCorrente": nContaCorrente,

            }
        )

    def ListarNFeTransp(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarNFeTransp',
            endpoint='produtos/cte/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def StatusFatura(
            self, cAppNome, cAppVersao, cAppId, nIdFaturamento
    ) -> dict:
        """Retorna o Status da Fatura inclusa."""
        return self._chamar_api(
            call='StatusFatura',
            endpoint='produtos/cte/',
            param={
                "cAppNome": cAppNome,
                "cAppVersao": cAppVersao,
                "cAppId": cAppId,
                "nIdFaturamento": nIdFaturamento,

            }
        )

    def AlterarRemessa(
            self, cabec, email, frete, infAdic, obs, produtos
    ) -> dict:
        """Altera uma remessa"""
        return self._chamar_api(
            call='AlterarRemessa',
            endpoint='produtos/remessa/',
            param={
                "cabec": cabec,
                "email": email,
                "frete": frete,
                "infAdic": infAdic,
                "obs": obs,
                "produtos": produtos,

            }
        )

    def ConsultarRemessa(
            self, nCodRem, cCodIntRem
    ) -> dict:
        """Consulta uma remessa."""
        return self._chamar_api(
            call='ConsultarRemessa',
            endpoint='produtos/remessa/',
            param={
                "nCodRem": nCodRem,
                "cCodIntRem": cCodIntRem,

            }
        )

    def IncluirRemessa(
            self, cabec, email, frete, infAdic, obs, produtos
    ) -> dict:
        """Inclui uma nova remessa"""
        return self._chamar_api(
            call='IncluirRemessa',
            endpoint='produtos/remessa/',
            param={
                "cabec": cabec,
                "email": email,
                "frete": frete,
                "infAdic": infAdic,
                "obs": obs,
                "produtos": produtos,

            }
        )

    def ListarRemessas(
            self, nPagina
    ) -> dict:
        """Lista as remessas cadastradas."""
        return self._chamar_api(
            call='ListarRemessas',
            endpoint='produtos/remessa/',
            param={
                "nPagina": nPagina,

            }
        )

    def StatusRemessa(
            self, nCodRem, cCodIntRem
    ) -> dict:
        """Retorna o status da remessa"""
        return self._chamar_api(
            call='StatusRemessa',
            endpoint='produtos/remessa/',
            param={
                "nCodRem": nCodRem,
                "cCodIntRem": cCodIntRem,

            }
        )

    def CancelarRemessa(
            self, nCodRem, cCodIntRem
    ) -> dict:
        """Cancelar remessa de produto"""
        return self._chamar_api(
            call='CancelarRemessa',
            endpoint='produtos/remessafat/',
            param={
                "nCodRem": nCodRem,
                "cCodIntRem": cCodIntRem,

            }
        )

    def ConcluirRemessa(
            self, nCodRem, cCodIntRem
    ) -> dict:
        """Concluir remessa de produto"""
        return self._chamar_api(
            call='ConcluirRemessa',
            endpoint='produtos/remessafat/',
            param={
                "nCodRem": nCodRem,
                "cCodIntRem": cCodIntRem,

            }
        )

    def ConferirRemessa(
            self, nCodRem, cCodIntRem
    ) -> dict:
        """Conferir remessa de produto"""
        return self._chamar_api(
            call='ConferirRemessa',
            endpoint='produtos/remessafat/',
            param={
                "nCodRem": nCodRem,
                "cCodIntRem": cCodIntRem,

            }
        )

    def DuplicarRemessa(
            self, nCodRem, cCodIntRem
    ) -> dict:
        """Duplicar remessa de produto"""
        return self._chamar_api(
            call='DuplicarRemessa',
            endpoint='produtos/remessafat/',
            param={
                "nCodRem": nCodRem,
                "cCodIntRem": cCodIntRem,

            }
        )

    def FecharCaixa(
            self, emissor, seqCaixa
    ) -> dict:
        """Efetua o fechamento de um determinado caixa."""
        return self._chamar_api(
            call='FecharCaixa',
            endpoint='produtos/cupomfiscalincluir/',
            param={
                "emissor": emissor,
                "seqCaixa": seqCaixa,

            }
        )

    def InutilizarNfce(
            self, emissor, nfceInut
    ) -> dict:
        """Inutiliza um lote de NFC-e."""
        return self._chamar_api(
            call='InutilizarNfce',
            endpoint='produtos/cupomfiscalincluir/',
            param={
                "emissor": emissor,
                "nfceInut": nfceInut,

            }
        )

    def CancelarCupom(
            self, nIdCupom
    ) -> dict:
        """Cancela um cupom Fiscal"""
        return self._chamar_api(
            call='CancelarCupom',
            endpoint='produtos/cupomfiscal/',
            param={
                "nIdCupom": nIdCupom,

            }
        )

    def CancelarNFCE(
            self, nCodigoPDV, nNumeroCaixa, cDataEmissao, IdenticacaoNFCE, DadosCancNFCE
    ) -> dict:
        """Cancelar NFC-e."""
        return self._chamar_api(
            call='CancelarNFCE',
            endpoint='produtos/cupomfiscal/',
            param={
                "nCodigoPDV": nCodigoPDV,
                "nNumeroCaixa": nNumeroCaixa,
                "cDataEmissao": cDataEmissao,
                "IdenticacaoNFCE": IdenticacaoNFCE,
                "DadosCancNFCE": DadosCancNFCE,

            }
        )

    def CancelarSAT(
            self, nCodigoPDV, nNumeroCaixa, cDataEmissao, IdenticacaoSAT, DadosCancSAT
    ) -> dict:
        """Cancelar CF-e-SAT."""
        return self._chamar_api(
            call='CancelarSAT',
            endpoint='produtos/cupomfiscal/',
            param={
                "nCodigoPDV": nCodigoPDV,
                "nNumeroCaixa": nNumeroCaixa,
                "cDataEmissao": cDataEmissao,
                "IdenticacaoSAT": IdenticacaoSAT,
                "DadosCancSAT": DadosCancSAT,

            }
        )

    def ExcluirCupom(
            self, nIdCupom
    ) -> dict:
        """Exclui um Cupom Fiscal."""
        return self._chamar_api(
            call='ExcluirCupom',
            endpoint='produtos/cupomfiscal/',
            param={
                "nIdCupom": nIdCupom,

            }
        )

    def ExcluirCuponsPorNumero(
            self, nCodigoPDV, nNumeroCaixa, cDataEmissao, nNumCupom
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirCuponsPorNumero',
            endpoint='produtos/cupomfiscal/',
            param={
                "nCodigoPDV": nCodigoPDV,
                "nNumeroCaixa": nNumeroCaixa,
                "cDataEmissao": cDataEmissao,
                "nNumCupom": nNumCupom,

            }
        )

    def ExcluirLote(
            self, nNumLote
    ) -> dict:
        """Excluir o lote"""
        return self._chamar_api(
            call='ExcluirLote',
            endpoint='produtos/cupomfiscal/',
            param={
                "nNumLote": nNumLote,

            }
        )

    def ListarCupons(
            self, nPagina, nRegPorPagina, dDtEmisInicial, dDtEmisFinal
    ) -> dict:
        """Lista os Cupons Fiscais."""
        return self._chamar_api(
            call='ListarCupons',
            endpoint='produtos/cupomfiscal/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,
                "dDtEmisInicial": dDtEmisInicial,
                "dDtEmisFinal": dDtEmisFinal,

            }
        )

    def ObterProximoLote(
            self, nCodigoPDV
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ObterProximoLote',
            endpoint='produtos/cupomfiscal/',
            param={
                "nCodigoPDV": nCodigoPDV,

            }
        )

    def CuponsFiscais(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """Listagem dos cupons fiscais."""
        return self._chamar_api(
            call='CuponsFiscais',
            endpoint='produtos/cupomfiscalconsultar/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def CuponsItens(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """Listagem dos itens dos cupons fiscais"""
        return self._chamar_api(
            call='CuponsItens',
            endpoint='produtos/cupomfiscalconsultar/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def CuponsPagamentos(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """Listagem dos pagamentos dos cupons fiscais"""
        return self._chamar_api(
            call='CuponsPagamentos',
            endpoint='produtos/cupomfiscalconsultar/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def ImportarNFCe(
            self, emiNome, emiVersao, emiId, chNFe, nfceXml, nfceMd5, cAcaoCliente, idCliente, idVendedor, idProjeto,
            idLocalEstoque, cNaoMovEstoque, cNaoGerarTitulo, cIncluirProduto
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ImportarNFCe',
            endpoint='produtos/nfce/',
            param={
                "emiNome": emiNome,
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
                "cIncluirProduto": cIncluirProduto,

            }
        )

    def ImportarCfeSat(
            self, emiNome, emiVersao, emiId, chNFe, satXml, satMd5, cAcaoCliente, idCliente, idVendedor, idProjeto,
            idLocalEstoque, cNaoMovEstoque, cNaoGerarTitulo, cIncluirProduto
    ) -> dict:
        """Importa o XML de um CF-e SAT."""
        return self._chamar_api(
            call='ImportarCfeSat',
            endpoint='produtos/sat/',
            param={
                "emiNome": emiNome,
                "emiVersao": emiVersao,
                "emiId": emiId,
                "chNFe": chNFe,
                "satXml": satXml,
                "satMd5": satMd5,
                "cAcaoCliente": cAcaoCliente,
                "idCliente": idCliente,
                "idVendedor": idVendedor,
                "idProjeto": idProjeto,
                "idLocalEstoque": idLocalEstoque,
                "cNaoMovEstoque": cNaoMovEstoque,
                "cNaoGerarTitulo": cNaoGerarTitulo,
                "cIncluirProduto": cIncluirProduto,

            }
        )

    def AlterarPrecoItem(
            self, nCodTabPreco, nCodProd, nValorTabela
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarPrecoItem',
            endpoint='produtos/tabelaprecos/',
            param={
                "nCodTabPreco": nCodTabPreco,
                "nCodProd": nCodProd,
                "nValorTabela": nValorTabela,

            }
        )

    def AlterarTabelaPreco(
            self, nCodTabPreco, cCodIntTabPreco, cNome, cCodigo, cOrigem, produtos, clientes, outrasInfo,
            caracteristicas
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarTabelaPreco',
            endpoint='produtos/tabelaprecos/',
            param={
                "nCodTabPreco": nCodTabPreco,
                "cCodIntTabPreco": cCodIntTabPreco,
                "cNome": cNome,
                "cCodigo": cCodigo,
                "cOrigem": cOrigem,
                "produtos": produtos,
                "clientes": clientes,
                "outrasInfo": outrasInfo,
                "caracteristicas": caracteristicas,

            }
        )

    def AtivarTabelaPreco(
            self, nCodTabPreco, cCodIntTabPreco
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AtivarTabelaPreco',
            endpoint='produtos/tabelaprecos/',
            param={
                "nCodTabPreco": nCodTabPreco,
                "cCodIntTabPreco": cCodIntTabPreco,

            }
        )

    def AtualizarProdutos(
            self, nCodTabPreco, cCodIntTabPreco
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AtualizarProdutos',
            endpoint='produtos/tabelaprecos/',
            param={
                "nCodTabPreco": nCodTabPreco,
                "cCodIntTabPreco": cCodIntTabPreco,

            }
        )

    def ConsultarTabelaPreco(
            self, nCodTabPreco, cCodIntTabPreco
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarTabelaPreco',
            endpoint='produtos/tabelaprecos/',
            param={
                "nCodTabPreco": nCodTabPreco,
                "cCodIntTabPreco": cCodIntTabPreco,

            }
        )

    def ExcluirTabelaPreco(
            self, nCodTabPreco, cCodIntTabPreco
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirTabelaPreco',
            endpoint='produtos/tabelaprecos/',
            param={
                "nCodTabPreco": nCodTabPreco,
                "cCodIntTabPreco": cCodIntTabPreco,

            }
        )

    def IncluirTabelaPreco(
            self, cCodIntTabPreco, cNome, cCodigo, cOrigem, produtos, clientes, outrasInfo, caracteristicas
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirTabelaPreco',
            endpoint='produtos/tabelaprecos/',
            param={
                "cCodIntTabPreco": cCodIntTabPreco,
                "cNome": cNome,
                "cCodigo": cCodigo,
                "cOrigem": cOrigem,
                "produtos": produtos,
                "clientes": clientes,
                "outrasInfo": outrasInfo,
                "caracteristicas": caracteristicas,

            }
        )

    def ListarTabelaItens(
            self, nPagina, nRegPorPagina, nCodTabPreco, cCodIntTabPreco
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarTabelaItens',
            endpoint='produtos/tabelaprecos/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,
                "nCodTabPreco": nCodTabPreco,
                "cCodIntTabPreco": cCodIntTabPreco,

            }
        )

    def ListarTabelasPreco(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarTabelasPreco',
            endpoint='produtos/tabelaprecos/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def SuspenderTabelaPreco(
            self, nCodTabPreco, cCodIntTabPreco
    ) -> dict:
        """"""
        return self._chamar_api(
            call='SuspenderTabelaPreco',
            endpoint='produtos/tabelaprecos/',
            param={
                "nCodTabPreco": nCodTabPreco,
                "cCodIntTabPreco": cCodIntTabPreco,

            }
        )

    def AlterarCaracteristica(
            self, nCodCaract, cCodIntCaract, cNomeCaract
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarCaracteristica',
            endpoint='geral/caracteristicas/',
            param={
                "nCodCaract": nCodCaract,
                "cCodIntCaract": cCodIntCaract,
                "cNomeCaract": cNomeCaract,

            }
        )

    def ConsultarCaracteristica(
            self, nCodCaract, cCodIntCaract
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarCaracteristica',
            endpoint='geral/caracteristicas/',
            param={
                "nCodCaract": nCodCaract,
                "cCodIntCaract": cCodIntCaract,

            }
        )

    def ExcluirCaracteristica(
            self, nCodCaract, cCodIntCaract
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirCaracteristica',
            endpoint='geral/caracteristicas/',
            param={
                "nCodCaract": nCodCaract,
                "cCodIntCaract": cCodIntCaract,

            }
        )

    def IncluirCaracteristica(
            self, cCodIntCaract, cNomeCaract
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirCaracteristica',
            endpoint='geral/caracteristicas/',
            param={
                "cCodIntCaract": cCodIntCaract,
                "cNomeCaract": cNomeCaract,

            }
        )

    def ListarCaracteristicas(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarCaracteristicas',
            endpoint='geral/caracteristicas/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def ListarEtapasFaturamento(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista as etapas do faturamento"""
        return self._chamar_api(
            call='ListarEtapasFaturamento',
            endpoint='produtos/etapafat/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarMeiosPagamento(
            self, codigo
    ) -> dict:
        """Listagem de meios de pagamento"""
        return self._chamar_api(
            call='ListarMeiosPagamento',
            endpoint='geral/meiospagamento/',
            param={
                "codigo": codigo,

            }
        )

    def ListarOrigem(
            self, codigo
    ) -> dict:
        """Lista Origem de pedidos."""
        return self._chamar_api(
            call='ListarOrigem',
            endpoint='geral/origempedido/',
            param={
                "codigo": codigo,

            }
        )

    def ListarNFSEs(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """Lista de NFS-es."""
        return self._chamar_api(
            call='ListarNFSEs',
            endpoint='servicos/nfse/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def GetUrlDanfe(
            self, nCodNF, cCodNFInt
    ) -> dict:
        """"""
        return self._chamar_api(
            call='GetUrlDanfe',
            endpoint='produtos/notafiscalutil/',
            param={
                "nCodNF": nCodNF,
                "cCodNFInt": cCodNFInt,

            }
        )

    def GetUrlLogo(
            self, nCodEmpr, cCodEmprInt
    ) -> dict:
        """Retorna a URL do Logotipo"""
        return self._chamar_api(
            call='GetUrlLogo',
            endpoint='produtos/notafiscalutil/',
            param={
                "nCodEmpr": nCodEmpr,
                "cCodEmprInt": cCodEmprInt,

            }
        )

    def GetUrlNotaFiscal(
            self, nCodNF, cCodNFInt
    ) -> dict:
        """Retorna a URL da Nota Fiscal"""
        return self._chamar_api(
            call='GetUrlNotaFiscal',
            endpoint='produtos/notafiscalutil/',
            param={
                "nCodNF": nCodNF,
                "cCodNFInt": cCodNFInt,

            }
        )

    def ExcluirNFe(
            self, cChaveNFe, nIdImportacao, nIdNFe
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirNFe',
            endpoint='produtos/nfe/',
            param={
                "cChaveNFe": cChaveNFe,
                "nIdImportacao": nIdImportacao,
                "nIdNFe": nIdNFe,

            }
        )

    def ImportarCancNFe(
            self, cAppNome, cAppVersao, cAppId, cChaveNFe, cXmlNFeCanc, cMd5NFeCanc
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ImportarCancNFe',
            endpoint='produtos/nfe/',
            param={
                "cAppNome": cAppNome,
                "cAppVersao": cAppVersao,
                "cAppId": cAppId,
                "cChaveNFe": cChaveNFe,
                "cXmlNFeCanc": cXmlNFeCanc,
                "cMd5NFeCanc": cMd5NFeCanc,

            }
        )

    def ListarNFe(
            self, nPagina, nRegPorPagina, dDataEmissaoInicial, dDataEmissaoFinal
    ) -> dict:
        """Lista as NFes importadas."""
        return self._chamar_api(
            call='ListarNFe',
            endpoint='produtos/nfe/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,
                "dDataEmissaoInicial": dDataEmissaoInicial,
                "dDataEmissaoFinal": dDataEmissaoFinal,

            }
        )

    def AssociarCodIntServico(
            self, nCodServ, cCodIntServ
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AssociarCodIntServico',
            endpoint='servicos/servico/',
            param={
                "nCodServ": nCodServ,
                "cCodIntServ": cCodIntServ,

            }
        )

    def ConsultarCadastroServico(
            self, cCodIntServ, nCodServ
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarCadastroServico',
            endpoint='servicos/servico/',
            param={
                "cCodIntServ": cCodIntServ,
                "nCodServ": nCodServ,

            }
        )

    def ExcluirCadastroServico(
            self, cCodIntServ, nCodServ
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirCadastroServico',
            endpoint='servicos/servico/',
            param={
                "cCodIntServ": cCodIntServ,
                "nCodServ": nCodServ,

            }
        )

    def ListarCadastroServico(
            self, nPagina, nRegPorPagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarCadastroServico',
            endpoint='servicos/servico/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,

            }
        )

    def AlterarOS(
            self, Cabecalho, Departamentos, Email, InformacoesAdicionais, ServicosPrestados
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AlterarOS',
            endpoint='servicos/os/',
            param={
                "Cabecalho": Cabecalho,
                "Departamentos": Departamentos,
                "Email": Email,
                "InformacoesAdicionais": InformacoesAdicionais,
                "ServicosPrestados": ServicosPrestados,

            }
        )

    def ConsultarOS(
            self, cCodIntOS, nCodOS, cNumOS
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarOS',
            endpoint='servicos/os/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,
                "cNumOS": cNumOS,

            }
        )

    def ExcluirOS(
            self, cCodIntOS, nCodOS, cNumOS
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirOS',
            endpoint='servicos/os/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,
                "cNumOS": cNumOS,

            }
        )

    def IncluirOS(
            self, Cabecalho, Departamentos, Email, InformacoesAdicionais, ServicosPrestados
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirOS',
            endpoint='servicos/os/',
            param={
                "Cabecalho": Cabecalho,
                "Departamentos": Departamentos,
                "Email": Email,
                "InformacoesAdicionais": InformacoesAdicionais,
                "ServicosPrestados": ServicosPrestados,

            }
        )

    def ListarOS(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarOS',
            endpoint='servicos/os/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def StatusOS(
            self, cCodIntOS, nCodOS
    ) -> dict:
        """"""
        return self._chamar_api(
            call='StatusOS',
            endpoint='servicos/os/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,

            }
        )

    def TrocarEtapaOS(
            self, cCodIntOS, nCodOS, cNumOS, cEtapa
    ) -> dict:
        """"""
        return self._chamar_api(
            call='TrocarEtapaOS',
            endpoint='servicos/os/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,
                "cNumOS": cNumOS,
                "cEtapa": cEtapa,

            }
        )

    def AssociarCodIntOS(
            self, cCodIntOS, nCodOS
    ) -> dict:
        """"""
        return self._chamar_api(
            call='AssociarCodIntOS',
            endpoint='servicos/osp/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,

            }
        )

    def CancelarOS(
            self, cCodIntOS, nCodOS
    ) -> dict:
        """"""
        return self._chamar_api(
            call='CancelarOS',
            endpoint='servicos/osp/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,

            }
        )

    def DuplicarOS(
            self, cCodIntOS, nCodOS
    ) -> dict:
        """"""
        return self._chamar_api(
            call='DuplicarOS',
            endpoint='servicos/osp/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,

            }
        )

    def FaturarOS(
            self, cCodIntOS, nCodOS
    ) -> dict:
        """"""
        return self._chamar_api(
            call='FaturarOS',
            endpoint='servicos/osp/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,

            }
        )

    def ObterOS(
            self, cEtapa
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ObterOS',
            endpoint='servicos/osp/',
            param={
                "cEtapa": cEtapa,

            }
        )

    def ReenviarOS(
            self, cCodIntOS, nCodOS
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ReenviarOS',
            endpoint='servicos/osp/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,

            }
        )

    def ValidarOS(
            self, cCodIntOS, nCodOS
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ValidarOS',
            endpoint='servicos/osp/',
            param={
                "cCodIntOS": cCodIntOS,
                "nCodOS": nCodOS,

            }
        )

    def AlterarContrato(
            self, cabecalho, departamentos, emailCliente, infAdic, itensContrato, observacoes, vencTextos
    ) -> dict:
        """Alterar um Contrato"""
        return self._chamar_api(
            call='AlterarContrato',
            endpoint='servicos/contrato/',
            param={
                "cabecalho": cabecalho,
                "departamentos": departamentos,
                "emailCliente": emailCliente,
                "infAdic": infAdic,
                "itensContrato": itensContrato,
                "observacoes": observacoes,
                "vencTextos": vencTextos,

            }
        )

    def ConsultarContrato(
            self, contratoChave
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarContrato',
            endpoint='servicos/contrato/',
            param={
                "contratoChave": contratoChave,

            }
        )

    def ExcluirItem(
            self, contratoChave, ItensExclusao
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ExcluirItem',
            endpoint='servicos/contrato/',
            param={
                "contratoChave": contratoChave,
                "ItensExclusao": ItensExclusao,

            }
        )

    def IncluirContrato(
            self, cabecalho, departamentos, emailCliente, infAdic, itensContrato, observacoes, vencTextos
    ) -> dict:
        """"""
        return self._chamar_api(
            call='IncluirContrato',
            endpoint='servicos/contrato/',
            param={
                "cabecalho": cabecalho,
                "departamentos": departamentos,
                "emailCliente": emailCliente,
                "infAdic": infAdic,
                "itensContrato": itensContrato,
                "observacoes": observacoes,
                "vencTextos": vencTextos,

            }
        )

    def ListarContratos(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Lista os contratos cadastrados."""
        return self._chamar_api(
            call='ListarContratos',
            endpoint='servicos/contrato/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api,

            }
        )

    def UpsertContrato(
            self, cabecalho, departamentos, emailCliente, infAdic, itensContrato, observacoes, vencTextos
    ) -> dict:
        """Inclui / Altera um contrato"""
        return self._chamar_api(
            call='UpsertContrato',
            endpoint='servicos/contrato/',
            param={
                "cabecalho": cabecalho,
                "departamentos": departamentos,
                "emailCliente": emailCliente,
                "infAdic": infAdic,
                "itensContrato": itensContrato,
                "observacoes": observacoes,
                "vencTextos": vencTextos,

            }
        )

    def AtivarContrato(
            self, nCodCtr
    ) -> dict:
        """Ativa um contrato"""
        return self._chamar_api(
            call='AtivarContrato',
            endpoint='servicos/contratofat/',
            param={
                "nCodCtr": nCodCtr,

            }
        )

    def CancelarContrato(
            self, nCodCtr
    ) -> dict:
        """Cancela contrato"""
        return self._chamar_api(
            call='CancelarContrato',
            endpoint='servicos/contratofat/',
            param={
                "nCodCtr": nCodCtr,

            }
        )

    def FaturarContrato(
            self, nCodCtr
    ) -> dict:
        """Fatura um contrato."""
        return self._chamar_api(
            call='FaturarContrato',
            endpoint='servicos/contratofat/',
            param={
                "nCodCtr": nCodCtr,

            }
        )

    def ObterContratos(
            self, cEtapa
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ObterContratos',
            endpoint='servicos/contratofat/',
            param={
                "cEtapa": cEtapa,

            }
        )

    def ReativarContrato(
            self, nCodCtr
    ) -> dict:
        """Reativar contrato"""
        return self._chamar_api(
            call='ReativarContrato',
            endpoint='servicos/contratofat/',
            param={
                "nCodCtr": nCodCtr,

            }
        )

    def SuspenderContrato(
            self, nCodCtr
    ) -> dict:
        """Suspende contrato"""
        return self._chamar_api(
            call='SuspenderContrato',
            endpoint='servicos/contratofat/',
            param={
                "nCodCtr": nCodCtr,

            }
        )

    def ValidarContrato(
            self, nCodCtr
    ) -> dict:
        """Valida os dados de um contrato para faturamento."""
        return self._chamar_api(
            call='ValidarContrato',
            endpoint='servicos/contratofat/',
            param={
                "nCodCtr": nCodCtr,

            }
        )

    def ListarServMunic(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarServMunic',
            endpoint='servicos/listaservico/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarTiposTrib(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarTiposTrib',
            endpoint='servicos/tipotrib/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarLC116(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarLC116',
            endpoint='servicos/lc116/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarNBS(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarNBS',
            endpoint='servicos/nbs/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarProdutosIBPT(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista os produtos da Tabela do IBPT."""
        return self._chamar_api(
            call='ListarProdutosIBPT',
            endpoint='servicos/ibpt/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarServicosIBPT(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarServicosIBPT',
            endpoint='servicos/ibpt/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarTipoFatContrato(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Lista os tipos de faturamento de contrato."""
        return self._chamar_api(
            call='ListarTipoFatContrato',
            endpoint='servicos/contratotpfat/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarTipoUtilizacao(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarTipoUtilizacao',
            endpoint='servicos/tipoutilizacao/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarClassificacaoServico(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarClassificacaoServico',
            endpoint='servicos/classificacaoservico/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,

            }
        )

    def ListarDocumentos(
            self, nPagina, nRegPorPagina, cModelo, dEmiInicial, dEmiFinal
    ) -> dict:
        """Lista de XMLs de Documentos Fiscais."""
        return self._chamar_api(
            call='ListarDocumentos',
            endpoint='contador/xml/',
            param={
                "nPagina": nPagina,
                "nRegPorPagina": nRegPorPagina,
                "cModelo": cModelo,
                "dEmiInicial": dEmiInicial,
                "dEmiFinal": dEmiFinal,

            }
        )
