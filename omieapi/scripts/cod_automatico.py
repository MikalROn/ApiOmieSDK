from omieapi.omiebase import OmieBase

# Aviso -> antes de usar confira se n�o a oq vc precisa j� feito no codigo principal,
# o codigo autogerdo pode conter erros n�o detectados ainda
class CodigoAutogerado(OmieBase):
    """Este codigo foi automaticamente geredo por um script de scrap """
    def alterar_cliente(
            self, codigo_cliente_integracao, email, razao_social, nome_fantasia
            ) -> dict:
                """Altera os dados do cliente"""
                return self._chamar_api(
                    call='AlterarCliente',
                    endpoint='geral/clientes/',
                    param = {
                "codigo_cliente_integracao":codigo_cliente_integracao,
                "email": email,
                "razao_social": razao_social,
                "nome_fantasia": nome_fantasia
                    }
                )
            
    def associar_cod_int_cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AssociarCodIntCliente',
                    endpoint='geral/clientes/',
                    param = {
                "codigo_cliente_omie":codigo_cliente_omie,
                "codigo_cliente_integracao":codigo_cliente_integracao,

}
                )
            
    def consultar_cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
            ) -> dict:
                """Consulta os dados de um cliente"""
                return self._chamar_api(
                    call='ConsultarCliente',
                    endpoint='geral/clientes/',
                    param = {
                "codigo_cliente_omie":codigo_cliente_omie,
                "codigo_cliente_integracao":codigo_cliente_integracao,

}
                )
            
    def excluir_cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
            ) -> dict:
                """Exclui um cliente da base de dados."""
                return self._chamar_api(
                    call='ExcluirCliente',
                    endpoint='geral/clientes/',
                    param = {
                "codigo_cliente_omie":codigo_cliente_omie,
                "codigo_cliente_integracao":codigo_cliente_integracao,

}
                )
            
    def incluir_cliente(
            self, codigo_cliente_integracao, email, razao_social, nome_fantasia
            ) -> dict:
                """Inclui o cliente no Omie"""
                return self._chamar_api(
                    call='IncluirCliente',
                    endpoint='geral/clientes/',
                    param = {
                "codigo_cliente_integracao":codigo_cliente_integracao,
                "email":email,
                "razao_social":razao_social,
                "nome_fantasia":nome_fantasia,

}
                )
            
    def incluir_clientes_por_lote(
            self, clientes_cadastro, lote
            ) -> dict:
                """DEPRECATED"""
                return self._chamar_api(
                    call='IncluirClientesPorLote',
                    endpoint='geral/clientes/',
                    param = {
                "clientes_cadastro":clientes_cadastro,
                "lote":lote,

}
                )
            
    def listar_clientes(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Lista os clientes cadastrados"""
                return self._chamar_api(
                    call='ListarClientes',
                    endpoint='geral/clientes/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def listar_clientes_resumido(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Realiza pesquisa dos clientes"""
                return self._chamar_api(
                    call='ListarClientesResumido',
                    endpoint='geral/clientes/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def upsert_cliente(
            self, codigo_cliente_integracao, email, razao_social, nome_fantasia
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='UpsertCliente',
                    endpoint='geral/clientes/',
                    param = {
                "codigo_cliente_integracao":codigo_cliente_integracao,
                "email":email,
                "razao_social":razao_social,
                "nome_fantasia":nome_fantasia,

}
                )
            
    def upsert_cliente_cpf_cnpj(
            self, cnpj_cpf, email, razao_social, nome_fantasia
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='UpsertClienteCpfCnpj',
                    endpoint='geral/clientes/',
                    param = {
                "cnpj_cpf":cnpj_cpf,
                "email":email,
                "razao_social":razao_social,
                "nome_fantasia":nome_fantasia,

}
                )
            
    def upsert_clientes_por_lote(
            self, clientes_cadastro, lote
            ) -> dict:
                """DEPRECATED"""
                return self._chamar_api(
                    call='UpsertClientesPorLote',
                    endpoint='geral/clientes/',
                    param = {
                "clientes_cadastro":clientes_cadastro,
                "lote":lote,

}
                )
            
    def alterar_caract_cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao, campo, conteudo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarCaractCliente',
                    endpoint='geral/clientescaract/',
                    param = {
                "codigo_cliente_omie":codigo_cliente_omie,
                "codigo_cliente_integracao":codigo_cliente_integracao,
                "campo":campo,
                "conteudo":conteudo,

}
                )
            
    def consultar_caract_cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarCaractCliente',
                    endpoint='geral/clientescaract/',
                    param = {
                "codigo_cliente_omie":codigo_cliente_omie,
                "codigo_cliente_integracao":codigo_cliente_integracao,

}
                )
            
    def excluir_caract_cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao, campo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirCaractCliente',
                    endpoint='geral/clientescaract/',
                    param = {
                "codigo_cliente_omie":codigo_cliente_omie,
                "codigo_cliente_integracao":codigo_cliente_integracao,
                "campo":campo,

}
                )
            
    def excluir_todas_caract_cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirTodasCaractCliente',
                    endpoint='geral/clientescaract/',
                    param = {
                "codigo_cliente_omie":codigo_cliente_omie,
                "codigo_cliente_integracao":codigo_cliente_integracao,

}
                )
            
    def incluir_caract_cliente(
            self, codigo_cliente_omie, codigo_cliente_integracao, campo, conteudo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirCaractCliente',
                    endpoint='geral/clientescaract/',
                    param = {
                "codigo_cliente_omie":codigo_cliente_omie,
                "codigo_cliente_integracao":codigo_cliente_integracao,
                "campo":campo,
                "conteudo":conteudo,

}
                )
            
    def excluir_tags(
            self, nCodCliente, cCodIntCliente, tags
            ) -> dict:
                """Remove tags associadas a um cliente."""
                return self._chamar_api(
                    call='ExcluirTags',
                    endpoint='geral/clientetag/',
                    param = {
                "nCodCliente":nCodCliente,
                "cCodIntCliente":cCodIntCliente,
                "tags":tags,

}
                )
            
    def excluir_todas(
            self, nCodCliente, cCodIntCliente
            ) -> dict:
                """Remove todas as tags associadas a um cliente."""
                return self._chamar_api(
                    call='ExcluirTodas',
                    endpoint='geral/clientetag/',
                    param = {
                "nCodCliente":nCodCliente,
                "cCodIntCliente":cCodIntCliente,

}
                )
            
    def incluir_tags(
            self, nCodCliente, cCodIntCliente, tags
            ) -> dict:
                """Associa tags a um cliente."""
                return self._chamar_api(
                    call='IncluirTags',
                    endpoint='geral/clientetag/',
                    param = {
                "nCodCliente":nCodCliente,
                "cCodIntCliente":cCodIntCliente,
                "tags":tags,

}
                )
            
    def listar_tags(
            self, nCodCliente, cCodIntCliente
            ) -> dict:
                """Lista as tags de um determinado cliente."""
                return self._chamar_api(
                    call='ListarTags',
                    endpoint='geral/clientetag/',
                    param = {
                "nCodCliente":nCodCliente,
                "cCodIntCliente":cCodIntCliente,

}
                )
            
    def alterar_projeto(
            self, codigo, codint, nome, inativo
            ) -> dict:
                """Altera um projeto"""
                return self._chamar_api(
                    call='AlterarProjeto',
                    endpoint='geral/projetos/',
                    param = {
                "codigo":codigo,
                "codint":codint,
                "nome":nome,
                "inativo":inativo,

}
                )
            
    def consultar_projeto(
            self, codigo, codint
            ) -> dict:
                """Consulta um projeto"""
                return self._chamar_api(
                    call='ConsultarProjeto',
                    endpoint='geral/projetos/',
                    param = {
                "codigo":codigo,
                "codint":codint,

}
                )
            
    def excluir_projeto(
            self, codigo, codint
            ) -> dict:
                """Exclui um projeto"""
                return self._chamar_api(
                    call='ExcluirProjeto',
                    endpoint='geral/projetos/',
                    param = {
                "codigo":codigo,
                "codint":codint,

}
                )
            
    def incluir_projeto(
            self, codint, nome, inativo
            ) -> dict:
                """Inclui um novo projeto"""
                return self._chamar_api(
                    call='IncluirProjeto',
                    endpoint='geral/projetos/',
                    param = {
                "codint":codint,
                "nome":nome,
                "inativo":inativo,

}
                )
            
    def listar_projetos(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Lista os projetos cadastrados"""
                return self._chamar_api(
                    call='ListarProjetos',
                    endpoint='geral/projetos/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def upsert_projeto(
            self, codigo, codint, nome, inativo
            ) -> dict:
                """Inclui / Altera um projeto."""
                return self._chamar_api(
                    call='UpsertProjeto',
                    endpoint='geral/projetos/',
                    param = {
                "codigo":codigo,
                "codint":codint,
                "nome":nome,
                "inativo":inativo,

}
                )
            
    def consultar_empresa(
            self, codigo_empresa
            ) -> dict:
                """Realiza a consulta de um registro especifico"""
                return self._chamar_api(
                    call='ConsultarEmpresa',
                    endpoint='geral/empresas/',
                    param = {
                "codigo_empresa":codigo_empresa,

}
                )
            
    def listar_empresas(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Lista as empresas cadastradas no Omie."""
                return self._chamar_api(
                    call='ListarEmpresas',
                    endpoint='geral/empresas/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def consultar_departamento(
            self, codigo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarDepartamento',
                    endpoint='geral/departamentos/',
                    param = {
                "codigo":codigo,

}
                )
            
    def listar_depatartamentos(
            self, pagina, registros_por_pagina
            ) -> dict:
                """DEPRECATED"""
                return self._chamar_api(
                    call='ListarDepatartamentos',
                    endpoint='geral/departamentos/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def consultar_categoria(
            self, codigo
            ) -> dict:
                """Consulta uma categoria"""
                return self._chamar_api(
                    call='ConsultarCategoria',
                    endpoint='geral/categorias/',
                    param = {
                "codigo":codigo,

}
                )
            
    def listar_categorias(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista as categorias cadastradas"""
                return self._chamar_api(
                    call='ListarCategorias',
                    endpoint='geral/categorias/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_parcelas(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista de Parcelas cadastradas."""
                return self._chamar_api(
                    call='ListarParcelas',
                    endpoint='geral/parcelas/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_tipo_ativ(
            self, filtrar_por_codigo, filtrar_por_descricao
            ) -> dict:
                """Listar Tipos de Atividade."""
                return self._chamar_api(
                    call='ListarTipoAtiv',
                    endpoint='geral/tpativ/',
                    param = {
                "filtrar_por_codigo":filtrar_por_codigo,
                "filtrar_por_descricao":filtrar_por_descricao,

}
                )
            
    def listar_c_n_a_e(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar os CNAEs cadastrados"""
                return self._chamar_api(
                    call='ListarCNAE',
                    endpoint='produtos/cnae/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def pesquisar_cidades(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='PesquisarCidades',
                    endpoint='geral/cidades/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_paises(
            self, filtrar_por_codigo, filtrar_por_descricao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarPaises',
                    endpoint='geral/paises/',
                    param = {
                "filtrar_por_codigo":filtrar_por_codigo,
                "filtrar_por_descricao":filtrar_por_descricao,

}
                )
            
    def listar_tipos_anexos(
            self, codigo
            ) -> dict:
                """Listagem de tipos de anexos."""
                return self._chamar_api(
                    call='ListarTiposAnexos',
                    endpoint='geral/tiposanexo/',
                    param = {
                "codigo":codigo,

}
                )
            
    def incluir_anexo(
            self, cCodIntAnexo, cTabela, nId, cNomeArquivo, cTipoArquivo, cArquivo, cMd5
            ) -> dict:
                """Inclui o anexo para um documento."""
                return self._chamar_api(
                    call='IncluirAnexo',
                    endpoint='geral/anexo/',
                    param = {
                "cCodIntAnexo":cCodIntAnexo,
                "cTabela":cTabela,
                "nId":nId,
                "cNomeArquivo":cNomeArquivo,
                "cTipoArquivo":cTipoArquivo,
                "cArquivo":cArquivo,
                "cMd5":cMd5
            }
                )
            
    def alterar_tipo_entrega(
            self, nCodEntrega, cCodIntEntrega, cDescricao, cInativo
            ) -> dict:
                """Alterar tipo de entrega"""
                return self._chamar_api(
                    call='AlterarTipoEntrega',
                    endpoint='geral/tiposentrega/',
                    param = {
                "nCodEntrega":nCodEntrega,
                "cCodIntEntrega":cCodIntEntrega,
                "cDescricao":cDescricao,
                "cInativo":cInativo,

}
                )
            
    def consultar_tipo_entrega(
            self, nCodEntrega, cCodIntEntrega
            ) -> dict:
                """Consultar tipo de entrega"""
                return self._chamar_api(
                    call='ConsultarTipoEntrega',
                    endpoint='geral/tiposentrega/',
                    param = {
                "nCodEntrega":nCodEntrega,
                "cCodIntEntrega":cCodIntEntrega,

}
                )
            
    def excluir_tipo_entrega(
            self, nCodEntrega, cCodIntEntrega
            ) -> dict:
                """Excluir tipo de entrega"""
                return self._chamar_api(
                    call='ExcluirTipoEntrega',
                    endpoint='geral/tiposentrega/',
                    param = {
                "nCodEntrega":nCodEntrega,
                "cCodIntEntrega":cCodIntEntrega,

}
                )
            
    def incluir_tipo_entrega(
            self, nCodTransp, cCodIntEntrega, cDescricao, cInativo
            ) -> dict:
                """Incluir tipo de entrega"""
                return self._chamar_api(
                    call='IncluirTipoEntrega',
                    endpoint='geral/tiposentrega/',
                    param = {
                "nCodTransp":nCodTransp,
                "cCodIntEntrega":cCodIntEntrega,
                "cDescricao":cDescricao,
                "cInativo":cInativo,

}
                )
            
    def listar_tipo_entrega(
            self, nPagina, nRegistrosPorPagina, nCodTransp
            ) -> dict:
                """Listar tipo de entrega"""
                return self._chamar_api(
                    call='ListarTipoEntrega',
                    endpoint='geral/tiposentrega/',
                    param = {
                "nPagina":nPagina,
                "nRegistrosPorPagina":nRegistrosPorPagina,
                "nCodTransp":nCodTransp,

}
                )
            
    def listar_tipo_assinante(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista os tipos de assinante"""
                return self._chamar_api(
                    call='ListarTipoAssinante',
                    endpoint='geral/tipoassinante/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_contas(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista as contas do CRM."""
                return self._chamar_api(
                    call='ListarContas',
                    endpoint='crm/contas/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def verificar_conta(
            self, cNome, cEmail
            ) -> dict:
                """Verifica se uma conta foi criada a partir do nome e e-mail."""
                return self._chamar_api(
                    call='VerificarConta',
                    endpoint='crm/contas/',
                    param = {
                "cNome":cNome,
                "cEmail":cEmail,

}
                )
            
    def alterar_caract_conta(
            self, nCod, cCodInt, campo, conteudo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarCaractConta',
                    endpoint='crm/contascaract/',
                    param = {
                "nCod":nCod,
                "cCodInt":cCodInt,
                "campo":campo,
                "conteudo":conteudo,

}
                )
            
    def consultar_caract_conta(
            self, nCod, cCodInt
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarCaractConta',
                    endpoint='crm/contascaract/',
                    param = {
                "nCod":nCod,
                "cCodInt":cCodInt,

}
                )
            
    def excluir_caract_conta(
            self, nCod, cCodInt, campo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirCaractConta',
                    endpoint='crm/contascaract/',
                    param = {
                "nCod":nCod,
                "cCodInt":cCodInt,
                "campo":campo,

}
                )
            
    def excluir_todas_caract_conta(
            self, nCod, cCodInt
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirTodasCaractConta',
                    endpoint='crm/contascaract/',
                    param = {
                "nCod":nCod,
                "cCodInt":cCodInt,

}
                )
            
    def incluir_caract_conta(
            self, nCod, cCodInt, campo, conteudo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirCaractConta',
                    endpoint='crm/contascaract/',
                    param = {
                "nCod":nCod,
                "cCodInt":cCodInt,
                "campo":campo,
                "conteudo":conteudo,

}
                )
            
    def consultar_contato(
            self, nCod, cCodInt
            ) -> dict:
                """Consulta o Contato"""
                return self._chamar_api(
                    call='ConsultarContato',
                    endpoint='crm/contatos/',
                    param = {
                "nCod":nCod,
                "cCodInt":cCodInt,

}
                )
            
    def incluir_contato(
            self, identificacao, endereco, telefone_email
            ) -> dict:
                """Inclui um novo Contato"""
                return self._chamar_api(
                    call='IncluirContato',
                    endpoint='crm/contatos/',
                    param = {
                "identificacao":identificacao,
                "endereco":endereco,
                "telefone_email":telefone_email,

}
                )
            
    def listar_contatos(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista os contatos do CRM."""
                return self._chamar_api(
                    call='ListarContatos',
                    endpoint='crm/contatos/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def upsert_contato(
            self, identificacao, endereco, telefone_email
            ) -> dict:
                """Upsert do contato"""
                return self._chamar_api(
                    call='UpsertContato',
                    endpoint='crm/contatos/',
                    param = {
                "identificacao":identificacao,
                "endereco":endereco,
                "telefone_email":telefone_email,

}
                )
            
    def verificar_contato(
            self, cNome, cEmail
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='VerificarContato',
                    endpoint='crm/contatos/',
                    param = {
                "cNome":cNome,
                "cEmail":cEmail,

}
                )
            
    def alterar_oportunidade(
            self, identificacao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarOportunidade',
                    endpoint='crm/oportunidades/',
                    param = {
                "identificacao":identificacao,

}
                )
            
    def consultar_oportunidade(
            self, nCodOp, cCodIntOp
            ) -> dict:
                """Consulta de oportunidade."""
                return self._chamar_api(
                    call='ConsultarOportunidade',
                    endpoint='crm/oportunidades/',
                    param = {
                "nCodOp":nCodOp,
                "cCodIntOp":cCodIntOp,

}
                )
            
    def excluir_oportunidade(
            self, nCodOp, cCodIntOp
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirOportunidade',
                    endpoint='crm/oportunidades/',
                    param = {
                "nCodOp":nCodOp,
                "cCodIntOp":cCodIntOp,

}
                )
            
    def incluir_oportunidade(
            self, identificacao
            ) -> dict:
                """Incluir uma oportunidade."""
                return self._chamar_api(
                    call='IncluirOportunidade',
                    endpoint='crm/oportunidades/',
                    param = {
                "identificacao":identificacao,

}
                )
            
    def listar_oportunidades(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista de oportunidades."""
                return self._chamar_api(
                    call='ListarOportunidades',
                    endpoint='crm/oportunidades/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def upsert_oportunidade(
            self, identificacao
            ) -> dict:
                """Upsert de oportunidade."""
                return self._chamar_api(
                    call='UpsertOportunidade',
                    endpoint='crm/oportunidades/',
                    param = {
                "identificacao":identificacao,

}
                )
            
    def obter_lista_op(
            self, cMesAno, cTemperatura
            ) -> dict:
                """Lista de Oportunidades."""
                return self._chamar_api(
                    call='ObterListaOp',
                    endpoint='crm/oportunidades-resumo/',
                    param = {
                "cMesAno":cMesAno,
                "cTemperatura":cTemperatura,

}
                )
            
    def alterar_tarefa(
            self, nCodTarefa, nCodOp, cCodInt, nCodUsuario, dData, cHora, nCodNotif, nCodAtividade, cDescricao
            ) -> dict:
                """Altera uma tarefa."""
                return self._chamar_api(
                    call='AlterarTarefa',
                    endpoint='crm/tarefas/',
                    param = {
                "nCodTarefa":nCodTarefa,
                "nCodOp":nCodOp,
                "cCodInt":cCodInt,
                "nCodUsuario":nCodUsuario,
                "dData":dData,
                "cHora":cHora,
                "nCodNotif":nCodNotif,
                "nCodAtividade":nCodAtividade,
                "cDescricao":cDescricao,

}
                )
            
    def calendario_tarefas(
            self, email_vend, calendar_key
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='CalendarioTarefas',
                    endpoint='crm/tarefas/',
                    param = {
                "email_vend":email_vend,
                "calendar_key":calendar_key,

}
                )
            
    def consultar_tarefa(
            self, nCodTarefa, nCodOp, cCodInt
            ) -> dict:
                """Consulta uma tarefa da oportunidade."""
                return self._chamar_api(
                    call='ConsultarTarefa',
                    endpoint='crm/tarefas/',
                    param = {
                "nCodTarefa":nCodTarefa,
                "nCodOp":nCodOp,
                "cCodInt":cCodInt,

}
                )
            
    def excluir_tarefa(
            self, nCodTarefa, nCodOp, cCodInt
            ) -> dict:
                """Exclui um tarefa."""
                return self._chamar_api(
                    call='ExcluirTarefa',
                    endpoint='crm/tarefas/',
                    param = {
                "nCodTarefa":nCodTarefa,
                "nCodOp":nCodOp,
                "cCodInt":cCodInt,

}
                )
            
    def incluir_tarefa(
            self, nCodOp, cCodInt, nCodUsuario, dData, cHora, nCodNotif, nCodAtividade, cDescricao
            ) -> dict:
                """Inclui uma tarefa na oportunidade."""
                return self._chamar_api(
                    call='IncluirTarefa',
                    endpoint='crm/tarefas/',
                    param = {
                "nCodOp":nCodOp,
                "cCodInt":cCodInt,
                "nCodUsuario":nCodUsuario,
                "dData":dData,
                "cHora":cHora,
                "nCodNotif":nCodNotif,
                "nCodAtividade":nCodAtividade,
                "cDescricao":cDescricao,

}
                )
            
    def listar_emails_tarefas(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista os  emails tarefas."""
                return self._chamar_api(
                    call='ListarEmailsTarefas',
                    endpoint='crm/tarefas/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_tarefas(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Tarefas da oportunidade."""
                return self._chamar_api(
                    call='ListarTarefas',
                    endpoint='crm/tarefas/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def upsert_tarefa(
            self, nCodTarefa, nCodOp, cCodInt, nCodUsuario, dData, cHora, nCodNotif, nCodAtividade, cDescricao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='UpsertTarefa',
                    endpoint='crm/tarefas/',
                    param = {
                "nCodTarefa":nCodTarefa,
                "nCodOp":nCodOp,
                "cCodInt":cCodInt,
                "nCodUsuario":nCodUsuario,
                "dData":dData,
                "cHora":cHora,
                "nCodNotif":nCodNotif,
                "nCodAtividade":nCodAtividade,
                "cDescricao":cDescricao,

}
                )
            
    def obter_detalhes_tarefa(
            self, nIdOportunidade, nIdTarefa
            ) -> dict:
                """Consulta os detalhes de uma tafera."""
                return self._chamar_api(
                    call='ObterDetalhesTarefa',
                    endpoint='crm/tarefas-resumo/',
                    param = {
                "nIdOportunidade":nIdOportunidade,
                "nIdTarefa":nIdTarefa,

}
                )
            
    def obter_lista_tarefas(
            self, dDia
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ObterListaTarefas',
                    endpoint='crm/tarefas-resumo/',
                    param = {
                "dDia":dDia,

}
                )
            
    def obter_resumo_tarefas(
            self, dDataInicio, dDataFim, cTipoTarefa
            ) -> dict:
                """Resumos das tarefas do CRM."""
                return self._chamar_api(
                    call='ObterResumoTarefas',
                    endpoint='crm/tarefas-resumo/',
                    param = {
                "dDataInicio":dDataInicio,
                "dDataFim":dDataFim,
                "cTipoTarefa":cTipoTarefa,

}
                )
            
    def listar_solucoes(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarSolucoes',
                    endpoint='crm/solucoes/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_fases(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Fases da Oportunidade"""
                return self._chamar_api(
                    call='ListarFases',
                    endpoint='crm/fases/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_usuarios(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarUsuarios',
                    endpoint='crm/usuarios/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def obter_usuarios(
            self, cExibirTodos
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ObterUsuarios',
                    endpoint='crm/usuarios/',
                    param = {
                "cExibirTodos":cExibirTodos,

}
                )
            
    def listar_status(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Status da oportunidade."""
                return self._chamar_api(
                    call='ListarStatus',
                    endpoint='crm/status/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_motivos(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Motivos da oportunidade."""
                return self._chamar_api(
                    call='ListarMotivos',
                    endpoint='crm/motivos/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_tipos(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Tipos de oportunidades."""
                return self._chamar_api(
                    call='ListarTipos',
                    endpoint='crm/tipos/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_parceiros(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Parceiros e equipes da oportunidade."""
                return self._chamar_api(
                    call='ListarParceiros',
                    endpoint='crm/parceiros/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_finders(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Finders da oportunidade."""
                return self._chamar_api(
                    call='ListarFinders',
                    endpoint='crm/finders/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_origens(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Origens da oportunidade."""
                return self._chamar_api(
                    call='ListarOrigens',
                    endpoint='crm/origens/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_concorrentes(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Concorrentes da oportunidade."""
                return self._chamar_api(
                    call='ListarConcorrentes',
                    endpoint='crm/concorrentes/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_verticais(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista as verticais cadastradas."""
                return self._chamar_api(
                    call='ListarVerticais',
                    endpoint='crm/verticais/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def alterar_vendedor(
            self, codigo, codInt, nome, inativo, email, fatura_pedido, visualiza_pedido, comissao
            ) -> dict:
                """Altera os dados de um vendedor"""
                return self._chamar_api(
                    call='AlterarVendedor',
                    endpoint='geral/vendedores/',
                    param = {
                "codigo":codigo,
                "codInt":codInt,
                "nome":nome,
                "inativo":inativo,
                "email":email,
                "fatura_pedido":fatura_pedido,
                "visualiza_pedido":visualiza_pedido,
                "comissao":comissao,

}
                )
            
    def consultar_vendedor(
            self, codigo, codInt
            ) -> dict:
                """Consulta os dados de um vendedor"""
                return self._chamar_api(
                    call='ConsultarVendedor',
                    endpoint='geral/vendedores/',
                    param = {
                "codigo":codigo,
                "codInt":codInt,

}
                )
            
    def excluir_vendedor(
            self, codigo, codInt
            ) -> dict:
                """Exclui um vendedor"""
                return self._chamar_api(
                    call='ExcluirVendedor',
                    endpoint='geral/vendedores/',
                    param = {
                "codigo":codigo,
                "codInt":codInt,

}
                )
            
    def incluir_vendedor(
            self, codInt, nome, inativo, email, fatura_pedido, visualiza_pedido, comissao
            ) -> dict:
                """Inclui um vendedor"""
                return self._chamar_api(
                    call='IncluirVendedor',
                    endpoint='geral/vendedores/',
                    param = {
                "codInt":codInt,
                "nome":nome,
                "inativo":inativo,
                "email":email,
                "fatura_pedido":fatura_pedido,
                "visualiza_pedido":visualiza_pedido,
                "comissao":comissao,

}
                )
            
    def listar_vendedores(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Listagem de Vendedores"""
                return self._chamar_api(
                    call='ListarVendedores',
                    endpoint='geral/vendedores/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def upsert_vendedor(
            self, codigo, codInt, nome, inativo, email, fatura_pedido, visualiza_pedido, comissao
            ) -> dict:
                """Inclui / Altera um vendedor"""
                return self._chamar_api(
                    call='UpsertVendedor',
                    endpoint='geral/vendedores/',
                    param = {
                "codigo":codigo,
                "codInt":codInt,
                "nome":nome,
                "inativo":inativo,
                "email":email,
                "fatura_pedido":fatura_pedido,
                "visualiza_pedido":visualiza_pedido,
                "comissao":comissao,

}
                )
            
    def consultar_tipo_tarefa(
            self, nIdTipoTarefa
            ) -> dict:
                """Consulta tipo de tarefa"""
                return self._chamar_api(
                    call='ConsultarTipoTarefa',
                    endpoint='crm/tipostarefa/',
                    param = {
                "nIdTipoTarefa":nIdTipoTarefa,

}
                )
            
    def excluir_tipo_tarefa(
            self, nIdTipoTarefa
            ) -> dict:
                """Excluir tipo de tarefa"""
                return self._chamar_api(
                    call='ExcluirTipoTarefa',
                    endpoint='crm/tipostarefa/',
                    param = {
                "nIdTipoTarefa":nIdTipoTarefa,

}
                )
            
    def listar_tipos_tarefa(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista tipos de tarefa"""
                return self._chamar_api(
                    call='ListarTiposTarefa',
                    endpoint='crm/tipostarefa/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def alterar_conta_corrente(
            self, cCodCCInt, tipo_conta_corrente, codigo_banco, descricao, saldo_inicial
            ) -> dict:
                """Altera a Conta Corrente"""
                return self._chamar_api(
                    call='AlterarContaCorrente',
                    endpoint='geral/contacorrente/',
                    param = {
                "cCodCCInt":cCodCCInt,
                "tipo_conta_corrente":tipo_conta_corrente,
                "codigo_banco":codigo_banco,
                "descricao":descricao,
                "saldo_inicial":saldo_inicial,

}
                )
            
    def consultar_conta_corrente(
            self, nCodCC, cCodCCInt
            ) -> dict:
                """Realiza a consulta de uma conta corrente"""
                return self._chamar_api(
                    call='ConsultarContaCorrente',
                    endpoint='geral/contacorrente/',
                    param = {
                "nCodCC":nCodCC,
                "cCodCCInt":cCodCCInt,

}
                )
            
    def excluir_conta_corrente(
            self, nCodCC, cCodCCInt
            ) -> dict:
                """Excluir a Conta Corrente"""
                return self._chamar_api(
                    call='ExcluirContaCorrente',
                    endpoint='geral/contacorrente/',
                    param = {
                "nCodCC":nCodCC,
                "cCodCCInt":cCodCCInt,

}
                )
            
    def incluir_conta_corrente(
            self, cCodCCInt, tipo_conta_corrente, codigo_banco, descricao, saldo_inicial
            ) -> dict:
                """Inclui uma conta corrente"""
                return self._chamar_api(
                    call='IncluirContaCorrente',
                    endpoint='geral/contacorrente/',
                    param = {
                "cCodCCInt":cCodCCInt,
                "tipo_conta_corrente":tipo_conta_corrente,
                "codigo_banco":codigo_banco,
                "descricao":descricao,
                "saldo_inicial":saldo_inicial,

}
                )
            
    def listar_contas_correntes(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Listar Contas Correntes"""
                return self._chamar_api(
                    call='ListarContasCorrentes',
                    endpoint='geral/contacorrente/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def listar_resumo_contas_correntes(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Listar resumida de Contas correntes."""
                return self._chamar_api(
                    call='ListarResumoContasCorrentes',
                    endpoint='geral/contacorrente/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def pesquisar_conta_corrente(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """DEPRECATED"""
                return self._chamar_api(
                    call='PesquisarContaCorrente',
                    endpoint='geral/contacorrente/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def upsert_conta_corrente(
            self, cCodCCInt, tipo_conta_corrente, codigo_banco, descricao, saldo_inicial
            ) -> dict:
                """Upsert da Conta Corrente"""
                return self._chamar_api(
                    call='UpsertContaCorrente',
                    endpoint='geral/contacorrente/',
                    param = {
                "cCodCCInt":cCodCCInt,
                "tipo_conta_corrente":tipo_conta_corrente,
                "codigo_banco":codigo_banco,
                "descricao":descricao,
                "saldo_inicial":saldo_inicial,

}
                )
            
    def upsert_conta_corrente_por_lote(
            self, lote, fin_conta_corrente_cadastro
            ) -> dict:
                """Upsert por lote de Conta Corrente"""
                return self._chamar_api(
                    call='UpsertContaCorrentePorLote',
                    endpoint='geral/contacorrente/',
                    param = {
                "lote":lote,
                "fin_conta_corrente_cadastro":fin_conta_corrente_cadastro,

}
                )
            
    def alterar_lanc_c_c(
            self, cCodIntLanc, cabecalho, detalhes
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarLancCC',
                    endpoint='financas/contacorrentelancamentos/',
                    param = {
                "cCodIntLanc":cCodIntLanc,
                "cabecalho":cabecalho,
                "detalhes":detalhes,

}
                )
            
    def consulta_lanc_c_c(
            self, nCodLanc, cCodIntLanc
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultaLancCC',
                    endpoint='financas/contacorrentelancamentos/',
                    param = {
                "nCodLanc":nCodLanc,
                "cCodIntLanc":cCodIntLanc,

}
                )
            
    def excluir_lanc_c_c(
            self, nCodLanc, cCodIntLanc
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirLancCC',
                    endpoint='financas/contacorrentelancamentos/',
                    param = {
                "nCodLanc":nCodLanc,
                "cCodIntLanc":cCodIntLanc,

}
                )
            
    def incluir_lanc_c_c(
            self, cCodIntLanc, cabecalho, detalhes
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirLancCC',
                    endpoint='financas/contacorrentelancamentos/',
                    param = {
                "cCodIntLanc":cCodIntLanc,
                "cabecalho":cabecalho,
                "detalhes":detalhes,

}
                )
            
    def listar_lanc_c_c(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarLancCC',
                    endpoint='financas/contacorrentelancamentos/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def alterar_conta_pagar(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento, codigo_categoria, data_previsao, id_conta_corrente
            ) -> dict:
                """Altera uma conta a pagar"""
                return self._chamar_api(
                    call='AlterarContaPagar',
                    endpoint='financas/contapagar/',
                    param = {
                "codigo_lancamento_integracao":codigo_lancamento_integracao,
                "codigo_cliente_fornecedor":codigo_cliente_fornecedor,
                "data_vencimento":data_vencimento,
                "valor_documento":valor_documento,
                "codigo_categoria":codigo_categoria,
                "data_previsao":data_previsao,
                "id_conta_corrente":id_conta_corrente,

}
                )
            
    def cancelar_pagamento(
            self, codigo_baixa
            ) -> dict:
                """Cancela um pagamento realizado no Contas a Pagar"""
                return self._chamar_api(
                    call='CancelarPagamento',
                    endpoint='financas/contapagar/',
                    param = {
                "codigo_baixa":codigo_baixa,

}
                )
            
    def consultar_conta_pagar(
            self, codigo_lancamento_omie, codigo_lancamento_integracao
            ) -> dict:
                """Consulta uma conta a pagar"""
                return self._chamar_api(
                    call='ConsultarContaPagar',
                    endpoint='financas/contapagar/',
                    param = {
                "codigo_lancamento_omie":codigo_lancamento_omie,
                "codigo_lancamento_integracao":codigo_lancamento_integracao,

}
                )
            
    def excluir_conta_pagar(
            self, codigo_lancamento_omie, codigo_lancamento_integracao
            ) -> dict:
                """Exclui uma conta a pagar"""
                return self._chamar_api(
                    call='ExcluirContaPagar',
                    endpoint='financas/contapagar/',
                    param = {
                "codigo_lancamento_omie":codigo_lancamento_omie,
                "codigo_lancamento_integracao":codigo_lancamento_integracao,

}
                )
            
    def incluir_conta_pagar(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento, codigo_categoria, data_previsao, id_conta_corrente
            ) -> dict:
                """Inclui uma conta a Pagar."""
                return self._chamar_api(
                    call='IncluirContaPagar',
                    endpoint='financas/contapagar/',
                    param = {
                "codigo_lancamento_integracao":codigo_lancamento_integracao,
                "codigo_cliente_fornecedor":codigo_cliente_fornecedor,
                "data_vencimento":data_vencimento,
                "valor_documento":valor_documento,
                "codigo_categoria":codigo_categoria,
                "data_previsao":data_previsao,
                "id_conta_corrente":id_conta_corrente,

}
                )
            
    def incluir_conta_pagar_por_lote(
            self, lote, conta_pagar_cadastro
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirContaPagarPorLote',
                    endpoint='financas/contapagar/',
                    param = {
                "lote":lote,
                "conta_pagar_cadastro":conta_pagar_cadastro,

}
                )
            
    def lancar_pagamento(
            self, codigo_lancamento, codigo_lancamento_integracao, codigo_baixa_integracao, codigo_conta_corrente, valor, desconto, juros, multa, data, observacao
            ) -> dict:
                """Efetua a baixa de um pagamento do contas a pagar."""
                return self._chamar_api(
                    call='LancarPagamento',
                    endpoint='financas/contapagar/',
                    param = {
                "codigo_lancamento":codigo_lancamento,
                "codigo_lancamento_integracao":codigo_lancamento_integracao,
                "codigo_baixa_integracao":codigo_baixa_integracao,
                "codigo_conta_corrente":codigo_conta_corrente,
                "valor":valor,
                "desconto":desconto,
                "juros":juros,
                "multa":multa,
                "data":data,
                "observacao":observacao,

}
                )
            
    def listar_contas_pagar(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Listar as Contas a Pagar"""
                return self._chamar_api(
                    call='ListarContasPagar',
                    endpoint='financas/contapagar/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def upsert_conta_pagar(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento, codigo_categoria, data_previsao, id_conta_corrente
            ) -> dict:
                """Upsert do Contas a Pagar"""
                return self._chamar_api(
                    call='UpsertContaPagar',
                    endpoint='financas/contapagar/',
                    param = {
                "codigo_lancamento_integracao":codigo_lancamento_integracao,
                "codigo_cliente_fornecedor":codigo_cliente_fornecedor,
                "data_vencimento":data_vencimento,
                "valor_documento":valor_documento,
                "codigo_categoria":codigo_categoria,
                "data_previsao":data_previsao,
                "id_conta_corrente":id_conta_corrente,

}
                )
            
    def upsert_conta_pagar_por_lote(
            self, lote, conta_pagar_cadastro
            ) -> dict:
                """Efetua o UPSERT do Contas a Pagar por Lote"""
                return self._chamar_api(
                    call='UpsertContaPagarPorLote',
                    endpoint='financas/contapagar/',
                    param = {
                "lote":lote,
                "conta_pagar_cadastro":conta_pagar_cadastro,

}
                )
            
    def alterar_conta_receber(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento, codigo_categoria, data_previsao, id_conta_corrente
            ) -> dict:
                """Altera um conta a receber"""
                return self._chamar_api(
                    call='AlterarContaReceber',
                    endpoint='financas/contareceber/',
                    param = {
                "codigo_lancamento_integracao":codigo_lancamento_integracao,
                "codigo_cliente_fornecedor":codigo_cliente_fornecedor,
                "data_vencimento":data_vencimento,
                "valor_documento":valor_documento,
                "codigo_categoria":codigo_categoria,
                "data_previsao":data_previsao,
                "id_conta_corrente":id_conta_corrente,

}
                )
            
    def cancelar_conta_receber(
            self, chave_lancamento
            ) -> dict:
                """Cancelamento do boleto gerado de uma conta a receber"""
                return self._chamar_api(
                    call='CancelarContaReceber',
                    endpoint='financas/contareceber/',
                    param = {
                "chave_lancamento":chave_lancamento,

}
                )
            
    def cancelar_recebimento(
            self, codigo_baixa
            ) -> dict:
                """Efetua o cancelamento de um recebimento de Contas a Receber."""
                return self._chamar_api(
                    call='CancelarRecebimento',
                    endpoint='financas/contareceber/',
                    param = {
                "codigo_baixa":codigo_baixa,

}
                )
            
    def conciliar_recebimento(
            self, codigo_baixa
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConciliarRecebimento',
                    endpoint='financas/contareceber/',
                    param = {
                "codigo_baixa":codigo_baixa,

}
                )
            
    def consultar_conta_receber(
            self, codigo_lancamento_omie, codigo_lancamento_integracao
            ) -> dict:
                """Consulta uma Conta a Pagar"""
                return self._chamar_api(
                    call='ConsultarContaReceber',
                    endpoint='financas/contareceber/',
                    param = {
                "codigo_lancamento_omie":codigo_lancamento_omie,
                "codigo_lancamento_integracao":codigo_lancamento_integracao,

}
                )
            
    def desconciliar_recebimento(
            self, codigo_baixa
            ) -> dict:
                """Desconciliar o Recebimento"""
                return self._chamar_api(
                    call='DesconciliarRecebimento',
                    endpoint='financas/contareceber/',
                    param = {
                "codigo_baixa":codigo_baixa,

}
                )
            
    def excluir_conta_receber(
            self, chave_lancamento
            ) -> dict:
                """Exclui uma conta a receber"""
                return self._chamar_api(
                    call='ExcluirContaReceber',
                    endpoint='financas/contareceber/',
                    param = {
                "chave_lancamento":chave_lancamento,

}
                )
            
    def incluir_conta_receber(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento, codigo_categoria, data_previsao, id_conta_corrente
            ) -> dict:
                """Inclui uma conta a Receber"""
                return self._chamar_api(
                    call='IncluirContaReceber',
                    endpoint='financas/contareceber/',
                    param = {
                "codigo_lancamento_integracao":codigo_lancamento_integracao,
                "codigo_cliente_fornecedor":codigo_cliente_fornecedor,
                "data_vencimento":data_vencimento,
                "valor_documento":valor_documento,
                "codigo_categoria":codigo_categoria,
                "data_previsao":data_previsao,
                "id_conta_corrente":id_conta_corrente,

}
                )
            
    def incluir_conta_receber_por_lote(
            self, lote, conta_receber_cadastro
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirContaReceberPorLote',
                    endpoint='financas/contareceber/',
                    param = {
                "lote":lote,
                "conta_receber_cadastro":conta_receber_cadastro,

}
                )
            
    def lancar_recebimento(
            self, codigo_lancamento, codigo_baixa, codigo_conta_corrente, valor, data, observacao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='LancarRecebimento',
                    endpoint='financas/contareceber/',
                    param = {
                "codigo_lancamento":codigo_lancamento,
                "codigo_baixa":codigo_baixa,
                "codigo_conta_corrente":codigo_conta_corrente,
                "valor":valor,
                "data":data,
                "observacao":observacao,

}
                )
            
    def listar_contas_receber(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Lista as contas a receber cadastradas."""
                return self._chamar_api(
                    call='ListarContasReceber',
                    endpoint='financas/contareceber/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def upsert_conta_receber(
            self, codigo_lancamento_integracao, codigo_cliente_fornecedor, data_vencimento, valor_documento, codigo_categoria, data_previsao, id_conta_corrente
            ) -> dict:
                """Executa o Upsert do Contas a receber"""
                return self._chamar_api(
                    call='UpsertContaReceber',
                    endpoint='financas/contareceber/',
                    param = {
                "codigo_lancamento_integracao":codigo_lancamento_integracao,
                "codigo_cliente_fornecedor":codigo_cliente_fornecedor,
                "data_vencimento":data_vencimento,
                "valor_documento":valor_documento,
                "codigo_categoria":codigo_categoria,
                "data_previsao":data_previsao,
                "id_conta_corrente":id_conta_corrente,

}
                )
            
    def upsert_conta_receber_por_lote(
            self, lote, conta_receber_cadastro
            ) -> dict:
                """Efetua o UPSERT do Contas a Receber por Lote."""
                return self._chamar_api(
                    call='UpsertContaReceberPorLote',
                    endpoint='financas/contareceber/',
                    param = {
                "lote":lote,
                "conta_receber_cadastro":conta_receber_cadastro,

}
                )
            
    def cancelar_boleto(
            self, nCodTitulo, cCodIntTitulo
            ) -> dict:
                """Cancela o Boleto."""
                return self._chamar_api(
                    call='CancelarBoleto',
                    endpoint='financas/contareceberboleto/',
                    param = {
                "nCodTitulo":nCodTitulo,
                "cCodIntTitulo":cCodIntTitulo,

}
                )
            
    def gerar_boleto(
            self, nCodTitulo, cCodIntTitulo
            ) -> dict:
                """Gera um Boleto referente a um Contas a Receber."""
                return self._chamar_api(
                    call='GerarBoleto',
                    endpoint='financas/contareceberboleto/',
                    param = {
                "nCodTitulo":nCodTitulo,
                "cCodIntTitulo":cCodIntTitulo,

}
                )
            
    def obter_boleto(
            self, nCodTitulo, cCodIntTitulo
            ) -> dict:
                """Disponibiliza o link de Download do Boleto."""
                return self._chamar_api(
                    call='ObterBoleto',
                    endpoint='financas/contareceberboleto/',
                    param = {
                "nCodTitulo":nCodTitulo,
                "cCodIntTitulo":cCodIntTitulo,

}
                )
            
    def prorrogar_boleto(
            self, nCodTitulo, cCodIntTitulo, dDtVenc
            ) -> dict:
                """Prorroga o vencimento do Boleto."""
                return self._chamar_api(
                    call='ProrrogarBoleto',
                    endpoint='financas/contareceberboleto/',
                    param = {
                "nCodTitulo":nCodTitulo,
                "cCodIntTitulo":cCodIntTitulo,
                "dDtVenc":dDtVenc,

}
                )
            
    def listar_extrato(
            self, nCodCC, cCodIntCC, dPeriodoInicial, dPeriodoFinal
            ) -> dict:
                """Listagem do Extrato"""
                return self._chamar_api(
                    call='ListarExtrato',
                    endpoint='financas/extrato/',
                    param = {
                "nCodCC":nCodCC,
                "cCodIntCC":cCodIntCC,
                "dPeriodoInicial":dPeriodoInicial,
                "dPeriodoFinal":dPeriodoFinal,

}
                )
            
    def listar_orcamentos(
            self, nAno, nMes
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarOrcamentos',
                    endpoint='financas/caixa/',
                    param = {
                "nAno":nAno,
                "nMes":nMes,

}
                )
            
    def obter_u_r_l_boleto(
            self, nCodTitulo, cCodIntTitulo
            ) -> dict:
                """DEPRECATED"""
                return self._chamar_api(
                    call='ObterURLBoleto',
                    endpoint='financas/pesquisartitulos/',
                    param = {
                "nCodTitulo":nCodTitulo,
                "cCodIntTitulo":cCodIntTitulo,

}
                )
            
    def pesquisar_excluidos(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='PesquisarExcluidos',
                    endpoint='financas/pesquisartitulos/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def pesquisar_lancamentos(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='PesquisarLancamentos',
                    endpoint='financas/pesquisartitulos/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def obter_resumo_contador(
            self, dDataInicio, dDataFim
            ) -> dict:
                """Obtem o resumo do painel do contador."""
                return self._chamar_api(
                    call='ObterResumoContador',
                    endpoint='contador/resumo/',
                    param = {
                "dDataInicio":dDataInicio,
                "dDataFim":dDataFim,

}
                )
            
    def consultar_banco(
            self, codigo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarBanco',
                    endpoint='geral/bancos/',
                    param = {
                "codigo":codigo,

}
                )
            
    def listar_bancos(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Exibe uma lista com os banco cadastrados."""
                return self._chamar_api(
                    call='ListarBancos',
                    endpoint='geral/bancos/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def consultar_tipo_documento(
            self, codigo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarTipoDocumento',
                    endpoint='geral/tiposdoc/',
                    param = {
                "codigo":codigo,

}
                )
            
    def pesquisar_tipo_documento(
            self, codigo
            ) -> dict:
                """Pesquisa o tipo de documento"""
                return self._chamar_api(
                    call='PesquisarTipoDocumento',
                    endpoint='geral/tiposdoc/',
                    param = {
                "codigo":codigo,

}
                )
            
    def listar_tipos_c_c(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar os tipos de contas correntes."""
                return self._chamar_api(
                    call='ListarTiposCC',
                    endpoint='geral/tipocc/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_cadastro_d_r_e(
            self, apenasContasAtivas
            ) -> dict:
                """Lista as contas do DRE"""
                return self._chamar_api(
                    call='ListarCadastroDRE',
                    endpoint='geral/dre/',
                    param = {
                "apenasContasAtivas":apenasContasAtivas,

}
                )
            
    def consultar_final_transf(
            self, banco, codigo
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarFinalTransf',
                    endpoint='geral/finaltransf/',
                    param = {
                "banco":banco,
                "codigo":codigo,

}
                )
            
    def listar_final_transf(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarFinalTransf',
                    endpoint='geral/finaltransf/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def alterar_produto(
            self, codigo_produto_integracao, codigo, descricao, unidade
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarProduto',
                    endpoint='geral/produtos/',
                    param = {
                "codigo_produto_integracao":codigo_produto_integracao,
                "codigo":codigo,
                "descricao":descricao,
                "unidade":unidade,

}
                )
            
    def associar_cod_int_produto(
            self, codigo_produto, codigo_produto_integracao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AssociarCodIntProduto',
                    endpoint='geral/produtos/',
                    param = {
                "codigo_produto":codigo_produto,
                "codigo_produto_integracao":codigo_produto_integracao,

}
                )
            
    def consultar_produto(
            self, codigo_produto, codigo_produto_integracao, codigo
            ) -> dict:
                """Consulta um produto."""
                return self._chamar_api(
                    call='ConsultarProduto',
                    endpoint='geral/produtos/',
                    param = {
                "codigo_produto":codigo_produto,
                "codigo_produto_integracao":codigo_produto_integracao,
                "codigo":codigo,

}
                )
            
    def excluir_produto(
            self, codigo_produto, codigo_produto_integracao, codigo
            ) -> dict:
                """Exclui um produto"""
                return self._chamar_api(
                    call='ExcluirProduto',
                    endpoint='geral/produtos/',
                    param = {
                "codigo_produto":codigo_produto,
                "codigo_produto_integracao":codigo_produto_integracao,
                "codigo":codigo,

}
                )
            
    def incluir_produto(
            self, codigo_produto_integracao, codigo, descricao, unidade
            ) -> dict:
                """Incluir um produto."""
                return self._chamar_api(
                    call='IncluirProduto',
                    endpoint='geral/produtos/',
                    param = {
                "codigo_produto_integracao":codigo_produto_integracao,
                "codigo":codigo,
                "descricao":descricao,
                "unidade":unidade,

}
                )
            
    def incluir_produtos_por_lote(
            self, lote, produto_servico_cadastro
            ) -> dict:
                """DEPRECATED"""
                return self._chamar_api(
                    call='IncluirProdutosPorLote',
                    endpoint='geral/produtos/',
                    param = {
                "lote":lote,
                "produto_servico_cadastro":produto_servico_cadastro,

}
                )
            
    def listar_produtos(
            self, pagina, registros_por_pagina, apenas_importado_api, filtrar_apenas_omiepdv
            ) -> dict:
                """Lista completa do cadastro de produtos"""
                return self._chamar_api(
                    call='ListarProdutos',
                    endpoint='geral/produtos/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,
                "filtrar_apenas_omiepdv":filtrar_apenas_omiepdv,

}
                )
            
    def listar_produtos_resumido(
            self, pagina, registros_por_pagina, apenas_importado_api, filtrar_apenas_omiepdv
            ) -> dict:
                """Lista os produtos cadastrados"""
                return self._chamar_api(
                    call='ListarProdutosResumido',
                    endpoint='geral/produtos/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,
                "filtrar_apenas_omiepdv":filtrar_apenas_omiepdv,

}
                )
            
    def upsert_produto(
            self, codigo_produto_integracao, codigo, descricao, unidade
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='UpsertProduto',
                    endpoint='geral/produtos/',
                    param = {
                "codigo_produto_integracao":codigo_produto_integracao,
                "codigo":codigo,
                "descricao":descricao,
                "unidade":unidade,

}
                )
            
    def upsert_produtos_por_lote(
            self, lote, produto_servico_cadastro
            ) -> dict:
                """DEPRECATED"""
                return self._chamar_api(
                    call='UpsertProdutosPorLote',
                    endpoint='geral/produtos/',
                    param = {
                "lote":lote,
                "produto_servico_cadastro":produto_servico_cadastro,

}
                )
            
    def alterar_caract_produto(
            self, nCodProd, cCodIntProd, nCodCaract, cCodIntCaract, cConteudo, cExibirItemNF, cExibirItemPedido, cExibirOrdemProd
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarCaractProduto',
                    endpoint='geral/prodcaract/',
                    param = {
                "nCodProd":nCodProd,
                "cCodIntProd":cCodIntProd,
                "nCodCaract":nCodCaract,
                "cCodIntCaract":cCodIntCaract,
                "cConteudo":cConteudo,
                "cExibirItemNF":cExibirItemNF,
                "cExibirItemPedido":cExibirItemPedido,
                "cExibirOrdemProd":cExibirOrdemProd,

}
                )
            
    def consultar_caract_produto(
            self, nCodProd, cCodIntProd, nCodCaract, cCodIntCaract
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarCaractProduto',
                    endpoint='geral/prodcaract/',
                    param = {
                "nCodProd":nCodProd,
                "cCodIntProd":cCodIntProd,
                "nCodCaract":nCodCaract,
                "cCodIntCaract":cCodIntCaract,

}
                )
            
    def excluir_caract_produto(
            self, nCodProd, cCodIntProd, nCodCaract, cCodIntCaract
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirCaractProduto',
                    endpoint='geral/prodcaract/',
                    param = {
                "nCodProd":nCodProd,
                "cCodIntProd":cCodIntProd,
                "nCodCaract":nCodCaract,
                "cCodIntCaract":cCodIntCaract,

}
                )
            
    def incluir_caract_produto(
            self, nCodProd, cCodIntProd, nCodCaract, cCodIntCaract, cConteudo, cExibirItemNF, cExibirItemPedido, cExibirOrdemProd
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirCaractProduto',
                    endpoint='geral/prodcaract/',
                    param = {
                "nCodProd":nCodProd,
                "cCodIntProd":cCodIntProd,
                "nCodCaract":nCodCaract,
                "cCodIntCaract":cCodIntCaract,
                "cConteudo":cConteudo,
                "cExibirItemNF":cExibirItemNF,
                "cExibirItemPedido":cExibirItemPedido,
                "cExibirOrdemProd":cExibirOrdemProd,

}
                )
            
    def listar_caract_produto(
            self, nPagina, nRegPorPagina, nCodProd
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarCaractProduto',
                    endpoint='geral/prodcaract/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,
                "nCodProd":nCodProd,

}
                )
            
    def alterar_estrutura(
            self, idProduto, intProduto, itemMalhaAlterar
            ) -> dict:
                """Alterar a estrutura de um produto."""
                return self._chamar_api(
                    call='AlterarEstrutura',
                    endpoint='geral/malha/',
                    param = {
                "idProduto":idProduto,
                "intProduto":intProduto,
                "itemMalhaAlterar":itemMalhaAlterar,

}
                )
            
    def consultar_estrutura(
            self, idProduto, intProduto, codProduto
            ) -> dict:
                """Consulta a estrutura do produto."""
                return self._chamar_api(
                    call='ConsultarEstrutura',
                    endpoint='geral/malha/',
                    param = {
                "idProduto":idProduto,
                "intProduto":intProduto,
                "codProduto":codProduto,

}
                )
            
    def excluir_estrutura(
            self, idProduto, intProduto, idMalha, intMalha
            ) -> dict:
                """Excluir item da estrutura de um produto."""
                return self._chamar_api(
                    call='ExcluirEstrutura',
                    endpoint='geral/malha/',
                    param = {
                "idProduto":idProduto,
                "intProduto":intProduto,
                "idMalha":idMalha,
                "intMalha":intMalha,

}
                )
            
    def incluir_estrutura(
            self, idProduto, intProduto, itemMalhaIncluir
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirEstrutura',
                    endpoint='geral/malha/',
                    param = {
                "idProduto":idProduto,
                "intProduto":intProduto,
                "itemMalhaIncluir":itemMalhaIncluir,

}
                )
            
    def listar_estruturas(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """Lista as estruturas de produtos."""
                return self._chamar_api(
                    call='ListarEstruturas',
                    endpoint='geral/malha/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def alterar_componentes_kit(
            self, codigo_produto, componentes_kit
            ) -> dict:
                """Inclui/Altera/Exclui os componentes do KIT."""
                return self._chamar_api(
                    call='AlterarComponentesKit',
                    endpoint='geral/produtoskit/',
                    param = {
                "codigo_produto":codigo_produto,
                "componentes_kit":componentes_kit,

}
                )
            
    def alterar_req(
            self, codCateg, codIntReqCompra, codProj, codReqCompra, dtSugestao, obsIntReqCompra, obsReqCompra, ItensReqCompra
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarReq',
                    endpoint='produtos/requisicaocompra/',
                    param = {
                "codCateg":codCateg,
                "codIntReqCompra":codIntReqCompra,
                "codProj":codProj,
                "codReqCompra":codReqCompra,
                "dtSugestao":dtSugestao,
                "obsIntReqCompra":obsIntReqCompra,
                "obsReqCompra":obsReqCompra,
                "ItensReqCompra":ItensReqCompra,

}
                )
            
    def consultar_req(
            self, codIntReqCompra, codReqCompra
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarReq',
                    endpoint='produtos/requisicaocompra/',
                    param = {
                "codIntReqCompra":codIntReqCompra,
                "codReqCompra":codReqCompra,

}
                )
            
    def excluir_req(
            self, codIntReqCompra, codReqCompra
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirReq',
                    endpoint='produtos/requisicaocompra/',
                    param = {
                "codIntReqCompra":codIntReqCompra,
                "codReqCompra":codReqCompra,

}
                )
            
    def incluir_req(
            self, codCateg, codIntReqCompra, codProj, codReqCompra, dtSugestao, obsIntReqCompra, obsReqCompra, ItensReqCompra
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirReq',
                    endpoint='produtos/requisicaocompra/',
                    param = {
                "codCateg":codCateg,
                "codIntReqCompra":codIntReqCompra,
                "codProj":codProj,
                "codReqCompra":codReqCompra,
                "dtSugestao":dtSugestao,
                "obsIntReqCompra":obsIntReqCompra,
                "obsReqCompra":obsReqCompra,
                "ItensReqCompra":ItensReqCompra,

}
                )
            
    def pesquisar_req(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='PesquisarReq',
                    endpoint='produtos/requisicaocompra/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def upsert_req(
            self, codCateg, codIntReqCompra, codProj, codReqCompra, dtSugestao, obsIntReqCompra, obsReqCompra, ItensReqCompra
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='UpsertReq',
                    endpoint='produtos/requisicaocompra/',
                    param = {
                "codCateg":codCateg,
                "codIntReqCompra":codIntReqCompra,
                "codProj":codProj,
                "codReqCompra":codReqCompra,
                "dtSugestao":dtSugestao,
                "obsIntReqCompra":obsIntReqCompra,
                "obsReqCompra":obsReqCompra,
                "ItensReqCompra":ItensReqCompra,

}
                )
            
    def altera_ped_compra(
            self, cabecalho_alterar, frete_alterar, departamentos_alterar, produtos_alterar
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlteraPedCompra',
                    endpoint='produtos/pedidocompra/',
                    param = {
                "cabecalho_alterar":cabecalho_alterar,
                "frete_alterar":frete_alterar,
                "departamentos_alterar":departamentos_alterar,
                "produtos_alterar":produtos_alterar,

}
                )
            
    def consultar_ped_compra(
            self, nCodPed, cCodIntPed, cNumero
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarPedCompra',
                    endpoint='produtos/pedidocompra/',
                    param = {
                "nCodPed":nCodPed,
                "cCodIntPed":cCodIntPed,
                "cNumero":cNumero,

}
                )
            
    def excluir_ped_compra(
            self, nCodPed, cCodIntPed
            ) -> dict:
                """Excluir um Pedido de Compra"""
                return self._chamar_api(
                    call='ExcluirPedCompra',
                    endpoint='produtos/pedidocompra/',
                    param = {
                "nCodPed":nCodPed,
                "cCodIntPed":cCodIntPed,

}
                )
            
    def incluir_ped_compra(
            self, cabecalho_incluir, frete_incluir, departamentos_incluir, produtos_incluir
            ) -> dict:
                """Incluir um Pedido de Compra"""
                return self._chamar_api(
                    call='IncluirPedCompra',
                    endpoint='produtos/pedidocompra/',
                    param = {
                "cabecalho_incluir":cabecalho_incluir,
                "frete_incluir":frete_incluir,
                "departamentos_incluir":departamentos_incluir,
                "produtos_incluir":produtos_incluir,

}
                )
            
    def pesquisar_ped_compra(
            self, nPagina, nRegsPorPagina, lApenasImportadoApi, lExibirPedidosPendentes, lExibirPedidosFaturados, lExibirPedidosRecebidos, lExibirPedidosCancelados, lExibirPedidosEncerrados, lExibirPedidosRecParciais, lExibirPedidosFatParciais, dDataInicial, dDataFinal, lApenasAlterados
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='PesquisarPedCompra',
                    endpoint='produtos/pedidocompra/',
                    param = {
                "nPagina":nPagina,
                "nRegsPorPagina":nRegsPorPagina,
                "lApenasImportadoApi":lApenasImportadoApi,
                "lExibirPedidosPendentes":lExibirPedidosPendentes,
                "lExibirPedidosFaturados":lExibirPedidosFaturados,
                "lExibirPedidosRecebidos":lExibirPedidosRecebidos,
                "lExibirPedidosCancelados":lExibirPedidosCancelados,
                "lExibirPedidosEncerrados":lExibirPedidosEncerrados,
                "lExibirPedidosRecParciais":lExibirPedidosRecParciais,
                "lExibirPedidosFatParciais":lExibirPedidosFatParciais,
                "dDataInicial":dDataInicial,
                "dDataFinal":dDataFinal,
                "lApenasAlterados":lApenasAlterados,

}
                )
            
    def upsert_ped_compra(
            self, cabecalho_upsert, frete_upsert, departamentos_upsert, produtos_upsert
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='UpsertPedCompra',
                    endpoint='produtos/pedidocompra/',
                    param = {
                "cabecalho_upsert":cabecalho_upsert,
                "frete_upsert":frete_upsert,
                "departamentos_upsert":departamentos_upsert,
                "produtos_upsert":produtos_upsert,

}
                )
            
    def alterar_ordem_producao(
            self, identificacao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarOrdemProducao',
                    endpoint='produtos/op/',
                    param = {
                "identificacao":identificacao,

}
                )
            
    def concluir_ordem_producao(
            self, cCodIntOP, nCodOP, dDtConclusao, nQtdeProduzida, cObsConclusao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConcluirOrdemProducao',
                    endpoint='produtos/op/',
                    param = {
                "cCodIntOP":cCodIntOP,
                "nCodOP":nCodOP,
                "dDtConclusao":dDtConclusao,
                "nQtdeProduzida":nQtdeProduzida,
                "cObsConclusao":cObsConclusao,

}
                )
            
    def consultar_ordem_producao(
            self, cCodIntOP, nCodOP
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarOrdemProducao',
                    endpoint='produtos/op/',
                    param = {
                "cCodIntOP":cCodIntOP,
                "nCodOP":nCodOP,

}
                )
            
    def excluir_ordem_producao(
            self, cCodIntOP, nCodOP
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirOrdemProducao',
                    endpoint='produtos/op/',
                    param = {
                "cCodIntOP":cCodIntOP,
                "nCodOP":nCodOP,

}
                )
            
    def incluir_ordem_producao(
            self, identificacao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirOrdemProducao',
                    endpoint='produtos/op/',
                    param = {
                "identificacao":identificacao,

}
                )
            
    def listar_ordem_producao(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarOrdemProducao',
                    endpoint='produtos/op/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def reverter_ordem_producao(
            self, cCodIntOP, nCodOP
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ReverterOrdemProducao',
                    endpoint='produtos/op/',
                    param = {
                "cCodIntOP":cCodIntOP,
                "nCodOP":nCodOP,

}
                )
            
    def upsert_ordem_producao(
            self, identificacao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='UpsertOrdemProducao',
                    endpoint='produtos/op/',
                    param = {
                "identificacao":identificacao,

}
                )
            
    def alterar_nota_ent(
            self, cabec, infAdic, produtos
            ) -> dict:
                """Alterar nota de entrada"""
                return self._chamar_api(
                    call='AlterarNotaEnt',
                    endpoint='produtos/notaentrada/',
                    param = {
                "cabec":cabec,
                "infAdic":infAdic,
                "produtos":produtos,

}
                )
            
    def consultar_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
            ) -> dict:
                """Consultar nota de entrada"""
                return self._chamar_api(
                    call='ConsultarNotaEnt',
                    endpoint='produtos/notaentrada/',
                    param = {
                "nCodNotaEnt":nCodNotaEnt,
                "cCodIntNotaEnt":cCodIntNotaEnt,

}
                )
            
    def excluir_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
            ) -> dict:
                """Excluir nota de entrada"""
                return self._chamar_api(
                    call='ExcluirNotaEnt',
                    endpoint='produtos/notaentrada/',
                    param = {
                "nCodNotaEnt":nCodNotaEnt,
                "cCodIntNotaEnt":cCodIntNotaEnt,

}
                )
            
    def incluir_nota_ent(
            self, cabec, infAdic, produtos
            ) -> dict:
                """Incluir nota de entrada"""
                return self._chamar_api(
                    call='IncluirNotaEnt',
                    endpoint='produtos/notaentrada/',
                    param = {
                "cabec":cabec,
                "infAdic":infAdic,
                "produtos":produtos,

}
                )
            
    def listar_nota_ent(
            self, nPagina, nRegistrosPorPagina
            ) -> dict:
                """Listagem de nota de entrada"""
                return self._chamar_api(
                    call='ListarNotaEnt',
                    endpoint='produtos/notaentrada/',
                    param = {
                "nPagina":nPagina,
                "nRegistrosPorPagina":nRegistrosPorPagina,

}
                )
            
    def status_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
            ) -> dict:
                """Status de nota de entrada"""
                return self._chamar_api(
                    call='StatusNotaEnt',
                    endpoint='produtos/notaentrada/',
                    param = {
                "nCodNotaEnt":nCodNotaEnt,
                "cCodIntNotaEnt":cCodIntNotaEnt,

}
                )
            
    def cancelar_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
            ) -> dict:
                """Cancelar nota de entrada"""
                return self._chamar_api(
                    call='CancelarNotaEnt',
                    endpoint='produtos/notaentradafat/',
                    param = {
                "nCodNotaEnt":nCodNotaEnt,
                "cCodIntNotaEnt":cCodIntNotaEnt,

}
                )
            
    def concluir_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
            ) -> dict:
                """Concluir nota de entrada"""
                return self._chamar_api(
                    call='ConcluirNotaEnt',
                    endpoint='produtos/notaentradafat/',
                    param = {
                "nCodNotaEnt":nCodNotaEnt,
                "cCodIntNotaEnt":cCodIntNotaEnt,

}
                )
            
    def conferir_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
            ) -> dict:
                """Conferir nota de entrada"""
                return self._chamar_api(
                    call='ConferirNotaEnt',
                    endpoint='produtos/notaentradafat/',
                    param = {
                "nCodNotaEnt":nCodNotaEnt,
                "cCodIntNotaEnt":cCodIntNotaEnt,

}
                )
            
    def duplicar_nota_ent(
            self, nCodNotaEnt, cCodIntNotaEnt
            ) -> dict:
                """Duplicar nota de entrada"""
                return self._chamar_api(
                    call='DuplicarNotaEnt',
                    endpoint='produtos/notaentradafat/',
                    param = {
                "nCodNotaEnt":nCodNotaEnt,
                "cCodIntNotaEnt":cCodIntNotaEnt,

}
                )
            
    def alterar_etapa_recebimento(
            self, nIdReceb, cChaveNfe, cEtapa
            ) -> dict:
                """Alterar etapa recebimento NFe"""
                return self._chamar_api(
                    call='AlterarEtapaRecebimento',
                    endpoint='produtos/recebimentonfe/',
                    param = {
                "nIdReceb":nIdReceb,
                "cChaveNfe":cChaveNfe,
                "cEtapa":cEtapa,

}
                )
            
    def alterar_recebimento(
            self, ide, itensRecebimentoEditar
            ) -> dict:
                """Alterar recebimento de NFe"""
                return self._chamar_api(
                    call='AlterarRecebimento',
                    endpoint='produtos/recebimentonfe/',
                    param = {
                "ide":ide,
                "itensRecebimentoEditar":itensRecebimentoEditar,

}
                )
            
    def concluir_recebimento(
            self, nIdReceb, cChaveNfe, cEtapa
            ) -> dict:
                """Concluir recebimento de NFe"""
                return self._chamar_api(
                    call='ConcluirRecebimento',
                    endpoint='produtos/recebimentonfe/',
                    param = {
                "nIdReceb":nIdReceb,
                "cChaveNfe":cChaveNfe,
                "cEtapa":cEtapa,

}
                )
            
    def consultar_recebimento(
            self, nIdReceb, cChaveNfe
            ) -> dict:
                """Consultar recebimento de NFe"""
                return self._chamar_api(
                    call='ConsultarRecebimento',
                    endpoint='produtos/recebimentonfe/',
                    param = {
                "nIdReceb":nIdReceb,
                "cChaveNfe":cChaveNfe,

}
                )
            
    def listar_recebimentos(
            self, nPagina, nRegistrosPorPagina
            ) -> dict:
                """Listar recebimento de NFe"""
                return self._chamar_api(
                    call='ListarRecebimentos',
                    endpoint='produtos/recebimentonfe/',
                    param = {
                "nPagina":nPagina,
                "nRegistrosPorPagina":nRegistrosPorPagina,

}
                )
            
    def reverter_recebimento(
            self, nIdReceb, cChaveNfe, cEtapa
            ) -> dict:
                """Reverter recebimento NFe"""
                return self._chamar_api(
                    call='ReverterRecebimento',
                    endpoint='produtos/recebimentonfe/',
                    param = {
                "nIdReceb":nIdReceb,
                "cChaveNfe":cChaveNfe,
                "cEtapa":cEtapa,

}
                )
            
    def alterar_familia(
            self, codigo, codInt, codFamilia, nomeFamilia, inativo
            ) -> dict:
                """Altera uma familia de produto"""
                return self._chamar_api(
                    call='AlterarFamilia',
                    endpoint='geral/familias/',
                    param = {
                "codigo":codigo,
                "codInt":codInt,
                "codFamilia":codFamilia,
                "nomeFamilia":nomeFamilia,
                "inativo":inativo,

}
                )
            
    def consultar_familia(
            self, codigo, codInt
            ) -> dict:
                """Consulta uma familia de produto"""
                return self._chamar_api(
                    call='ConsultarFamilia',
                    endpoint='geral/familias/',
                    param = {
                "codigo":codigo,
                "codInt":codInt,

}
                )
            
    def excluir_familia(
            self, codigo, codInt
            ) -> dict:
                """Exclui uma familia de produto"""
                return self._chamar_api(
                    call='ExcluirFamilia',
                    endpoint='geral/familias/',
                    param = {
                "codigo":codigo,
                "codInt":codInt,

}
                )
            
    def incluir_familia(
            self, codInt, codFamilia, nomeFamilia, inativo
            ) -> dict:
                """Inclui uma familia de produto"""
                return self._chamar_api(
                    call='IncluirFamilia',
                    endpoint='geral/familias/',
                    param = {
                "codInt":codInt,
                "codFamilia":codFamilia,
                "nomeFamilia":nomeFamilia,
                "inativo":inativo,

}
                )
            
    def pesquisar_familias(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listagem de familias cadastradas"""
                return self._chamar_api(
                    call='PesquisarFamilias',
                    endpoint='geral/familias/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def upsert_familia(
            self, codigo, codInt, codFamilia, nomeFamilia, inativo
            ) -> dict:
                """Inclui / Altera uma familia de produto"""
                return self._chamar_api(
                    call='UpsertFamilia',
                    endpoint='geral/familias/',
                    param = {
                "codigo":codigo,
                "codInt":codInt,
                "codFamilia":codFamilia,
                "nomeFamilia":nomeFamilia,
                "inativo":inativo,

}
                )
            
    def listar_unidades(
            self, codigo
            ) -> dict:
                """Lista as unidades de medidas"""
                return self._chamar_api(
                    call='ListarUnidades',
                    endpoint='geral/unidade/',
                    param = {
                "codigo":codigo,

}
                )
            
    def listar_compradores(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista os compradores cadastrados."""
                return self._chamar_api(
                    call='ListarCompradores',
                    endpoint='estoque/comprador/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_produto_fornecedor(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar os produtos por fornecedores."""
                return self._chamar_api(
                    call='ListarProdutoFornecedor',
                    endpoint='estoque/produtofornecedor/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_formas_pag_vendas(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista as formas de pagmento de vendas."""
                return self._chamar_api(
                    call='ListarFormasPagVendas',
                    endpoint='produtos/formaspagvendas/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def consultar_n_c_m(
            self, cCodigo
            ) -> dict:
                """Consulta um NCM"""
                return self._chamar_api(
                    call='ConsultarNCM',
                    endpoint='produtos/ncm/',
                    param = {
                "cCodigo":cCodigo,

}
                )
            
    def listar_n_c_m(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """Lista os NCMs cadastrados."""
                return self._chamar_api(
                    call='ListarNCM',
                    endpoint='produtos/ncm/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def listar_cenarios(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarCenarios',
                    endpoint='geral/cenarios/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def listar_impostos_cenario(
            self, codigo_cliente_integracao, consumo_final, codigo_produto_integracao, codigo_cenario
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarImpostosCenario',
                    endpoint='geral/cenarios/',
                    param = {
                "codigo_cliente_integracao":codigo_cliente_integracao,
                "consumo_final":consumo_final,
                "codigo_produto_integracao":codigo_produto_integracao,
                "codigo_cenario":codigo_cenario,

}
                )
            
    def listar_c_f_o_p(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar as CFOPs"""
                return self._chamar_api(
                    call='ListarCFOP',
                    endpoint='produtos/cfop/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_c_s_t(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar os CSTs do ICMS"""
                return self._chamar_api(
                    call='ListarCST',
                    endpoint='produtos/icmscst/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_c_s_o_s_n(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar os CSOSN do ICMS."""
                return self._chamar_api(
                    call='ListarCSOSN',
                    endpoint='produtos/icmscsosn/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_orig_merc(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar a origem da mercadoria do ICMS."""
                return self._chamar_api(
                    call='ListarOrigMerc',
                    endpoint='produtos/icmsorigem/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_cst_pis(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar o CST do PIS."""
                return self._chamar_api(
                    call='ListarCstPis',
                    endpoint='produtos/piscst/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_cst_cofins(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar CST do COFINS."""
                return self._chamar_api(
                    call='ListarCstCofins',
                    endpoint='produtos/cofinscst/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_cst_ipi(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar CST do IPI."""
                return self._chamar_api(
                    call='ListarCstIpi',
                    endpoint='produtos/ipicst/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_enq_ipi(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar Enquadramento do IPI."""
                return self._chamar_api(
                    call='ListarEnqIpi',
                    endpoint='produtos/ipienq/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_tp_calc(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarTpCalc',
                    endpoint='produtos/tpcalc/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_c_e_s_t(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Listar CEST."""
                return self._chamar_api(
                    call='ListarCEST',
                    endpoint='produtos/cest/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def alterar_estoque_minimo(
            self, codigo_local_estoque, id_prod, cod_int, quan_min
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarEstoqueMinimo',
                    endpoint='estoque/ajuste/',
                    param = {
                "codigo_local_estoque":codigo_local_estoque,
                "id_prod":id_prod,
                "cod_int":cod_int,
                "quan_min":quan_min,

}
                )
            
    def excluir_ajuste_estoque(
            self, id_ajuste
            ) -> dict:
                """Excluir um Movimento de Ajuste de Estoque"""
                return self._chamar_api(
                    call='ExcluirAjusteEstoque',
                    endpoint='estoque/ajuste/',
                    param = {
                "id_ajuste":id_ajuste,

}
                )
            
    def incluir_ajuste_estoque(
            self, codigo_local_estoque, id_prod, data, quan, obs, origem, tipo, motivo, valor
            ) -> dict:
                """Incluir um Ajuste de Estoque"""
                return self._chamar_api(
                    call='IncluirAjusteEstoque',
                    endpoint='estoque/ajuste/',
                    param = {
                "codigo_local_estoque":codigo_local_estoque,
                "id_prod":id_prod,
                "data":data,
                "quan":quan,
                "obs":obs,
                "origem":origem,
                "tipo":tipo,
                "motivo":motivo,
                "valor":valor,

}
                )
            
    def listar_ajuste_estoque(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Listar os ajuste de estoque."""
                return self._chamar_api(
                    call='ListarAjusteEstoque',
                    endpoint='estoque/ajuste/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def listar_movimento_estoque(
            self, nPagina, nRegPorPagina, codigo_local_estoque, idProd, dDtInicial, dDtFinal, lista_local_estoque
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarMovimentoEstoque',
                    endpoint='estoque/consulta/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,
                "codigo_local_estoque":codigo_local_estoque,
                "idProd":idProd,
                "dDtInicial":dDtInicial,
                "dDtFinal":dDtFinal,
                "lista_local_estoque":lista_local_estoque,

}
                )
            
    def listar_pos_estoque(
            self, nPagina, nRegPorPagina, dDataPosicao, cExibeTodos, codigo_local_estoque
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarPosEstoque',
                    endpoint='estoque/consulta/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,
                "dDataPosicao":dDataPosicao,
                "cExibeTodos":cExibeTodos,
                "codigo_local_estoque":codigo_local_estoque,

}
                )
            
    def listar_saldo_pendente(
            self, pagina, registros_por_pagina, codigo_local_estoque, id_prod, tipo
            ) -> dict:
                """Lista o saldo pendente de estoque."""
                return self._chamar_api(
                    call='ListarSaldoPendente',
                    endpoint='estoque/consulta/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "codigo_local_estoque":codigo_local_estoque,
                "id_prod":id_prod,
                "tipo":tipo,

}
                )
            
    def movimento_estoque(
            self, codigo_local_estoque, id_prod, cod_int, dataInicial, dataFinal
            ) -> dict:
                """Consulta do Movimento de Estoque"""
                return self._chamar_api(
                    call='MovimentoEstoque',
                    endpoint='estoque/consulta/',
                    param = {
                "codigo_local_estoque":codigo_local_estoque,
                "id_prod":id_prod,
                "cod_int":cod_int,
                "dataInicial":dataInicial,
                "dataFinal":dataFinal,

}
                )
            
    def posicao_estoque(
            self, codigo_local_estoque, id_prod, cod_int, data
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='PosicaoEstoque',
                    endpoint='estoque/consulta/',
                    param = {
                "codigo_local_estoque":codigo_local_estoque,
                "id_prod":id_prod,
                "cod_int":cod_int,
                "data":data,

}
                )
            
    def consultar_previsao(
            self, nCodProd
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarPrevisao',
                    endpoint='estoque/movestoque/',
                    param = {
                "nCodProd":nCodProd,

}
                )
            
    def listar_movimentos(
            self, pagina, registros_por_pagina, codigo_local_estoque
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarMovimentos',
                    endpoint='estoque/movestoque/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "codigo_local_estoque":codigo_local_estoque,

}
                )
            
    def listar_locais_estoque(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """Lista os Locais de Estoque encontrados."""
                return self._chamar_api(
                    call='ListarLocaisEstoque',
                    endpoint='estoque/local/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def obter_estoque_produto(
            self, cEAN, nIdProduto, cCodigo, dDia
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ObterEstoqueProduto',
                    endpoint='estoque/resumo/',
                    param = {
                "cEAN":cEAN,
                "nIdProduto":nIdProduto,
                "cCodigo":cCodigo,
                "dDia":dDia,

}
                )
            
    def alterar_ped_faturado(
            self, codigo_pedido, codigo_pedido_integracao, codigo_rastreio, previsao_entrega, obs_venda
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarPedFaturado',
                    endpoint='produtos/pedido/',
                    param = {
                "codigo_pedido":codigo_pedido,
                "codigo_pedido_integracao":codigo_pedido_integracao,
                "codigo_rastreio":codigo_rastreio,
                "previsao_entrega":previsao_entrega,
                "obs_venda":obs_venda,

}
                )
            
    def alterar_pedido_venda(
            self, cabecalho, det, informacoes_adicionais, lista_parcelas, total_pedido
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarPedidoVenda',
                    endpoint='produtos/pedido/',
                    param = {
                "cabecalho":cabecalho,
                "det":det,
                "informacoes_adicionais":informacoes_adicionais,
                "lista_parcelas":lista_parcelas,
                "total_pedido":total_pedido,

}
                )
            
    def consultar_pedido(
            self, codigo_pedido
            ) -> dict:
                """Consulta de Pedido de Venda de Produto"""
                return self._chamar_api(
                    call='ConsultarPedido',
                    endpoint='produtos/pedido/',
                    param = {
                "codigo_pedido":codigo_pedido,

}
                )
            
    def excluir_pedido(
            self, codigo_pedido, codigo_pedido_integracao
            ) -> dict:
                """Excluir pedido de venda de produto"""
                return self._chamar_api(
                    call='ExcluirPedido',
                    endpoint='produtos/pedido/',
                    param = {
                "codigo_pedido":codigo_pedido,
                "codigo_pedido_integracao":codigo_pedido_integracao,

}
                )
            
    def incluir_pedido(
            self, cabecalho, det, frete, informacoes_adicionais, lista_parcelas
            ) -> dict:
                """Inclui um pedido de venda de produto"""
                return self._chamar_api(
                    call='IncluirPedido',
                    endpoint='produtos/pedido/',
                    param = {
                "cabecalho":cabecalho,
                "det":det,
                "frete":frete,
                "informacoes_adicionais":informacoes_adicionais,
                "lista_parcelas":lista_parcelas,

}
                )
            
    def listar_pedidos(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Listar os pedidos de venda de produto"""
                return self._chamar_api(
                    call='ListarPedidos',
                    endpoint='produtos/pedido/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def simular_impostos(
            self, codigo_cliente, consumidor_final, frete_simul, det_simul
            ) -> dict:
                """Simula os impostos de um pedido de venda."""
                return self._chamar_api(
                    call='SimularImpostos',
                    endpoint='produtos/pedido/',
                    param = {
                "codigo_cliente":codigo_cliente,
                "consumidor_final":consumidor_final,
                "frete_simul":frete_simul,
                "det_simul":det_simul,

}
                )
            
    def status_pedido(
            self, codigo_pedido, codigo_pedido_integracao
            ) -> dict:
                """Consulta do Status do Pedido"""
                return self._chamar_api(
                    call='StatusPedido',
                    endpoint='produtos/pedido/',
                    param = {
                "codigo_pedido":codigo_pedido,
                "codigo_pedido_integracao":codigo_pedido_integracao,

}
                )
            
    def trocar_etapa_pedido(
            self, codigo_pedido, codigo_pedido_integracao, etapa
            ) -> dict:
                """Troca etapa do pedido."""
                return self._chamar_api(
                    call='TrocarEtapaPedido',
                    endpoint='produtos/pedido/',
                    param = {
                "codigo_pedido":codigo_pedido,
                "codigo_pedido_integracao":codigo_pedido_integracao,
                "etapa":etapa,

}
                )
            
    def associar_cod_int_pedido_venda(
            self, cCodIntPed, nCodPed
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AssociarCodIntPedidoVenda',
                    endpoint='produtos/pedidovendafat/',
                    param = {
                "cCodIntPed":cCodIntPed,
                "nCodPed":nCodPed,

}
                )
            
    def cancelar_pedido_venda(
            self, cCodIntPed, nCodPed
            ) -> dict:
                """Cancela um pedido de venda de produto."""
                return self._chamar_api(
                    call='CancelarPedidoVenda',
                    endpoint='produtos/pedidovendafat/',
                    param = {
                "cCodIntPed":cCodIntPed,
                "nCodPed":nCodPed,

}
                )
            
    def duplicar_pedido_venda(
            self, cCodIntPed, nCodPed
            ) -> dict:
                """Duplica um pedido de venda de produto."""
                return self._chamar_api(
                    call='DuplicarPedidoVenda',
                    endpoint='produtos/pedidovendafat/',
                    param = {
                "cCodIntPed":cCodIntPed,
                "nCodPed":nCodPed,

}
                )
            
    def faturar_pedido_venda(
            self, cCodIntPed, nCodPed
            ) -> dict:
                """Fatura um pedido de venda de produto."""
                return self._chamar_api(
                    call='FaturarPedidoVenda',
                    endpoint='produtos/pedidovendafat/',
                    param = {
                "cCodIntPed":cCodIntPed,
                "nCodPed":nCodPed,

}
                )
            
    def obter_pedidos_venda(
            self, cEtapa
            ) -> dict:
                """Retorna a lista de pedidos de venda a serem faturados."""
                return self._chamar_api(
                    call='ObterPedidosVenda',
                    endpoint='produtos/pedidovendafat/',
                    param = {
                "cEtapa":cEtapa,

}
                )
            
    def validar_pedido_venda(
            self, cCodIntPed, nCodPed
            ) -> dict:
                """Valida um pedido de venda de produto para faturamento."""
                return self._chamar_api(
                    call='ValidarPedidoVenda',
                    endpoint='produtos/pedidovendafat/',
                    param = {
                "cCodIntPed":cCodIntPed,
                "nCodPed":nCodPed,

}
                )
            
    def listar_etapas_pedido(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """Lista as etapas do Pedido de Venda de Produtos."""
                return self._chamar_api(
                    call='ListarEtapasPedido',
                    endpoint='produtos/pedidoetapas/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def averbacao_c_te(
            self, cAppNome, cAppVersao, cAppId, cChaveCte, cXmlCteAverb, cMd5CteAverb
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AverbacaoCTe',
                    endpoint='produtos/cte/',
                    param = {
                "cAppNome":cAppNome,
                "cAppVersao":cAppVersao,
                "cAppId":cAppId,
                "cChaveCte":cChaveCte,
                "cXmlCteAverb":cXmlCteAverb,
                "cMd5CteAverb":cMd5CteAverb,

}
                )
            
    def cancelar_c_te(
            self, cAppNome, cAppVersao, cAppId, cChaveCte, cXmlCteCanc, cMd5CteCanc
            ) -> dict:
                """Cancela um CT-e."""
                return self._chamar_api(
                    call='CancelarCTe',
                    endpoint='produtos/cte/',
                    param = {
                "cAppNome":cAppNome,
                "cAppVersao":cAppVersao,
                "cAppId":cAppId,
                "cChaveCte":cChaveCte,
                "cXmlCteCanc":cXmlCteCanc,
                "cMd5CteCanc":cMd5CteCanc,

}
                )
            
    def carta_correcao_c_te(
            self, cAppNome, cAppVersao, cAppId, cChaveCte, cXmlCteCC, cMd5CteCC
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='CartaCorrecaoCTe',
                    endpoint='produtos/cte/',
                    param = {
                "cAppNome":cAppNome,
                "cAppVersao":cAppVersao,
                "cAppId":cAppId,
                "cChaveCte":cChaveCte,
                "cXmlCteCC":cXmlCteCC,
                "cMd5CteCC":cMd5CteCC,

}
                )
            
    def excluir_fatura_c_te(
            self, cAppNome, cAppVersao, cAppId, nIdFaturamento
            ) -> dict:
                """Exclui uma fatura de um grupo de CT-es."""
                return self._chamar_api(
                    call='ExcluirFaturaCTe',
                    endpoint='produtos/cte/',
                    param = {
                "cAppNome":cAppNome,
                "cAppVersao":cAppVersao,
                "cAppId":cAppId,
                "nIdFaturamento":nIdFaturamento,

}
                )
            
    def faturar_c_te(
            self, cAppNome, cAppVersao, cAppId, CNPJCliente, cCategoria, nContaCorrente, dVencimento, nValorFatura, itensFatura
            ) -> dict:
                """Gera uma fatura para um grupo de CT-es."""
                return self._chamar_api(
                    call='FaturarCTe',
                    endpoint='produtos/cte/',
                    param = {
                "cAppNome":cAppNome,
                "cAppVersao":cAppVersao,
                "cAppId":cAppId,
                "CNPJCliente":CNPJCliente,
                "cCategoria":cCategoria,
                "nContaCorrente":nContaCorrente,
                "dVencimento":dVencimento,
                "nValorFatura":nValorFatura,
                "itensFatura":itensFatura,

}
                )
            
    def faturar_lote_c_te(
            self, cAppNome, cAppVersao, cAppId, nIdFaturamento, CNPJCliente, cConcluirFatura, itensFatura
            ) -> dict:
                """Gera uma fatura por lote para um grupo de CT-es."""
                return self._chamar_api(
                    call='FaturarLoteCTe',
                    endpoint='produtos/cte/',
                    param = {
                "cAppNome":cAppNome,
                "cAppVersao":cAppVersao,
                "cAppId":cAppId,
                "nIdFaturamento":nIdFaturamento,
                "CNPJCliente":CNPJCliente,
                "cConcluirFatura":cConcluirFatura,
                "itensFatura":itensFatura,

}
                )
            
    def importar_c_te(
            self, cAppNome, cAppVersao, cAppId, cChaveCte, cXmlCte, cMd5Cte, cCategoria, nContaCorrente
            ) -> dict:
                """Importar o XML de um CT-e."""
                return self._chamar_api(
                    call='ImportarCTe',
                    endpoint='produtos/cte/',
                    param = {
                "cAppNome":cAppNome,
                "cAppVersao":cAppVersao,
                "cAppId":cAppId,
                "cChaveCte":cChaveCte,
                "cXmlCte":cXmlCte,
                "cMd5Cte":cMd5Cte,
                "cCategoria":cCategoria,
                "nContaCorrente":nContaCorrente,

}
                )
            
    def listar_n_fe_transp(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarNFeTransp',
                    endpoint='produtos/cte/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def status_fatura(
            self, cAppNome, cAppVersao, cAppId, nIdFaturamento
            ) -> dict:
                """Retorna o Status da Fatura inclusa."""
                return self._chamar_api(
                    call='StatusFatura',
                    endpoint='produtos/cte/',
                    param = {
                "cAppNome":cAppNome,
                "cAppVersao":cAppVersao,
                "cAppId":cAppId,
                "nIdFaturamento":nIdFaturamento,

}
                )
            
    def alterar_remessa(
            self, cabec, email, frete, infAdic, obs, produtos
            ) -> dict:
                """Altera uma remessa"""
                return self._chamar_api(
                    call='AlterarRemessa',
                    endpoint='produtos/remessa/',
                    param = {
                "cabec":cabec,
                "email":email,
                "frete":frete,
                "infAdic":infAdic,
                "obs":obs,
                "produtos":produtos,

}
                )
            
    def consultar_remessa(
            self, nCodRem, cCodIntRem
            ) -> dict:
                """Consulta uma remessa."""
                return self._chamar_api(
                    call='ConsultarRemessa',
                    endpoint='produtos/remessa/',
                    param = {
                "nCodRem":nCodRem,
                "cCodIntRem":cCodIntRem,

}
                )
            
    def incluir_remessa(
            self, cabec, email, frete, infAdic, obs, produtos
            ) -> dict:
                """Inclui uma nova remessa"""
                return self._chamar_api(
                    call='IncluirRemessa',
                    endpoint='produtos/remessa/',
                    param = {
                "cabec":cabec,
                "email":email,
                "frete":frete,
                "infAdic":infAdic,
                "obs":obs,
                "produtos":produtos,

}
                )
            
    def listar_remessas(
            self, nPagina
            ) -> dict:
                """Lista as remessas cadastradas."""
                return self._chamar_api(
                    call='ListarRemessas',
                    endpoint='produtos/remessa/',
                    param = {
                "nPagina":nPagina,

}
                )
            
    def status_remessa(
            self, nCodRem, cCodIntRem
            ) -> dict:
                """Retorna o status da remessa"""
                return self._chamar_api(
                    call='StatusRemessa',
                    endpoint='produtos/remessa/',
                    param = {
                "nCodRem":nCodRem,
                "cCodIntRem":cCodIntRem,

}
                )
            
    def cancelar_remessa(
            self, nCodRem, cCodIntRem
            ) -> dict:
                """Cancelar remessa de produto"""
                return self._chamar_api(
                    call='CancelarRemessa',
                    endpoint='produtos/remessafat/',
                    param = {
                "nCodRem":nCodRem,
                "cCodIntRem":cCodIntRem,

}
                )
            
    def concluir_remessa(
            self, nCodRem, cCodIntRem
            ) -> dict:
                """Concluir remessa de produto"""
                return self._chamar_api(
                    call='ConcluirRemessa',
                    endpoint='produtos/remessafat/',
                    param = {
                "nCodRem":nCodRem,
                "cCodIntRem":cCodIntRem,

}
                )
            
    def conferir_remessa(
            self, nCodRem, cCodIntRem
            ) -> dict:
                """Conferir remessa de produto"""
                return self._chamar_api(
                    call='ConferirRemessa',
                    endpoint='produtos/remessafat/',
                    param = {
                "nCodRem":nCodRem,
                "cCodIntRem":cCodIntRem,

}
                )
            
    def duplicar_remessa(
            self, nCodRem, cCodIntRem
            ) -> dict:
                """Duplicar remessa de produto"""
                return self._chamar_api(
                    call='DuplicarRemessa',
                    endpoint='produtos/remessafat/',
                    param = {
                "nCodRem":nCodRem,
                "cCodIntRem":cCodIntRem,

}
                )
            
    def fechar_caixa(
            self, emissor, seqCaixa
            ) -> dict:
                """Efetua o fechamento de um determinado caixa."""
                return self._chamar_api(
                    call='FecharCaixa',
                    endpoint='produtos/cupomfiscalincluir/',
                    param = {
                "emissor":emissor,
                "seqCaixa":seqCaixa,

}
                )
            
    def inutilizar_nfce(
            self, emissor, nfceInut
            ) -> dict:
                """Inutiliza um lote de NFC-e."""
                return self._chamar_api(
                    call='InutilizarNfce',
                    endpoint='produtos/cupomfiscalincluir/',
                    param = {
                "emissor":emissor,
                "nfceInut":nfceInut,

}
                )
            
    def cancelar_cupom(
            self, nIdCupom
            ) -> dict:
                """Cancela um cupom Fiscal"""
                return self._chamar_api(
                    call='CancelarCupom',
                    endpoint='produtos/cupomfiscal/',
                    param = {
                "nIdCupom":nIdCupom,

}
                )
            
    def cancelar_n_f_c_e(
            self, nCodigoPDV, nNumeroCaixa, cDataEmissao, IdenticacaoNFCE, DadosCancNFCE
            ) -> dict:
                """Cancelar NFC-e."""
                return self._chamar_api(
                    call='CancelarNFCE',
                    endpoint='produtos/cupomfiscal/',
                    param = {
                "nCodigoPDV":nCodigoPDV,
                "nNumeroCaixa":nNumeroCaixa,
                "cDataEmissao":cDataEmissao,
                "IdenticacaoNFCE":IdenticacaoNFCE,
                "DadosCancNFCE":DadosCancNFCE,

}
                )
            
    def cancelar_s_a_t(
            self, nCodigoPDV, nNumeroCaixa, cDataEmissao, IdenticacaoSAT, DadosCancSAT
            ) -> dict:
                """Cancelar CF-e-SAT."""
                return self._chamar_api(
                    call='CancelarSAT',
                    endpoint='produtos/cupomfiscal/',
                    param = {
                "nCodigoPDV":nCodigoPDV,
                "nNumeroCaixa":nNumeroCaixa,
                "cDataEmissao":cDataEmissao,
                "IdenticacaoSAT":IdenticacaoSAT,
                "DadosCancSAT":DadosCancSAT,

}
                )
            
    def excluir_cupom(
            self, nIdCupom
            ) -> dict:
                """Exclui um Cupom Fiscal."""
                return self._chamar_api(
                    call='ExcluirCupom',
                    endpoint='produtos/cupomfiscal/',
                    param = {
                "nIdCupom":nIdCupom,

}
                )
            
    def excluir_cupons_por_numero(
            self, nCodigoPDV, nNumeroCaixa, cDataEmissao, nNumCupom
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirCuponsPorNumero',
                    endpoint='produtos/cupomfiscal/',
                    param = {
                "nCodigoPDV":nCodigoPDV,
                "nNumeroCaixa":nNumeroCaixa,
                "cDataEmissao":cDataEmissao,
                "nNumCupom":nNumCupom,

}
                )
            
    def excluir_lote(
            self, nNumLote
            ) -> dict:
                """Excluir o lote"""
                return self._chamar_api(
                    call='ExcluirLote',
                    endpoint='produtos/cupomfiscal/',
                    param = {
                "nNumLote":nNumLote,

}
                )
            
    def listar_cupons(
            self, nPagina, nRegPorPagina, dDtEmisInicial, dDtEmisFinal
            ) -> dict:
                """Lista os Cupons Fiscais."""
                return self._chamar_api(
                    call='ListarCupons',
                    endpoint='produtos/cupomfiscal/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,
                "dDtEmisInicial":dDtEmisInicial,
                "dDtEmisFinal":dDtEmisFinal,

}
                )
            
    def obter_proximo_lote(
            self, nCodigoPDV
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ObterProximoLote',
                    endpoint='produtos/cupomfiscal/',
                    param = {
                "nCodigoPDV":nCodigoPDV,

}
                )
            
    def cupons_fiscais(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """Listagem dos cupons fiscais."""
                return self._chamar_api(
                    call='CuponsFiscais',
                    endpoint='produtos/cupomfiscalconsultar/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def cupons_itens(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """Listagem dos itens dos cupons fiscais"""
                return self._chamar_api(
                    call='CuponsItens',
                    endpoint='produtos/cupomfiscalconsultar/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def cupons_pagamentos(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """Listagem dos pagamentos dos cupons fiscais"""
                return self._chamar_api(
                    call='CuponsPagamentos',
                    endpoint='produtos/cupomfiscalconsultar/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def importar_n_f_ce(
            self, emiNome, emiVersao, emiId, chNFe, nfceXml, nfceMd5, cAcaoCliente, idCliente, idVendedor, idProjeto, idLocalEstoque, cNaoMovEstoque, cNaoGerarTitulo, cIncluirProduto
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ImportarNFCe',
                    endpoint='produtos/nfce/',
                    param = {
                "emiNome":emiNome,
                "emiVersao":emiVersao,
                "emiId":emiId,
                "chNFe":chNFe,
                "nfceXml":nfceXml,
                "nfceMd5":nfceMd5,
                "cAcaoCliente":cAcaoCliente,
                "idCliente":idCliente,
                "idVendedor":idVendedor,
                "idProjeto":idProjeto,
                "idLocalEstoque":idLocalEstoque,
                "cNaoMovEstoque":cNaoMovEstoque,
                "cNaoGerarTitulo":cNaoGerarTitulo,
                "cIncluirProduto":cIncluirProduto,

}
                )
            
    def importar_cfe_sat(
            self, emiNome, emiVersao, emiId, chNFe, satXml, satMd5, cAcaoCliente, idCliente, idVendedor, idProjeto, idLocalEstoque, cNaoMovEstoque, cNaoGerarTitulo, cIncluirProduto
            ) -> dict:
                """Importa o XML de um CF-e SAT."""
                return self._chamar_api(
                    call='ImportarCfeSat',
                    endpoint='produtos/sat/',
                    param = {
                "emiNome":emiNome,
                "emiVersao":emiVersao,
                "emiId":emiId,
                "chNFe":chNFe,
                "satXml":satXml,
                "satMd5":satMd5,
                "cAcaoCliente":cAcaoCliente,
                "idCliente":idCliente,
                "idVendedor":idVendedor,
                "idProjeto":idProjeto,
                "idLocalEstoque":idLocalEstoque,
                "cNaoMovEstoque":cNaoMovEstoque,
                "cNaoGerarTitulo":cNaoGerarTitulo,
                "cIncluirProduto":cIncluirProduto,

}
                )
            
    def alterar_preco_item(
            self, nCodTabPreco, nCodProd, nValorTabela
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarPrecoItem',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "nCodTabPreco":nCodTabPreco,
                "nCodProd":nCodProd,
                "nValorTabela":nValorTabela,

}
                )
            
    def alterar_tabela_preco(
            self, nCodTabPreco, cCodIntTabPreco, cNome, cCodigo, cOrigem, produtos, clientes, outrasInfo, caracteristicas
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarTabelaPreco',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "nCodTabPreco":nCodTabPreco,
                "cCodIntTabPreco":cCodIntTabPreco,
                "cNome":cNome,
                "cCodigo":cCodigo,
                "cOrigem":cOrigem,
                "produtos":produtos,
                "clientes":clientes,
                "outrasInfo":outrasInfo,
                "caracteristicas":caracteristicas,

}
                )
            
    def ativar_tabela_preco(
            self, nCodTabPreco, cCodIntTabPreco
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AtivarTabelaPreco',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "nCodTabPreco":nCodTabPreco,
                "cCodIntTabPreco":cCodIntTabPreco,

}
                )
            
    def atualizar_produtos(
            self, nCodTabPreco, cCodIntTabPreco
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AtualizarProdutos',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "nCodTabPreco":nCodTabPreco,
                "cCodIntTabPreco":cCodIntTabPreco,

}
                )
            
    def consultar_tabela_preco(
            self, nCodTabPreco, cCodIntTabPreco
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarTabelaPreco',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "nCodTabPreco":nCodTabPreco,
                "cCodIntTabPreco":cCodIntTabPreco,

}
                )
            
    def excluir_tabela_preco(
            self, nCodTabPreco, cCodIntTabPreco
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirTabelaPreco',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "nCodTabPreco":nCodTabPreco,
                "cCodIntTabPreco":cCodIntTabPreco,

}
                )
            
    def incluir_tabela_preco(
            self, cCodIntTabPreco, cNome, cCodigo, cOrigem, produtos, clientes, outrasInfo, caracteristicas
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirTabelaPreco',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "cCodIntTabPreco":cCodIntTabPreco,
                "cNome":cNome,
                "cCodigo":cCodigo,
                "cOrigem":cOrigem,
                "produtos":produtos,
                "clientes":clientes,
                "outrasInfo":outrasInfo,
                "caracteristicas":caracteristicas,

}
                )
            
    def listar_tabela_itens(
            self, nPagina, nRegPorPagina, nCodTabPreco, cCodIntTabPreco
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarTabelaItens',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,
                "nCodTabPreco":nCodTabPreco,
                "cCodIntTabPreco":cCodIntTabPreco,

}
                )
            
    def listar_tabelas_preco(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarTabelasPreco',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def suspender_tabela_preco(
            self, nCodTabPreco, cCodIntTabPreco
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='SuspenderTabelaPreco',
                    endpoint='produtos/tabelaprecos/',
                    param = {
                "nCodTabPreco":nCodTabPreco,
                "cCodIntTabPreco":cCodIntTabPreco,

}
                )
            
    def alterar_caracteristica(
            self, nCodCaract, cCodIntCaract, cNomeCaract
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarCaracteristica',
                    endpoint='geral/caracteristicas/',
                    param = {
                "nCodCaract":nCodCaract,
                "cCodIntCaract":cCodIntCaract,
                "cNomeCaract":cNomeCaract,

}
                )
            
    def consultar_caracteristica(
            self, nCodCaract, cCodIntCaract
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarCaracteristica',
                    endpoint='geral/caracteristicas/',
                    param = {
                "nCodCaract":nCodCaract,
                "cCodIntCaract":cCodIntCaract,

}
                )
            
    def excluir_caracteristica(
            self, nCodCaract, cCodIntCaract
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirCaracteristica',
                    endpoint='geral/caracteristicas/',
                    param = {
                "nCodCaract":nCodCaract,
                "cCodIntCaract":cCodIntCaract,

}
                )
            
    def incluir_caracteristica(
            self, cCodIntCaract, cNomeCaract
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirCaracteristica',
                    endpoint='geral/caracteristicas/',
                    param = {
                "cCodIntCaract":cCodIntCaract,
                "cNomeCaract":cNomeCaract,

}
                )
            
    def listar_caracteristicas(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarCaracteristicas',
                    endpoint='geral/caracteristicas/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def listar_etapas_faturamento(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista as etapas do faturamento"""
                return self._chamar_api(
                    call='ListarEtapasFaturamento',
                    endpoint='produtos/etapafat/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_meios_pagamento(
            self, codigo
            ) -> dict:
                """Listagem de meios de pagamento"""
                return self._chamar_api(
                    call='ListarMeiosPagamento',
                    endpoint='geral/meiospagamento/',
                    param = {
                "codigo":codigo,

}
                )
            
    def listar_origem(
            self, codigo
            ) -> dict:
                """Lista Origem de pedidos."""
                return self._chamar_api(
                    call='ListarOrigem',
                    endpoint='geral/origempedido/',
                    param = {
                "codigo":codigo,

}
                )
            
    def listar_n_f_s_es(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """Lista de NFS-es."""
                return self._chamar_api(
                    call='ListarNFSEs',
                    endpoint='servicos/nfse/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def get_url_danfe(
            self, nCodNF, cCodNFInt
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='GetUrlDanfe',
                    endpoint='produtos/notafiscalutil/',
                    param = {
                "nCodNF":nCodNF,
                "cCodNFInt":cCodNFInt,

}
                )
            
    def get_url_logo(
            self, nCodEmpr, cCodEmprInt
            ) -> dict:
                """Retorna a URL do Logotipo"""
                return self._chamar_api(
                    call='GetUrlLogo',
                    endpoint='produtos/notafiscalutil/',
                    param = {
                "nCodEmpr":nCodEmpr,
                "cCodEmprInt":cCodEmprInt,

}
                )
            
    def get_url_nota_fiscal(
            self, nCodNF, cCodNFInt
            ) -> dict:
                """Retorna a URL da Nota Fiscal"""
                return self._chamar_api(
                    call='GetUrlNotaFiscal',
                    endpoint='produtos/notafiscalutil/',
                    param = {
                "nCodNF":nCodNF,
                "cCodNFInt":cCodNFInt,

}
                )
            
    def excluir_n_fe(
            self, cChaveNFe, nIdImportacao, nIdNFe
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirNFe',
                    endpoint='produtos/nfe/',
                    param = {
                "cChaveNFe":cChaveNFe,
                "nIdImportacao":nIdImportacao,
                "nIdNFe":nIdNFe,

}
                )
            
    def importar_canc_n_fe(
            self, cAppNome, cAppVersao, cAppId, cChaveNFe, cXmlNFeCanc, cMd5NFeCanc
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ImportarCancNFe',
                    endpoint='produtos/nfe/',
                    param = {
                "cAppNome":cAppNome,
                "cAppVersao":cAppVersao,
                "cAppId":cAppId,
                "cChaveNFe":cChaveNFe,
                "cXmlNFeCanc":cXmlNFeCanc,
                "cMd5NFeCanc":cMd5NFeCanc,

}
                )
            
    def listar_n_fe(
            self, nPagina, nRegPorPagina, dDataEmissaoInicial, dDataEmissaoFinal
            ) -> dict:
                """Lista as NFes importadas."""
                return self._chamar_api(
                    call='ListarNFe',
                    endpoint='produtos/nfe/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,
                "dDataEmissaoInicial":dDataEmissaoInicial,
                "dDataEmissaoFinal":dDataEmissaoFinal,

}
                )
            
    def associar_cod_int_servico(
            self, nCodServ, cCodIntServ
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AssociarCodIntServico',
                    endpoint='servicos/servico/',
                    param = {
                "nCodServ":nCodServ,
                "cCodIntServ":cCodIntServ,

}
                )
            
    def consultar_cadastro_servico(
            self, cCodIntServ, nCodServ
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarCadastroServico',
                    endpoint='servicos/servico/',
                    param = {
                "cCodIntServ":cCodIntServ,
                "nCodServ":nCodServ,

}
                )
            
    def excluir_cadastro_servico(
            self, cCodIntServ, nCodServ
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirCadastroServico',
                    endpoint='servicos/servico/',
                    param = {
                "cCodIntServ":cCodIntServ,
                "nCodServ":nCodServ,

}
                )
            
    def listar_cadastro_servico(
            self, nPagina, nRegPorPagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarCadastroServico',
                    endpoint='servicos/servico/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,

}
                )
            
    def alterar_o_s(
            self, Cabecalho, Departamentos, Email, InformacoesAdicionais, ServicosPrestados
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AlterarOS',
                    endpoint='servicos/os/',
                    param = {
                "Cabecalho":Cabecalho,
                "Departamentos":Departamentos,
                "Email":Email,
                "InformacoesAdicionais":InformacoesAdicionais,
                "ServicosPrestados":ServicosPrestados,

}
                )
            
    def consultar_o_s(
            self, cCodIntOS, nCodOS, cNumOS
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarOS',
                    endpoint='servicos/os/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,
                "cNumOS":cNumOS,

}
                )
            
    def excluir_o_s(
            self, cCodIntOS, nCodOS, cNumOS
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirOS',
                    endpoint='servicos/os/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,
                "cNumOS":cNumOS,

}
                )
            
    def incluir_o_s(
            self, Cabecalho, Departamentos, Email, InformacoesAdicionais, ServicosPrestados
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirOS',
                    endpoint='servicos/os/',
                    param = {
                "Cabecalho":Cabecalho,
                "Departamentos":Departamentos,
                "Email":Email,
                "InformacoesAdicionais":InformacoesAdicionais,
                "ServicosPrestados":ServicosPrestados,

}
                )
            
    def listar_o_s(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarOS',
                    endpoint='servicos/os/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def status_o_s(
            self, cCodIntOS, nCodOS
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='StatusOS',
                    endpoint='servicos/os/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,

}
                )
            
    def trocar_etapa_o_s(
            self, cCodIntOS, nCodOS, cNumOS, cEtapa
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='TrocarEtapaOS',
                    endpoint='servicos/os/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,
                "cNumOS":cNumOS,
                "cEtapa":cEtapa,

}
                )
            
    def associar_cod_int_o_s(
            self, cCodIntOS, nCodOS
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='AssociarCodIntOS',
                    endpoint='servicos/osp/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,

}
                )
            
    def cancelar_o_s(
            self, cCodIntOS, nCodOS
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='CancelarOS',
                    endpoint='servicos/osp/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,

}
                )
            
    def duplicar_o_s(
            self, cCodIntOS, nCodOS
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='DuplicarOS',
                    endpoint='servicos/osp/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,

}
                )
            
    def faturar_o_s(
            self, cCodIntOS, nCodOS
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='FaturarOS',
                    endpoint='servicos/osp/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,

}
                )
            
    def obter_o_s(
            self, cEtapa
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ObterOS',
                    endpoint='servicos/osp/',
                    param = {
                "cEtapa":cEtapa,

}
                )
            
    def reenviar_o_s(
            self, cCodIntOS, nCodOS
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ReenviarOS',
                    endpoint='servicos/osp/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,

}
                )
            
    def validar_o_s(
            self, cCodIntOS, nCodOS
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ValidarOS',
                    endpoint='servicos/osp/',
                    param = {
                "cCodIntOS":cCodIntOS,
                "nCodOS":nCodOS,

}
                )
            
    def alterar_contrato(
            self, cabecalho, departamentos, emailCliente, infAdic, itensContrato, observacoes, vencTextos
            ) -> dict:
                """Alterar um Contrato"""
                return self._chamar_api(
                    call='AlterarContrato',
                    endpoint='servicos/contrato/',
                    param = {
                "cabecalho":cabecalho,
                "departamentos":departamentos,
                "emailCliente":emailCliente,
                "infAdic":infAdic,
                "itensContrato":itensContrato,
                "observacoes":observacoes,
                "vencTextos":vencTextos,

}
                )
            
    def consultar_contrato(
            self, contratoChave
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ConsultarContrato',
                    endpoint='servicos/contrato/',
                    param = {
                "contratoChave":contratoChave,

}
                )
            
    def excluir_item(
            self, contratoChave, ItensExclusao
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ExcluirItem',
                    endpoint='servicos/contrato/',
                    param = {
                "contratoChave":contratoChave,
                "ItensExclusao":ItensExclusao,

}
                )
            
    def incluir_contrato(
            self, cabecalho, departamentos, emailCliente, infAdic, itensContrato, observacoes, vencTextos
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='IncluirContrato',
                    endpoint='servicos/contrato/',
                    param = {
                "cabecalho":cabecalho,
                "departamentos":departamentos,
                "emailCliente":emailCliente,
                "infAdic":infAdic,
                "itensContrato":itensContrato,
                "observacoes":observacoes,
                "vencTextos":vencTextos,

}
                )
            
    def listar_contratos(
            self, pagina, registros_por_pagina, apenas_importado_api
            ) -> dict:
                """Lista os contratos cadastrados."""
                return self._chamar_api(
                    call='ListarContratos',
                    endpoint='servicos/contrato/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,
                "apenas_importado_api":apenas_importado_api,

}
                )
            
    def upsert_contrato(
            self, cabecalho, departamentos, emailCliente, infAdic, itensContrato, observacoes, vencTextos
            ) -> dict:
                """Inclui / Altera um contrato"""
                return self._chamar_api(
                    call='UpsertContrato',
                    endpoint='servicos/contrato/',
                    param = {
                "cabecalho":cabecalho,
                "departamentos":departamentos,
                "emailCliente":emailCliente,
                "infAdic":infAdic,
                "itensContrato":itensContrato,
                "observacoes":observacoes,
                "vencTextos":vencTextos,

}
                )
            
    def ativar_contrato(
            self, nCodCtr
            ) -> dict:
                """Ativa um contrato"""
                return self._chamar_api(
                    call='AtivarContrato',
                    endpoint='servicos/contratofat/',
                    param = {
                "nCodCtr":nCodCtr,

}
                )
            
    def cancelar_contrato(
            self, nCodCtr
            ) -> dict:
                """Cancela contrato"""
                return self._chamar_api(
                    call='CancelarContrato',
                    endpoint='servicos/contratofat/',
                    param = {
                "nCodCtr":nCodCtr,

}
                )
            
    def faturar_contrato(
            self, nCodCtr
            ) -> dict:
                """Fatura um contrato."""
                return self._chamar_api(
                    call='FaturarContrato',
                    endpoint='servicos/contratofat/',
                    param = {
                "nCodCtr":nCodCtr,

}
                )
            
    def obter_contratos(
            self, cEtapa
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ObterContratos',
                    endpoint='servicos/contratofat/',
                    param = {
                "cEtapa":cEtapa,

}
                )
            
    def reativar_contrato(
            self, nCodCtr
            ) -> dict:
                """Reativar contrato"""
                return self._chamar_api(
                    call='ReativarContrato',
                    endpoint='servicos/contratofat/',
                    param = {
                "nCodCtr":nCodCtr,

}
                )
            
    def suspender_contrato(
            self, nCodCtr
            ) -> dict:
                """Suspende contrato"""
                return self._chamar_api(
                    call='SuspenderContrato',
                    endpoint='servicos/contratofat/',
                    param = {
                "nCodCtr":nCodCtr,

}
                )
            
    def validar_contrato(
            self, nCodCtr
            ) -> dict:
                """Valida os dados de um contrato para faturamento."""
                return self._chamar_api(
                    call='ValidarContrato',
                    endpoint='servicos/contratofat/',
                    param = {
                "nCodCtr":nCodCtr,

}
                )
            
    def listar_serv_munic(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarServMunic',
                    endpoint='servicos/listaservico/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_tipos_trib(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarTiposTrib',
                    endpoint='servicos/tipotrib/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_l_c116(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarLC116',
                    endpoint='servicos/lc116/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_n_b_s(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarNBS',
                    endpoint='servicos/nbs/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_produtos_i_b_p_t(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista os produtos da Tabela do IBPT."""
                return self._chamar_api(
                    call='ListarProdutosIBPT',
                    endpoint='servicos/ibpt/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_servicos_i_b_p_t(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarServicosIBPT',
                    endpoint='servicos/ibpt/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_tipo_fat_contrato(
            self, pagina, registros_por_pagina
            ) -> dict:
                """Lista os tipos de faturamento de contrato."""
                return self._chamar_api(
                    call='ListarTipoFatContrato',
                    endpoint='servicos/contratotpfat/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_tipo_utilizacao(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarTipoUtilizacao',
                    endpoint='servicos/tipoutilizacao/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_classificacao_servico(
            self, pagina, registros_por_pagina
            ) -> dict:
                """"""
                return self._chamar_api(
                    call='ListarClassificacaoServico',
                    endpoint='servicos/classificacaoservico/',
                    param = {
                "pagina":pagina,
                "registros_por_pagina":registros_por_pagina,

}
                )
            
    def listar_documentos(
            self, nPagina, nRegPorPagina, cModelo, dEmiInicial, dEmiFinal
            ) -> dict:
                """Lista de XMLs de Documentos Fiscais."""
                return self._chamar_api(
                    call='ListarDocumentos',
                    endpoint='contador/xml/',
                    param = {
                "nPagina":nPagina,
                "nRegPorPagina":nRegPorPagina,
                "cModelo":cModelo,
                "dEmiInicial":dEmiInicial,
                "dEmiFinal":dEmiFinal,

}
                )
            