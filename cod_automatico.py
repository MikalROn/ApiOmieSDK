from omieapi.core.omiebase import OmieBase 

# Aviso -> antes de usar confira se não a oq vc precisa já feito no codigo principal,
# o codigo autogerdo pode conter erros não detectados ainda
class CodigoAutogerado(OmieBase):
    def alterar_cliente(self, **kargs) -> dict:
                """ 
                Altera os dados do cliente 
                :exemplo de uso:
                {
                
                "codigo_cliente_integracao": "CodigoInterno0001",
                "email": "primeiro@ccliente.com.br",
                "razao_social": "Primeiro Cliente  Ltda Me",
                "nome_fantasia": "Primeiro Cliente"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_status
                """
                return self._chamar_api(
                    call= 'AlterarCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def associar_cod_int_cliente(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_cliente_omie": 0,
                "codigo_cliente_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_status
                """
                return self._chamar_api(
                    call= 'AssociarCodIntCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def consultar_cliente(self, **kargs) -> dict:
                """ 
                Consulta os dados de um cliente 
                :exemplo de uso:
                {
                
                "codigo_cliente_omie": 0,
                "codigo_cliente_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_cadastro
                """
                return self._chamar_api(
                    call= 'ConsultarCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def excluir_cliente(self, **kargs) -> dict:
                """ 
                Exclui um cliente da base de dados. 
                :exemplo de uso:
                {
                
                "codigo_cliente_omie": 0,
                "codigo_cliente_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_status
                """
                return self._chamar_api(
                    call= 'ExcluirCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def incluir_cliente(self, **kargs) -> dict:
                """ 
                Inclui o cliente no Omie 
                :exemplo de uso:
                {
                
                "codigo_cliente_integracao": "CodigoInterno0001",
                "email": "primeiro@ccliente.com.br",
                "razao_social": "Primeiro Cliente  Ltda Me",
                "nome_fantasia": "Primeiro Cliente"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_status
                """
                return self._chamar_api(
                    call= 'IncluirCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def incluir_clientes_por_lote(self, **kargs) -> dict:
                """ 
                DEPRECATED 
                :exemplo de uso:
                {
                
                "clientes_cadastro": [
                                
                                                "codigo_cliente_integracao": "CodigoInterno0001",
                                                "email": "primeiro@cliente.com.br",
                                                "nome_fantasia": "Primeiro Cliente",
                                                "razao_social": "Primeiro Cliente  Ltda Me"
                                ,
                                
                                                "codigo_cliente_integracao": "CodigoInterno0002",
                                                "email": "segundo@cliente.com.br",
                                                "nome_fantasia": "Segundo Cliente",
                                                "razao_social": "Segundo Cliente  Ltda Me"
                                
                ],
                "lote": 1

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_lote_response
                """
                return self._chamar_api(
                    call= 'IncluirClientesPorLote',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def listar_clientes(self, **kargs) -> dict:
                """ 
                Lista os clientes cadastrados 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_listfull_response
                """
                return self._chamar_api(
                    call= 'ListarClientes',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def listar_clientes_resumido(self, **kargs) -> dict:
                """ 
                Realiza pesquisa dos clientes 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_list_response
                """
                return self._chamar_api(
                    call= 'ListarClientesResumido',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def upsert_cliente(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_cliente_integracao": "CodigoInterno0001",
                "email": "primeiro@ccliente.com.br",
                "razao_social": "Primeiro Cliente  Ltda Me",
                "nome_fantasia": "Primeiro Cliente"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_status
                """
                return self._chamar_api(
                    call= 'UpsertCliente',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def upsert_cliente_cpf_cnpj(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cnpj_cpf": "80.716.929/0001-50",
                "email": "primeiro@ccliente.com.br",
                "razao_social": "Primeiro Cliente  Ltda Me",
                "nome_fantasia": "Primeiro Cliente"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_status
                """
                return self._chamar_api(
                    call= 'UpsertClienteCpfCnpj',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def upsert_clientes_por_lote(self, **kargs) -> dict:
                """ 
                DEPRECATED 
                :exemplo de uso:
                {
                
                "clientes_cadastro": [
                                
                                                "codigo_cliente_integracao": "CodigoInterno0001",
                                                "email": "primeiro@cliente.com.br",
                                                "nome_fantasia": "Primeiro Cliente",
                                                "razao_social": "Primeiro Cliente  Ltda Me"
                                ,
                                
                                                "codigo_cliente_integracao": "CodigoInterno0002",
                                                "email": "segundo@cliente.com.br",
                                                "nome_fantasia": "Segundo Cliente",
                                                "razao_social": "Segundo Cliente  Ltda Me"
                                
                ],
                "lote": 1

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientes/
                :retorno:  clientes_lote_response
                """
                return self._chamar_api(
                    call= 'UpsertClientesPorLote',
                    endpoint= 'geral/clientes/',
                    param = kargs
                )
            
    def alterar_caract_cliente(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_cliente_omie": 0,
                "codigo_cliente_integracao": "",
                "campo": "",
                "conteudo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientescaract/
                :retorno:  AlterarCaractClienteResponse
                """
                return self._chamar_api(
                    call= 'AlterarCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def consultar_caract_cliente(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_cliente_omie": 0,
                "codigo_cliente_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientescaract/
                :retorno:  ConsultarCaractClienteResponse
                """
                return self._chamar_api(
                    call= 'ConsultarCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def excluir_caract_cliente(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_cliente_omie": 0,
                "codigo_cliente_integracao": "",
                "campo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientescaract/
                :retorno:  ExcluirCaractClienteResponse
                """
                return self._chamar_api(
                    call= 'ExcluirCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def excluir_todas_caract_cliente(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_cliente_omie": 0,
                "codigo_cliente_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientescaract/
                :retorno:  ExcluirTodasCaractClienteResponse
                """
                return self._chamar_api(
                    call= 'ExcluirTodasCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def incluir_caract_cliente(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_cliente_omie": 0,
                "codigo_cliente_integracao": "",
                "campo": "",
                "conteudo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientescaract/
                :retorno:  IncluirCaractClienteResponse
                """
                return self._chamar_api(
                    call= 'IncluirCaractCliente',
                    endpoint= 'geral/clientescaract/',
                    param = kargs
                )
            
    def excluir_tags(self, **kargs) -> dict:
                """ 
                Remove tags associadas a um cliente. 
                :exemplo de uso:
                {
                
                "nCodCliente": 0,
                "cCodIntCliente": "",
                "tags": [
                                
                                                "tag": "Grupo A"
                                ,
                                
                                                "tag": "Grupo B"
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientetag/
                :retorno:  cTagExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirTags',
                    endpoint= 'geral/clientetag/',
                    param = kargs
                )
            
    def excluir_todas(self, **kargs) -> dict:
                """ 
                Remove todas as tags associadas a um cliente. 
                :exemplo de uso:
                {
                
                "nCodCliente": 0,
                "cCodIntCliente": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientetag/
                :retorno:  cTagExcluirTodasResponse
                """
                return self._chamar_api(
                    call= 'ExcluirTodas',
                    endpoint= 'geral/clientetag/',
                    param = kargs
                )
            
    def incluir_tags(self, **kargs) -> dict:
                """ 
                Associa tags a um cliente. 
                :exemplo de uso:
                {
                
                "nCodCliente": 0,
                "cCodIntCliente": "",
                "tags": [
                                
                                                "tag": "Grupo A"
                                ,
                                
                                                "tag": "Grupo B"
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientetag/
                :retorno:  cTagIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirTags',
                    endpoint= 'geral/clientetag/',
                    param = kargs
                )
            
    def listar_tags(self, **kargs) -> dict:
                """ 
                Lista as tags de um determinado cliente. 
                :exemplo de uso:
                {
                
                "nCodCliente": 0,
                "cCodIntCliente": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/clientetag/
                :retorno:  cTagListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTags',
                    endpoint= 'geral/clientetag/',
                    param = kargs
                )
            
    def alterar_projeto(self, **kargs) -> dict:
                """ 
                Altera um projeto 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codint": "123",
                "nome": "",
                "inativo": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/projetos/
                :retorno:  projAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def consultar_projeto(self, **kargs) -> dict:
                """ 
                Consulta um projeto 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codint": "123"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/projetos/
                :retorno:  projConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def excluir_projeto(self, **kargs) -> dict:
                """ 
                Exclui um projeto 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codint": "123"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/projetos/
                :retorno:  projExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def incluir_projeto(self, **kargs) -> dict:
                """ 
                Inclui um novo projeto 
                :exemplo de uso:
                {
                
                "codint": "123",
                "nome": "",
                "inativo": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/projetos/
                :retorno:  projIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def listar_projetos(self, **kargs) -> dict:
                """ 
                Lista os projetos cadastrados 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/projetos/
                :retorno:  projListarResponse
                """
                return self._chamar_api(
                    call= 'ListarProjetos',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def upsert_projeto(self, **kargs) -> dict:
                """ 
                Inclui / Altera um projeto. 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codint": "123",
                "nome": "",
                "inativo": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/projetos/
                :retorno:  projUpsertResponse
                """
                return self._chamar_api(
                    call= 'UpsertProjeto',
                    endpoint= 'geral/projetos/',
                    param = kargs
                )
            
    def consultar_empresa(self, **kargs) -> dict:
                """ 
                Realiza a consulta de um registro especifico 
                :exemplo de uso:
                {
                
                "codigo_empresa": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/empresas/
                :retorno:  empresas_cadastro
                """
                return self._chamar_api(
                    call= 'ConsultarEmpresa',
                    endpoint= 'geral/empresas/',
                    param = kargs
                )
            
    def listar_empresas(self, **kargs) -> dict:
                """ 
                Lista as empresas cadastradas no Omie. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 100,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/empresas/
                :retorno:  empresas_list_response
                """
                return self._chamar_api(
                    call= 'ListarEmpresas',
                    endpoint= 'geral/empresas/',
                    param = kargs
                )
            
    def alterar_departamento(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "descricao": "",
                "codigo": "000000000723648"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/departamentos/
                :retorno:  departamento_alterar_response
                """
                return self._chamar_api(
                    call= 'AlterarDepartamento',
                    endpoint= 'geral/departamentos/',
                    param = kargs
                )
            
    def consultar_departamento(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/departamentos/
                :retorno:  departamentos
                """
                return self._chamar_api(
                    call= 'ConsultarDepartamento',
                    endpoint= 'geral/departamentos/',
                    param = kargs
                )
            
    def excluir_departamento(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/departamentos/
                :retorno:  departamento_excluir_response
                """
                return self._chamar_api(
                    call= 'ExcluirDepartamento',
                    endpoint= 'geral/departamentos/',
                    param = kargs
                )
            
    def incluir_departamento(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "descricao": "",
                "codigo": "000000000723648"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/departamentos/
                :retorno:  departamento_incluir_response
                """
                return self._chamar_api(
                    call= 'IncluirDepartamento',
                    endpoint= 'geral/departamentos/',
                    param = kargs
                )
            
    def listar_departamentos(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/departamentos/
                :retorno:  
                """
                return self._chamar_api(
                    call= 'ListarDepartamentos',
                    endpoint= 'geral/departamentos/',
                    param = kargs
                )
            
    def listar_depatartamentos(self, **kargs) -> dict:
                """ 
                DEPRECATED 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/departamentos/
                :retorno:  
                """
                return self._chamar_api(
                    call= 'ListarDepatartamentos',
                    endpoint= 'geral/departamentos/',
                    param = kargs
                )
            
    def consultar_categoria(self, **kargs) -> dict:
                """ 
                Consulta uma categoria 
                :exemplo de uso:
                {
                
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/categorias/
                :retorno:  categoria_cadastro
                """
                return self._chamar_api(
                    call= 'ConsultarCategoria',
                    endpoint= 'geral/categorias/',
                    param = kargs
                )
            
    def listar_categorias(self, **kargs) -> dict:
                """ 
                Lista as categorias cadastradas 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/categorias/
                :retorno:  categoria_listfull_response
                """
                return self._chamar_api(
                    call= 'ListarCategorias',
                    endpoint= 'geral/categorias/',
                    param = kargs
                )
            
    def listar_parcelas(self, **kargs) -> dict:
                """ 
                Lista de Parcelas cadastradas. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/parcelas/
                :retorno:  parcelaListarResponse
                """
                return self._chamar_api(
                    call= 'ListarParcelas',
                    endpoint= 'geral/parcelas/',
                    param = kargs
                )
            
    def listar_tipo_ativ(self, **kargs) -> dict:
                """ 
                Listar Tipos de Atividade. 
                :exemplo de uso:
                {
                
                "filtrar_por_codigo": "",
                "filtrar_por_descricao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tpativ/
                :retorno:  tpAtivListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTipoAtiv',
                    endpoint= 'geral/tpativ/',
                    param = kargs
                )
            
    def listar_c_n_a_e(self, **kargs) -> dict:
                """ 
                Listar os CNAEs cadastrados 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cnae/
                :retorno:  cnaeListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCNAE',
                    endpoint= 'produtos/cnae/',
                    param = kargs
                )
            
    def pesquisar_cidades(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/cidades/
                :retorno:  cidListarResponse
                """
                return self._chamar_api(
                    call= 'PesquisarCidades',
                    endpoint= 'geral/cidades/',
                    param = kargs
                )
            
    def listar_paises(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "filtrar_por_codigo": "",
                "filtrar_por_descricao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/paises/
                :retorno:  paisListarResponse
                """
                return self._chamar_api(
                    call= 'ListarPaises',
                    endpoint= 'geral/paises/',
                    param = kargs
                )
            
    def listar_tipos_anexos(self, **kargs) -> dict:
                """ 
                Listagem de tipos de anexos. 
                :exemplo de uso:
                {
                
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tiposanexo/
                :retorno:  ListarTipoAnexoResponse
                """
                return self._chamar_api(
                    call= 'ListarTiposAnexos',
                    endpoint= 'geral/tiposanexo/',
                    param = kargs
                )
            
    def consultar_anexo(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntAnexo": "",
                "cTabela": "",
                "nId": 0,
                "nIdAnexo": 0,
                "cNomeArquivo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/anexo/
                :retorno:  docConsultarAnexoResponse
                """
                return self._chamar_api(
                    call= 'ConsultarAnexo',
                    endpoint= 'geral/anexo/',
                    param = kargs
                )
            
    def excluir_anexo(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntAnexo": "",
                "cTabela": "",
                "nId": 0,
                "nIdAnexo": 0,
                "cNomeArquivo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/anexo/
                :retorno:  docExcluirAnexoResponse
                """
                return self._chamar_api(
                    call= 'ExcluirAnexo',
                    endpoint= 'geral/anexo/',
                    param = kargs
                )
            
    def incluir_anexo(self, **kargs) -> dict:
                """ 
                Inclui o anexo para um documento. 
                :exemplo de uso:
                {
                
                "cCodIntAnexo": "",
                "cTabela": "",
                "nId": 0,
                "cNomeArquivo": "",
                "cTipoArquivo": "",
                "cArquivo": "",
                "cMd5": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/anexo/
                :retorno:  docIncluirAnexoResponse
                """
                return self._chamar_api(
                    call= 'IncluirAnexo',
                    endpoint= 'geral/anexo/',
                    param = kargs
                )
            
    def listar_anexo(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50,
                "nId": 0,
                "cTabela": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/anexo/
                :retorno:  docListarAnexosResponse
                """
                return self._chamar_api(
                    call= 'ListarAnexo',
                    endpoint= 'geral/anexo/',
                    param = kargs
                )
            
    def obter_anexo(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntAnexo": "",
                "cTabela": "",
                "nId": 0,
                "nIdAnexo": 0,
                "cNomeArquivo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/anexo/
                :retorno:  docObterAnexoResponse
                """
                return self._chamar_api(
                    call= 'ObterAnexo',
                    endpoint= 'geral/anexo/',
                    param = kargs
                )
            
    def alterar_tipo_entrega(self, **kargs) -> dict:
                """ 
                Alterar tipo de entrega 
                :exemplo de uso:
                {
                
                "nCodEntrega": 0,
                "cCodIntEntrega": "",
                "cDescricao": "",
                "cInativo": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tiposentrega/
                :retorno:  teAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def consultar_tipo_entrega(self, **kargs) -> dict:
                """ 
                Consultar tipo de entrega 
                :exemplo de uso:
                {
                
                "nCodEntrega": 0,
                "cCodIntEntrega": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tiposentrega/
                :retorno:  teConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def excluir_tipo_entrega(self, **kargs) -> dict:
                """ 
                Excluir tipo de entrega 
                :exemplo de uso:
                {
                
                "nCodEntrega": 0,
                "cCodIntEntrega": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tiposentrega/
                :retorno:  teExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def incluir_tipo_entrega(self, **kargs) -> dict:
                """ 
                Incluir tipo de entrega 
                :exemplo de uso:
                {
                
                "nCodTransp": 0,
                "cCodIntEntrega": "",
                "cDescricao": "",
                "cInativo": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tiposentrega/
                :retorno:  teIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def listar_tipo_entrega(self, **kargs) -> dict:
                """ 
                Listar tipo de entrega 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegistrosPorPagina": 50,
                "nCodTransp": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tiposentrega/
                :retorno:  teListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTipoEntrega',
                    endpoint= 'geral/tiposentrega/',
                    param = kargs
                )
            
    def listar_tipo_assinante(self, **kargs) -> dict:
                """ 
                Lista os tipos de assinante 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tipoassinante/
                :retorno:  tipoAssinanteResponse
                """
                return self._chamar_api(
                    call= 'ListarTipoAssinante',
                    endpoint= 'geral/tipoassinante/',
                    param = kargs
                )
            
    def alterar_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodInt": "79137",
                                "cNome": "Omiexperience S/A",
                                "cObs": "Conta adicionada via API",
                                "dDtReg": "23/01/2024",
                                "dDtValid": "25/02/2024"
                ,
                "endereco": 
                                "cEndereco": "Av. Dr. Chucri Zaidan, 1550",
                                "cCEP": "04583-110",
                                "cCidade": "SAO PAULO",
                                "cUF": "SP",
                                "cPais": "Brasil"
                ,
                "telefone_email": 
                                "cDDDTel": "11",
                                "cNumTel": "5171-8888",
                                "cEmail": "ajuda@omie.com.br",
                                "cWebsite": "http://www.omie.com.br/"
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contas/
                :retorno:  CRM_CONTAS_RESPOSTA
                """
                return self._chamar_api(
                    call= 'AlterarConta',
                    endpoint= 'crm/contas/',
                    param = kargs
                )
            
    def consultar_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodInt": "0004"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contas/
                :retorno:  cadastros
                """
                return self._chamar_api(
                    call= 'ConsultarConta',
                    endpoint= 'crm/contas/',
                    param = kargs
                )
            
    def excluir_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCod": 0,
                "cCodInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contas/
                :retorno:  CRM_CONTAS_RESPOSTA
                """
                return self._chamar_api(
                    call= 'ExcluirConta',
                    endpoint= 'crm/contas/',
                    param = kargs
                )
            
    def incluir_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodInt": "42675",
                                "cNome": "Omiexperience S/A",
                                "cObs": "Conta adicionada via API",
                                "dDtReg": "23/01/2024",
                                "dDtValid": "10/06/2024"
                ,
                "endereco": 
                                "cEndereco": "Av. Dr. Chucri Zaidan, 1550",
                                "cCEP": "04583-110",
                                "cCidade": "SAO PAULO",
                                "cUF": "SP",
                                "cPais": "Brasil"
                ,
                "telefone_email": 
                                "cDDDTel": "11",
                                "cNumTel": "5171-8888",
                                "cEmail": "ajuda@omie.com.br",
                                "cWebsite": "http://www.omie.com.br/"
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contas/
                :retorno:  CRM_CONTAS_RESPOSTA
                """
                return self._chamar_api(
                    call= 'IncluirConta',
                    endpoint= 'crm/contas/',
                    param = kargs
                )
            
    def listar_contas(self, **kargs) -> dict:
                """ 
                Lista as contas do CRM. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contas/
                :retorno:  contaListarResponse
                """
                return self._chamar_api(
                    call= 'ListarContas',
                    endpoint= 'crm/contas/',
                    param = kargs
                )
            
    def upsert_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodInt": "0004",
                                "cNome": "Omiexperience S/A",
                                "cObs": "Conta adicionada via API (1706038786)",
                                "dDtReg": "23/01/2024",
                                "dDtValid": "13/03/2024"
                ,
                "endereco": 
                                "cEndereco": "Av. Dr. Chucri Zaidan, 1550",
                                "cCEP": "04583-110",
                                "cCidade": "SAO PAULO",
                                "cUF": "SP",
                                "cPais": "Brasil"
                ,
                "telefone_email": 
                                "cDDDTel": "11",
                                "cNumTel": "5171-8888",
                                "cEmail": "ajuda@omie.com.br",
                                "cWebsite": "http://www.omie.com.br/"
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contas/
                :retorno:  CRM_CONTAS_RESPOSTA
                """
                return self._chamar_api(
                    call= 'UpsertConta',
                    endpoint= 'crm/contas/',
                    param = kargs
                )
            
    def verificar_conta(self, **kargs) -> dict:
                """ 
                Verifica se uma conta foi criada a partir do nome e e-mail. 
                :exemplo de uso:
                {
                
                "cNome": "",
                "cEmail": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contas/
                :retorno:  contaVerificarResponse
                """
                return self._chamar_api(
                    call= 'VerificarConta',
                    endpoint= 'crm/contas/',
                    param = kargs
                )
            
    def alterar_caract_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCod": 0,
                "cCodInt": "",
                "campo": "",
                "conteudo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contascaract/
                :retorno:  AlterarCaractCRMContaResponse
                """
                return self._chamar_api(
                    call= 'AlterarCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def consultar_caract_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCod": 0,
                "cCodInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contascaract/
                :retorno:  ConsultarCaractCRMContaResponse
                """
                return self._chamar_api(
                    call= 'ConsultarCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def excluir_caract_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCod": 0,
                "cCodInt": "",
                "campo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contascaract/
                :retorno:  ExcluirCaractCRMContaResponse
                """
                return self._chamar_api(
                    call= 'ExcluirCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def excluir_todas_caract_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCod": 0,
                "cCodInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contascaract/
                :retorno:  ExcluirTodasCaractCRMContaResponse
                """
                return self._chamar_api(
                    call= 'ExcluirTodasCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def incluir_caract_conta(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCod": 0,
                "cCodInt": "",
                "campo": "",
                "conteudo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contascaract/
                :retorno:  IncluirCaractCRMContaResponse
                """
                return self._chamar_api(
                    call= 'IncluirCaractConta',
                    endpoint= 'crm/contascaract/',
                    param = kargs
                )
            
    def alterar_contato(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodInt": "",
                                "cNome": "",
                                "cSobrenome": "",
                                "cCargo": "",
                                "dDtNasc": "",
                                "nCodVend": 0,
                                "nCodConta": 0
                ,
                "endereco": 
                                "cEndereco": "",
                                "cCompl": "",
                                "cCEP": "",
                                "cBairro": "",
                                "cCidade": "",
                                "cUF": "",
                                "cPais": ""
                ,
                "telefone_email": 
                                "cDDDCel1": "",
                                "cNumCel1": "",
                                "cEmail": "",
                                "cWebsite": ""
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contatos/
                :retorno:  CRM_CONTATOS_RESPOSTA
                """
                return self._chamar_api(
                    call= 'AlterarContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def consultar_contato(self, **kargs) -> dict:
                """ 
                Consulta o Contato 
                :exemplo de uso:
                {
                
                "nCod": 1,
                "cCodInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contatos/
                :retorno:  cadastros
                """
                return self._chamar_api(
                    call= 'ConsultarContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def excluir_contato(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCod": 0,
                "cCodInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contatos/
                :retorno:  CRM_CONTATOS_RESPOSTA
                """
                return self._chamar_api(
                    call= 'ExcluirContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def incluir_contato(self, **kargs) -> dict:
                """ 
                Inclui um novo Contato 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodInt": "",
                                "cNome": "",
                                "cSobrenome": "",
                                "cCargo": "",
                                "dDtNasc": "",
                                "nCodVend": 0,
                                "nCodConta": 0
                ,
                "endereco": 
                                "cEndereco": "",
                                "cCompl": "",
                                "cCEP": "",
                                "cBairro": "",
                                "cCidade": "",
                                "cUF": "",
                                "cPais": ""
                ,
                "telefone_email": 
                                "cDDDCel1": "",
                                "cNumCel1": "",
                                "cEmail": "",
                                "cWebsite": ""
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contatos/
                :retorno:  CRM_CONTATOS_RESPOSTA
                """
                return self._chamar_api(
                    call= 'IncluirContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def listar_contatos(self, **kargs) -> dict:
                """ 
                Lista os contatos do CRM. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contatos/
                :retorno:  contatoListarResponse
                """
                return self._chamar_api(
                    call= 'ListarContatos',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def upsert_contato(self, **kargs) -> dict:
                """ 
                Upsert do contato 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodInt": "",
                                "cNome": "",
                                "cSobrenome": "",
                                "cCargo": "",
                                "dDtNasc": "",
                                "nCodVend": 0,
                                "nCodConta": 0
                ,
                "endereco": 
                                "cEndereco": "",
                                "cCompl": "",
                                "cCEP": "",
                                "cBairro": "",
                                "cCidade": "",
                                "cUF": "",
                                "cPais": ""
                ,
                "telefone_email": 
                                "cDDDCel1": "",
                                "cNumCel1": "",
                                "cEmail": "",
                                "cWebsite": ""
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contatos/
                :retorno:  CRM_CONTATOS_RESPOSTA
                """
                return self._chamar_api(
                    call= 'UpsertContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def verificar_contato(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cNome": "",
                "cEmail": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/contatos/
                :retorno:  contatoVerificarResponse
                """
                return self._chamar_api(
                    call= 'VerificarContato',
                    endpoint= 'crm/contatos/',
                    param = kargs
                )
            
    def alterar_oportunidade(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "nCodOp": 0,
                                "cCodIntOp": "",
                                "cDesOp": "",
                                "nCodConta": 0,
                                "nCodContato": 0,
                                "nCodOrigem": 0,
                                "nCodSolucao": 0,
                                "nCodVendedor": 0
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/oportunidades/
                :retorno:  opAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def consultar_oportunidade(self, **kargs) -> dict:
                """ 
                Consulta de oportunidade. 
                :exemplo de uso:
                {
                
                "nCodOp": 0,
                "cCodIntOp": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/oportunidades/
                :retorno:  opConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def excluir_oportunidade(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodOp": 0,
                "cCodIntOp": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/oportunidades/
                :retorno:  opExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def incluir_oportunidade(self, **kargs) -> dict:
                """ 
                Incluir uma oportunidade. 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodIntOp": "",
                                "cDesOp": "",
                                "nCodConta": 0,
                                "nCodContato": 0,
                                "nCodOrigem": 0,
                                "nCodSolucao": 0,
                                "nCodVendedor": 0
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/oportunidades/
                :retorno:  opIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def listar_oportunidades(self, **kargs) -> dict:
                """ 
                Lista de oportunidades. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/oportunidades/
                :retorno:  opListarResponse
                """
                return self._chamar_api(
                    call= 'ListarOportunidades',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def upsert_oportunidade(self, **kargs) -> dict:
                """ 
                Upsert de oportunidade. 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "nCodOp": 0,
                                "cCodIntOp": "",
                                "cDesOp": "",
                                "nCodConta": 0,
                                "nCodContato": 0,
                                "nCodOrigem": 0,
                                "nCodSolucao": 0,
                                "nCodVendedor": 0
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/oportunidades/
                :retorno:  opUpsertResponse
                """
                return self._chamar_api(
                    call= 'UpsertOportunidade',
                    endpoint= 'crm/oportunidades/',
                    param = kargs
                )
            
    def obter_lista_op(self, **kargs) -> dict:
                """ 
                Lista de Oportunidades. 
                :exemplo de uso:
                {
                
                "cMesAno": "04/2022",
                "cTemperatura": "em-processo"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/oportunidades-resumo/
                :retorno:  ObterListaOpResponse
                """
                return self._chamar_api(
                    call= 'ObterListaOp',
                    endpoint= 'crm/oportunidades-resumo/',
                    param = kargs
                )
            
    def obter_resumo_op(self, **kargs) -> dict:
                """ 
                Resumo das oportunidades. 
                :exemplo de uso:
                {
                
                "nIdVendedor": 0,
                "nIdParceiro": 0,
                "cMesAno": "02/2022",
                "lApenasResumo": true

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/oportunidades-resumo/
                :retorno:  obterResumoOpResponse
                """
                return self._chamar_api(
                    call= 'ObterResumoOp',
                    endpoint= 'crm/oportunidades-resumo/',
                    param = kargs
                )
            
    def alterar_tarefa(self, **kargs) -> dict:
                """ 
                Altera uma tarefa. 
                :exemplo de uso:
                {
                
                "nCodTarefa": 0,
                "nCodOp": 0,
                "cCodInt": "",
                "nCodUsuario": 425605408,
                "dData": "23/01/2024",
                "cHora": "10:15",
                "nCodNotif": 99999,
                "nCodAtividade": 1,
                "cDescricao": "Descricao"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas/
                :retorno:  tarefaAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def calendario_tarefas(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "email_vend": "omie@omie.com.br",
                "calendar_key": "9bbd473104936d521d364abdc6a0d1a5"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas/
                :retorno:  tarefa_ics_response
                """
                return self._chamar_api(
                    call= 'CalendarioTarefas',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def consultar_tarefa(self, **kargs) -> dict:
                """ 
                Consulta uma tarefa da oportunidade. 
                :exemplo de uso:
                {
                
                "nCodTarefa": 0,
                "nCodOp": 0,
                "cCodInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas/
                :retorno:  tarefaConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def excluir_tarefa(self, **kargs) -> dict:
                """ 
                Exclui um tarefa. 
                :exemplo de uso:
                {
                
                "nCodTarefa": 0,
                "nCodOp": 0,
                "cCodInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas/
                :retorno:  tarefaExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def incluir_tarefa(self, **kargs) -> dict:
                """ 
                Inclui uma tarefa na oportunidade. 
                :exemplo de uso:
                {
                
                "nCodOp": 0,
                "cCodInt": "",
                "nCodUsuario": 425605408,
                "dData": "23/01/2024",
                "cHora": "10:15",
                "nCodNotif": 99999,
                "nCodAtividade": 1,
                "cDescricao": "Descricao"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas/
                :retorno:  tarefaIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def listar_emails_tarefas(self, **kargs) -> dict:
                """ 
                Lista os  emails tarefas. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas/
                :retorno:  tarefaEmailListarResponse
                """
                return self._chamar_api(
                    call= 'ListarEmailsTarefas',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def listar_tarefas(self, **kargs) -> dict:
                """ 
                Tarefas da oportunidade. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas/
                :retorno:  tarefaListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTarefas',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def upsert_tarefa(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodTarefa": 0,
                "nCodOp": 0,
                "cCodInt": "",
                "nCodUsuario": 425605408,
                "dData": "23/01/2024",
                "cHora": "10:15",
                "nCodNotif": 99999,
                "nCodAtividade": 1,
                "cDescricao": "Descricao"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas/
                :retorno:  tarefaUpsertResponse
                """
                return self._chamar_api(
                    call= 'UpsertTarefa',
                    endpoint= 'crm/tarefas/',
                    param = kargs
                )
            
    def obter_detalhes_tarefa(self, **kargs) -> dict:
                """ 
                Consulta os detalhes de uma tafera. 
                :exemplo de uso:
                {
                
                "nIdOportunidade": 0,
                "nIdTarefa": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas-resumo/
                :retorno:  ObterDetalhesTarefasResponse
                """
                return self._chamar_api(
                    call= 'ObterDetalhesTarefa',
                    endpoint= 'crm/tarefas-resumo/',
                    param = kargs
                )
            
    def obter_lista_tarefas(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "dDia": "23/01/2024"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas-resumo/
                :retorno:  ObterListaTarefasResponse
                """
                return self._chamar_api(
                    call= 'ObterListaTarefas',
                    endpoint= 'crm/tarefas-resumo/',
                    param = kargs
                )
            
    def obter_resumo_tarefas(self, **kargs) -> dict:
                """ 
                Resumos das tarefas do CRM. 
                :exemplo de uso:
                {
                
                "dDataInicio": "23/01/2024",
                "dDataFim": "23/01/2024",
                "cTipoTarefa": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tarefas-resumo/
                :retorno:  obterResumoTarefasResponse
                """
                return self._chamar_api(
                    call= 'ObterResumoTarefas',
                    endpoint= 'crm/tarefas-resumo/',
                    param = kargs
                )
            
    def listar_solucoes(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/solucoes/
                :retorno:  solucaoListarResponse
                """
                return self._chamar_api(
                    call= 'ListarSolucoes',
                    endpoint= 'crm/solucoes/',
                    param = kargs
                )
            
    def listar_fases(self, **kargs) -> dict:
                """ 
                Fases da Oportunidade 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/fases/
                :retorno:  fasesListarResponse
                """
                return self._chamar_api(
                    call= 'ListarFases',
                    endpoint= 'crm/fases/',
                    param = kargs
                )
            
    def listar_usuarios(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/usuarios/
                :retorno:  uscrmListarResponse
                """
                return self._chamar_api(
                    call= 'ListarUsuarios',
                    endpoint= 'crm/usuarios/',
                    param = kargs
                )
            
    def obter_usuarios(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cExibirTodos": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/usuarios/
                :retorno:  obterUsuariosResponse
                """
                return self._chamar_api(
                    call= 'ObterUsuarios',
                    endpoint= 'crm/usuarios/',
                    param = kargs
                )
            
    def listar_status(self, **kargs) -> dict:
                """ 
                Status da oportunidade. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/status/
                :retorno:  statusListarResponse
                """
                return self._chamar_api(
                    call= 'ListarStatus',
                    endpoint= 'crm/status/',
                    param = kargs
                )
            
    def listar_motivos(self, **kargs) -> dict:
                """ 
                Motivos da oportunidade. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/motivos/
                :retorno:  motivoListarResponse
                """
                return self._chamar_api(
                    call= 'ListarMotivos',
                    endpoint= 'crm/motivos/',
                    param = kargs
                )
            
    def listar_tipos(self, **kargs) -> dict:
                """ 
                Tipos de oportunidades. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tipos/
                :retorno:  tipoListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTipos',
                    endpoint= 'crm/tipos/',
                    param = kargs
                )
            
    def listar_parceiros(self, **kargs) -> dict:
                """ 
                Parceiros e equipes da oportunidade. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/parceiros/
                :retorno:  parceiroListarResponse
                """
                return self._chamar_api(
                    call= 'ListarParceiros',
                    endpoint= 'crm/parceiros/',
                    param = kargs
                )
            
    def listar_finders(self, **kargs) -> dict:
                """ 
                Finders da oportunidade. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/finders/
                :retorno:  finderListarResponse
                """
                return self._chamar_api(
                    call= 'ListarFinders',
                    endpoint= 'crm/finders/',
                    param = kargs
                )
            
    def listar_origens(self, **kargs) -> dict:
                """ 
                Origens da oportunidade. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/origens/
                :retorno:  origemListarResponse
                """
                return self._chamar_api(
                    call= 'ListarOrigens',
                    endpoint= 'crm/origens/',
                    param = kargs
                )
            
    def listar_concorrentes(self, **kargs) -> dict:
                """ 
                Concorrentes da oportunidade. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/concorrentes/
                :retorno:  concorrenteListarResponse
                """
                return self._chamar_api(
                    call= 'ListarConcorrentes',
                    endpoint= 'crm/concorrentes/',
                    param = kargs
                )
            
    def listar_verticais(self, **kargs) -> dict:
                """ 
                Lista as verticais cadastradas. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/verticais/
                :retorno:  verticalListarResponse
                """
                return self._chamar_api(
                    call= 'ListarVerticais',
                    endpoint= 'crm/verticais/',
                    param = kargs
                )
            
    def alterar_vendedor(self, **kargs) -> dict:
                """ 
                Altera os dados de um vendedor 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codInt": "123",
                "nome": "",
                "inativo": "N",
                "email": "teste@minhaempresa.com.br",
                "fatura_pedido": "S",
                "visualiza_pedido": "N",
                "comissao": 10.0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/vendedores/
                :retorno:  vendAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def consultar_vendedor(self, **kargs) -> dict:
                """ 
                Consulta os dados de um vendedor 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codInt": "123"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/vendedores/
                :retorno:  vendConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def excluir_vendedor(self, **kargs) -> dict:
                """ 
                Exclui um vendedor 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codInt": "123"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/vendedores/
                :retorno:  vendExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def incluir_vendedor(self, **kargs) -> dict:
                """ 
                Inclui um vendedor 
                :exemplo de uso:
                {
                
                "codInt": "123",
                "nome": "",
                "inativo": "N",
                "email": "teste@minhaempresa.com.br",
                "fatura_pedido": "S",
                "visualiza_pedido": "N",
                "comissao": 10.0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/vendedores/
                :retorno:  vendIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def listar_vendedores(self, **kargs) -> dict:
                """ 
                Listagem de Vendedores 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 100,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/vendedores/
                :retorno:  vendListarResponse
                """
                return self._chamar_api(
                    call= 'ListarVendedores',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def upsert_vendedor(self, **kargs) -> dict:
                """ 
                Inclui / Altera um vendedor 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codInt": "123",
                "nome": "",
                "inativo": "N",
                "email": "teste@minhaempresa.com.br",
                "fatura_pedido": "S",
                "visualiza_pedido": "N",
                "comissao": 10.0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/vendedores/
                :retorno:  vendUpsertResponse
                """
                return self._chamar_api(
                    call= 'UpsertVendedor',
                    endpoint= 'geral/vendedores/',
                    param = kargs
                )
            
    def consultar_tipo_tarefa(self, **kargs) -> dict:
                """ 
                Consulta tipo de tarefa 
                :exemplo de uso:
                {
                
                "nIdTipoTarefa": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tipostarefa/
                :retorno:  tipostarefaConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarTipoTarefa',
                    endpoint= 'crm/tipostarefa/',
                    param = kargs
                )
            
    def excluir_tipo_tarefa(self, **kargs) -> dict:
                """ 
                Excluir tipo de tarefa 
                :exemplo de uso:
                {
                
                "nIdTipoTarefa": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tipostarefa/
                :retorno:  tipostarefaExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirTipoTarefa',
                    endpoint= 'crm/tipostarefa/',
                    param = kargs
                )
            
    def listar_tipos_tarefa(self, **kargs) -> dict:
                """ 
                Lista tipos de tarefa 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/crm/tipostarefa/
                :retorno:  tipostarefaListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTiposTarefa',
                    endpoint= 'crm/tipostarefa/',
                    param = kargs
                )
            
    def alterar_conta_corrente(self, **kargs) -> dict:
                """ 
                Altera a Conta Corrente 
                :exemplo de uso:
                {
                
                "cCodCCInt": "MyCC0001",
                "tipo_conta_corrente": "CX",
                "codigo_banco": "999",
                "descricao": "Caixinha",
                "saldo_inicial": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/contacorrente/
                :retorno:  fin_conta_corrente_cadastro_response
                """
                return self._chamar_api(
                    call= 'AlterarContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def consultar_conta_corrente(self, **kargs) -> dict:
                """ 
                Realiza a consulta de uma conta corrente 
                :exemplo de uso:
                {
                
                "nCodCC": 0,
                "cCodCCInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/contacorrente/
                :retorno:  ListarContasCorrentes
                """
                return self._chamar_api(
                    call= 'ConsultarContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def excluir_conta_corrente(self, **kargs) -> dict:
                """ 
                Excluir a Conta Corrente 
                :exemplo de uso:
                {
                
                "nCodCC": 0,
                "cCodCCInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/contacorrente/
                :retorno:  fin_conta_corrente_cadastro_response
                """
                return self._chamar_api(
                    call= 'ExcluirContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def incluir_conta_corrente(self, **kargs) -> dict:
                """ 
                Inclui uma conta corrente 
                :exemplo de uso:
                {
                
                "cCodCCInt": "MyCC0001",
                "tipo_conta_corrente": "CX",
                "codigo_banco": "999",
                "descricao": "Caixinha",
                "saldo_inicial": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/contacorrente/
                :retorno:  fin_conta_corrente_cadastro_response
                """
                return self._chamar_api(
                    call= 'IncluirContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def listar_contas_correntes(self, **kargs) -> dict:
                """ 
                Listar Contas Correntes 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 100,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/contacorrente/
                :retorno:  fin_conta_corrente_listar_response
                """
                return self._chamar_api(
                    call= 'ListarContasCorrentes',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def listar_resumo_contas_correntes(self, **kargs) -> dict:
                """ 
                Listar resumida de Contas correntes. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 100,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/contacorrente/
                :retorno:  fin_conta_corrente_resumo_response
                """
                return self._chamar_api(
                    call= 'ListarResumoContasCorrentes',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def pesquisar_conta_corrente(self, **kargs) -> dict:
                """ 
                DEPRECATED 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 100,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/contacorrente/
                :retorno:  fin_conta_corrente_pesquisar_resposta
                """
                return self._chamar_api(
                    call= 'PesquisarContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def upsert_conta_corrente(self, **kargs) -> dict:
                """ 
                Upsert da Conta Corrente 
                :exemplo de uso:
                {
                
                "cCodCCInt": "MyCC0001",
                "tipo_conta_corrente": "CX",
                "codigo_banco": "999",
                "descricao": "Caixinha",
                "saldo_inicial": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/contacorrente/
                :retorno:  fin_conta_corrente_cadastro_response
                """
                return self._chamar_api(
                    call= 'UpsertContaCorrente',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def upsert_conta_corrente_por_lote(self, **kargs) -> dict:
                """ 
                Upsert por lote de Conta Corrente 
                :exemplo de uso:
                {
                
                "lote": 1,
                "fin_conta_corrente_cadastro": [
                                
                                                "cCodCCInt": "MyCC0001",
                                                "tipo_conta_corrente": "CX",
                                                "codigo_banco": "999",
                                                "descricao": "Caixinha",
                                                "saldo_inicial": 0
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/contacorrente/
                :retorno:  fin_conta_corrente_lote_response
                """
                return self._chamar_api(
                    call= 'UpsertContaCorrentePorLote',
                    endpoint= 'geral/contacorrente/',
                    param = kargs
                )
            
    def alterar_lanc_c_c(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntLanc": "1706041410",
                "cabecalho": 
                                "nCodCC": 427619317,
                                "dDtLanc": "23/01/2024",
                                "nValorLanc": 123.46
                ,
                "detalhes": 
                                "cCodCateg": "1.01.02",
                                "cTipo": "DIN",
                                "nCodCliente": 2485994,
                                "cObs": "Referente a jardinagem executada na matriz"
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contacorrentelancamentos/
                :retorno:  lanccAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def consulta_lanc_c_c(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodLanc": 0,
                "cCodIntLanc": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contacorrentelancamentos/
                :retorno:  lanccConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultaLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def excluir_lanc_c_c(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodLanc": 0,
                "cCodIntLanc": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contacorrentelancamentos/
                :retorno:  lanccExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def incluir_lanc_c_c(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntLanc": "1706041410",
                "cabecalho": 
                                "nCodCC": 427619317,
                                "dDtLanc": "23/01/2024",
                                "nValorLanc": 123.46
                ,
                "detalhes": 
                                "cCodCateg": "1.01.02",
                                "cTipo": "DIN",
                                "nCodCliente": 2485994,
                                "cObs": "Referente a jardinagem executada na matriz"
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contacorrentelancamentos/
                :retorno:  lanccIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def listar_lanc_c_c(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contacorrentelancamentos/
                :retorno:  lanccListarResponse
                """
                return self._chamar_api(
                    call= 'ListarLancCC',
                    endpoint= 'financas/contacorrentelancamentos/',
                    param = kargs
                )
            
    def alterar_conta_pagar(self, **kargs) -> dict:
                """ 
                Altera uma conta a pagar 
                :exemplo de uso:
                {
                
                "codigo_lancamento_integracao": "1706039026",
                "codigo_cliente_fornecedor": 4214850,
                "data_vencimento": "23/01/2024",
                "valor_documento": 100.0,
                "codigo_categoria": "2.04.01",
                "data_previsao": "23/01/2024",
                "id_conta_corrente": 4243124

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  conta_pagar_cadastro_response
                """
                return self._chamar_api(
                    call= 'AlterarContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def cancelar_pagamento(self, **kargs) -> dict:
                """ 
                Cancela um pagamento realizado no Contas a Pagar 
                :exemplo de uso:
                {
                
                "codigo_baixa": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  conta_pagar_cancelar_pagamento_resposta
                """
                return self._chamar_api(
                    call= 'CancelarPagamento',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def consultar_conta_pagar(self, **kargs) -> dict:
                """ 
                Consulta uma conta a pagar 
                :exemplo de uso:
                {
                
                "codigo_lancamento_omie": 0,
                "codigo_lancamento_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  conta_pagar_cadastro
                """
                return self._chamar_api(
                    call= 'ConsultarContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def excluir_conta_pagar(self, **kargs) -> dict:
                """ 
                Exclui uma conta a pagar 
                :exemplo de uso:
                {
                
                "codigo_lancamento_omie": 0,
                "codigo_lancamento_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  conta_pagar_cadastro_response
                """
                return self._chamar_api(
                    call= 'ExcluirContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def incluir_conta_pagar(self, **kargs) -> dict:
                """ 
                Inclui uma conta a Pagar. 
                :exemplo de uso:
                {
                
                "codigo_lancamento_integracao": "1706039026",
                "codigo_cliente_fornecedor": 4214850,
                "data_vencimento": "23/01/2024",
                "valor_documento": 100.0,
                "codigo_categoria": "2.04.01",
                "data_previsao": "23/01/2024",
                "id_conta_corrente": 4243124

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  conta_pagar_cadastro_response
                """
                return self._chamar_api(
                    call= 'IncluirContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def incluir_conta_pagar_por_lote(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "lote": 100,
                "conta_pagar_cadastro": [
                                
                                                "codigo_lancamento_integracao": "1706039026",
                                                "codigo_cliente_fornecedor": 4214850,
                                                "data_vencimento": "23/01/2024",
                                                "valor_documento": 100.0,
                                                "codigo_categoria": "2.04.01",
                                                "data_previsao": "23/01/2024",
                                                "id_conta_corrente": 4243124
                                ,
                                
                                                "codigo_lancamento_integracao": "1706039026",
                                                "codigo_cliente_fornecedor": 4214850,
                                                "data_vencimento": "23/01/2024",
                                                "valor_documento": 120.0,
                                                "codigo_categoria": "2.04.01",
                                                "data_previsao": "23/01/2024",
                                                "id_conta_corrente": 4243124
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  conta_pagar_lote_response
                """
                return self._chamar_api(
                    call= 'IncluirContaPagarPorLote',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def lancar_pagamento(self, **kargs) -> dict:
                """ 
                Efetua a baixa de um pagamento do contas a pagar. 
                :exemplo de uso:
                {
                
                "codigo_lancamento": 0,
                "codigo_lancamento_integracao": "",
                "codigo_baixa_integracao": "",
                "codigo_conta_corrente": "",
                "valor": 100.2,
                "desconto": 0,
                "juros": 0,
                "multa": 0,
                "data": "23/01/2024",
                "observacao": "Baixa de documento realizada via API."

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  conta_pagar_lancar_pagamento_resposta
                """
                return self._chamar_api(
                    call= 'LancarPagamento',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def listar_contas_pagar(self, **kargs) -> dict:
                """ 
                Listar as Contas a Pagar 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  lcpListarResponse
                """
                return self._chamar_api(
                    call= 'ListarContasPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def upsert_conta_pagar(self, **kargs) -> dict:
                """ 
                Upsert do Contas a Pagar 
                :exemplo de uso:
                {
                
                "codigo_lancamento_integracao": "1706039026",
                "codigo_cliente_fornecedor": 4214850,
                "data_vencimento": "23/01/2024",
                "valor_documento": 100.0,
                "codigo_categoria": "2.04.01",
                "data_previsao": "23/01/2024",
                "id_conta_corrente": 4243124

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  conta_pagar_cadastro_response
                """
                return self._chamar_api(
                    call= 'UpsertContaPagar',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def upsert_conta_pagar_por_lote(self, **kargs) -> dict:
                """ 
                Efetua o UPSERT do Contas a Pagar por Lote 
                :exemplo de uso:
                {
                
                "lote": 100,
                "conta_pagar_cadastro": [
                                
                                                "codigo_lancamento_integracao": "1706039026",
                                                "codigo_cliente_fornecedor": 4214850,
                                                "data_vencimento": "23/01/2024",
                                                "valor_documento": 100.0,
                                                "codigo_categoria": "2.04.01",
                                                "data_previsao": "23/01/2024",
                                                "id_conta_corrente": 4243124
                                ,
                                
                                                "codigo_lancamento_integracao": "1706039026",
                                                "codigo_cliente_fornecedor": 4214850,
                                                "data_vencimento": "23/01/2024",
                                                "valor_documento": 120.0,
                                                "codigo_categoria": "2.04.01",
                                                "data_previsao": "23/01/2024",
                                                "id_conta_corrente": 4243124
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contapagar/
                :retorno:  conta_pagar_lote_response
                """
                return self._chamar_api(
                    call= 'UpsertContaPagarPorLote',
                    endpoint= 'financas/contapagar/',
                    param = kargs
                )
            
    def alterar_conta_receber(self, **kargs) -> dict:
                """ 
                Altera um conta a receber 
                :exemplo de uso:
                {
                
                "codigo_lancamento_integracao": "1706040909",
                "codigo_cliente_fornecedor": 4214850,
                "data_vencimento": "23/01/2024",
                "valor_documento": 100.0,
                "codigo_categoria": "1.01.02",
                "data_previsao": "23/01/2024",
                "id_conta_corrente": 4243124

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_cadastro_response
                """
                return self._chamar_api(
                    call= 'AlterarContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def cancelar_conta_receber(self, **kargs) -> dict:
                """ 
                Cancelamento do boleto gerado de uma conta a receber 
                :exemplo de uso:
                {
                
                "chave_lancamento": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_cadastro_response
                """
                return self._chamar_api(
                    call= 'CancelarContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def cancelar_recebimento(self, **kargs) -> dict:
                """ 
                Efetua o cancelamento de um recebimento de Contas a Receber. 
                :exemplo de uso:
                {
                
                "codigo_baixa": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_cancelar_recebimento_resposta
                """
                return self._chamar_api(
                    call= 'CancelarRecebimento',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def conciliar_recebimento(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_baixa": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_conciliar_response
                """
                return self._chamar_api(
                    call= 'ConciliarRecebimento',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def consultar_conta_receber(self, **kargs) -> dict:
                """ 
                Consulta uma Conta a Receber 
                :exemplo de uso:
                {
                
                "codigo_lancamento_omie": 0,
                "codigo_lancamento_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_cadastro
                """
                return self._chamar_api(
                    call= 'ConsultarContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def desconciliar_recebimento(self, **kargs) -> dict:
                """ 
                Desconciliar o Recebimento 
                :exemplo de uso:
                {
                
                "codigo_baixa": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_conciliar_response
                """
                return self._chamar_api(
                    call= 'DesconciliarRecebimento',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def excluir_conta_receber(self, **kargs) -> dict:
                """ 
                Exclui uma conta a receber 
                :exemplo de uso:
                {
                
                "chave_lancamento": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_cadastro_response
                """
                return self._chamar_api(
                    call= 'ExcluirContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def incluir_conta_receber(self, **kargs) -> dict:
                """ 
                Inclui uma conta a Receber 
                :exemplo de uso:
                {
                
                "codigo_lancamento_integracao": "1706040909",
                "codigo_cliente_fornecedor": 4214850,
                "data_vencimento": "23/01/2024",
                "valor_documento": 100.0,
                "codigo_categoria": "1.01.02",
                "data_previsao": "23/01/2024",
                "id_conta_corrente": 4243124

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_cadastro_response
                """
                return self._chamar_api(
                    call= 'IncluirContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def incluir_conta_receber_por_lote(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "lote": 100,
                "conta_receber_cadastro": [
                                
                                                "codigo_lancamento_integracao": "1706040909",
                                                "codigo_cliente_fornecedor": 4214850,
                                                "data_vencimento": "23/01/2024",
                                                "valor_documento": 100.0,
                                                "codigo_categoria": "1.01.02",
                                                "data_previsao": "23/01/2024",
                                                "id_conta_corrente": 4243124
                                ,
                                
                                                "codigo_lancamento_integracao": "1706040909",
                                                "codigo_cliente_fornecedor": 4214850,
                                                "data_vencimento": "23/01/2024",
                                                "valor_documento": 120.0,
                                                "codigo_categoria": "1.01.02",
                                                "data_previsao": "23/01/2024",
                                                "id_conta_corrente": 4243124
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_lote_response
                """
                return self._chamar_api(
                    call= 'IncluirContaReceberPorLote',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def lancar_recebimento(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_lancamento": 0,
                "codigo_baixa": 0,
                "codigo_conta_corrente": 0,
                "valor": 0,
                "data": "",
                "observacao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_lancar_recebimento_resposta
                """
                return self._chamar_api(
                    call= 'LancarRecebimento',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def listar_contas_receber(self, **kargs) -> dict:
                """ 
                Lista as contas a receber cadastradas. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  lcrListarResponse
                """
                return self._chamar_api(
                    call= 'ListarContasReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def upsert_conta_receber(self, **kargs) -> dict:
                """ 
                Executa o Upsert do Contas a receber 
                :exemplo de uso:
                {
                
                "codigo_lancamento_integracao": "1706040909",
                "codigo_cliente_fornecedor": 4214850,
                "data_vencimento": "23/01/2024",
                "valor_documento": 100.0,
                "codigo_categoria": "1.01.02",
                "data_previsao": "23/01/2024",
                "id_conta_corrente": 4243124

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_cadastro_response
                """
                return self._chamar_api(
                    call= 'UpsertContaReceber',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def upsert_conta_receber_por_lote(self, **kargs) -> dict:
                """ 
                Efetua o UPSERT do Contas a Receber por Lote. 
                :exemplo de uso:
                {
                
                "lote": 100,
                "conta_receber_cadastro": [
                                
                                                "codigo_lancamento_integracao": "1706040909",
                                                "codigo_cliente_fornecedor": 4214850,
                                                "data_vencimento": "23/01/2024",
                                                "valor_documento": 100.0,
                                                "codigo_categoria": "1.01.02",
                                                "data_previsao": "23/01/2024",
                                                "id_conta_corrente": 4243124
                                ,
                                
                                                "codigo_lancamento_integracao": "1706040909",
                                                "codigo_cliente_fornecedor": 4214850,
                                                "data_vencimento": "23/01/2024",
                                                "valor_documento": 120.0,
                                                "codigo_categoria": "1.01.02",
                                                "data_previsao": "23/01/2024",
                                                "id_conta_corrente": 4243124
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceber/
                :retorno:  conta_receber_lote_response
                """
                return self._chamar_api(
                    call= 'UpsertContaReceberPorLote',
                    endpoint= 'financas/contareceber/',
                    param = kargs
                )
            
    def cancelar_boleto(self, **kargs) -> dict:
                """ 
                Cancela o Boleto. 
                :exemplo de uso:
                {
                
                "nCodTitulo": 0,
                "cCodIntTitulo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceberboleto/
                :retorno:  boletoCancelarResponse
                """
                return self._chamar_api(
                    call= 'CancelarBoleto',
                    endpoint= 'financas/contareceberboleto/',
                    param = kargs
                )
            
    def gerar_boleto(self, **kargs) -> dict:
                """ 
                Gera um Boleto referente a um Contas a Receber. 
                :exemplo de uso:
                {
                
                "nCodTitulo": 0,
                "cCodIntTitulo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceberboleto/
                :retorno:  boletoGerarResponse
                """
                return self._chamar_api(
                    call= 'GerarBoleto',
                    endpoint= 'financas/contareceberboleto/',
                    param = kargs
                )
            
    def obter_boleto(self, **kargs) -> dict:
                """ 
                Disponibiliza o link de Download do Boleto. 
                :exemplo de uso:
                {
                
                "nCodTitulo": 0,
                "cCodIntTitulo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceberboleto/
                :retorno:  boletoObterResponse
                """
                return self._chamar_api(
                    call= 'ObterBoleto',
                    endpoint= 'financas/contareceberboleto/',
                    param = kargs
                )
            
    def prorrogar_boleto(self, **kargs) -> dict:
                """ 
                Prorroga o vencimento do Boleto. 
                :exemplo de uso:
                {
                
                "nCodTitulo": 0,
                "cCodIntTitulo": "",
                "dDtVenc": "23/01/2024"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/contareceberboleto/
                :retorno:  boletoProrrogarResponse
                """
                return self._chamar_api(
                    call= 'ProrrogarBoleto',
                    endpoint= 'financas/contareceberboleto/',
                    param = kargs
                )
            
    def cancelar_pix(self, **kargs) -> dict:
                """ 
                Efetua o cancelamento de um PIX 
                :exemplo de uso:
                {
                
                "nIdPix": 0,
                "cCodIntPix": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pix/
                :retorno:  CancelarPixResponse
                """
                return self._chamar_api(
                    call= 'CancelarPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def gerar_pix(self, **kargs) -> dict:
                """ 
                Gera o QrCode de um PIX. 
                :exemplo de uso:
                {
                
                "cCodIntPix": "1670867357",
                "nIdCliente": 0,
                "vValor": 1.99,
                "nIdConta": 0,
                "cUrlNotif": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pix/
                :retorno:  GerarPixResponse
                """
                return self._chamar_api(
                    call= 'GerarPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def gerar_qr_code_pix(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nIdConta": 0,
                "vValor": 1.99

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pix/
                :retorno:  GerarQrCodePixResponse
                """
                return self._chamar_api(
                    call= 'GerarQrCodePix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def listar_pix(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pix/
                :retorno:  ListarPixResponse
                """
                return self._chamar_api(
                    call= 'ListarPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def listar_status_pix(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pix/
                :retorno:  ListarStatusPixResponse
                """
                return self._chamar_api(
                    call= 'ListarStatusPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def obter_pix(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nIdPix": 0,
                "cCodIntPix": "",
                "nCodTitulo": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pix/
                :retorno:  ObterPixResponse
                """
                return self._chamar_api(
                    call= 'ObterPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def obter_status_pix(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nIdPix": 0,
                "cCodIntPix": "",
                "nCodTitulo": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pix/
                :retorno:  ObterStatusPixResponse
                """
                return self._chamar_api(
                    call= 'ObterStatusPix',
                    endpoint= 'financas/pix/',
                    param = kargs
                )
            
    def listar_extrato(self, **kargs) -> dict:
                """ 
                Listagem do Extrato 
                :exemplo de uso:
                {
                
                "nCodCC": 0,
                "cCodIntCC": "",
                "dPeriodoInicial": "",
                "dPeriodoFinal": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/extrato/
                :retorno:  eccListarExtratoResponse
                """
                return self._chamar_api(
                    call= 'ListarExtrato',
                    endpoint= 'financas/extrato/',
                    param = kargs
                )
            
    def listar_orcamentos(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nAno": 2018,
                "nMes": 3

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/caixa/
                :retorno:  ocprListarResponse
                """
                return self._chamar_api(
                    call= 'ListarOrcamentos',
                    endpoint= 'financas/caixa/',
                    param = kargs
                )
            
    def obter_u_r_l_boleto(self, **kargs) -> dict:
                """ 
                DEPRECATED 
                :exemplo de uso:
                {
                
                "nCodTitulo": 0,
                "cCodIntTitulo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pesquisartitulos/
                :retorno:  ltLinkBoletoResponse
                """
                return self._chamar_api(
                    call= 'ObterURLBoleto',
                    endpoint= 'financas/pesquisartitulos/',
                    param = kargs
                )
            
    def pesquisar_excluidos(self, **kargs) -> dict:
                """ 
                DEPRECATED 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pesquisartitulos/
                :retorno:  ltListarExcluidosResponse
                """
                return self._chamar_api(
                    call= 'PesquisarExcluidos',
                    endpoint= 'financas/pesquisartitulos/',
                    param = kargs
                )
            
    def pesquisar_lancamentos(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/financas/pesquisartitulos/
                :retorno:  ltPesquisarResponse
                """
                return self._chamar_api(
                    call= 'PesquisarLancamentos',
                    endpoint= 'financas/pesquisartitulos/',
                    param = kargs
                )
            
    def listar_movimentos(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20,
                "codigo_local_estoque": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/movestoque/
                :retorno:  epListarResponse
                """
                return self._chamar_api(
                    call= 'ListarMovimentos',
                    endpoint= 'estoque/movestoque/',
                    param = kargs
                )
            
    def obter_resumo_contador(self, **kargs) -> dict:
                """ 
                Obtem o resumo do painel do contador. 
                :exemplo de uso:
                {
                
                "dDataInicio": "",
                "dDataFim": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/contador/resumo/
                :retorno:  ObterResumoContadorResponse
                """
                return self._chamar_api(
                    call= 'ObterResumoContador',
                    endpoint= 'contador/resumo/',
                    param = kargs
                )
            
    def consultar_banco(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/bancos/
                :retorno:  fin_banco_cadastro
                """
                return self._chamar_api(
                    call= 'ConsultarBanco',
                    endpoint= 'geral/bancos/',
                    param = kargs
                )
            
    def listar_bancos(self, **kargs) -> dict:
                """ 
                Exibe uma lista com os banco cadastrados. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 100

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/bancos/
                :retorno:  fin_bancos_list_response
                """
                return self._chamar_api(
                    call= 'ListarBancos',
                    endpoint= 'geral/bancos/',
                    param = kargs
                )
            
    def consultar_tipo_documento(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo": "9999"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tiposdoc/
                :retorno:  tipo_documento_cadastro
                """
                return self._chamar_api(
                    call= 'ConsultarTipoDocumento',
                    endpoint= 'geral/tiposdoc/',
                    param = kargs
                )
            
    def pesquisar_tipo_documento(self, **kargs) -> dict:
                """ 
                Pesquisa o tipo de documento 
                :exemplo de uso:
                {
                
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tiposdoc/
                :retorno:  tipo_documento_pesquisa_response
                """
                return self._chamar_api(
                    call= 'PesquisarTipoDocumento',
                    endpoint= 'geral/tiposdoc/',
                    param = kargs
                )
            
    def listar_tipos_c_c(self, **kargs) -> dict:
                """ 
                Listar os tipos de contas correntes. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/tipocc/
                :retorno:  tipoCCListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTiposCC',
                    endpoint= 'geral/tipocc/',
                    param = kargs
                )
            
    def listar_cadastro_d_r_e(self, **kargs) -> dict:
                """ 
                Lista as contas do DRE 
                :exemplo de uso:
                {
                
                "apenasContasAtivas": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/dre/
                :retorno:  dreCadastroListResponse
                """
                return self._chamar_api(
                    call= 'ListarCadastroDRE',
                    endpoint= 'geral/dre/',
                    param = kargs
                )
            
    def consultar_final_transf(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "banco": "104",
                "codigo": "01"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/finaltransf/
                :retorno:  cadastros
                """
                return self._chamar_api(
                    call= 'ConsultarFinalTransf',
                    endpoint= 'geral/finaltransf/',
                    param = kargs
                )
            
    def listar_final_transf(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/finaltransf/
                :retorno:  final_transf_list_response
                """
                return self._chamar_api(
                    call= 'ListarFinalTransf',
                    endpoint= 'geral/finaltransf/',
                    param = kargs
                )
            
    def listar_origem(self, **kargs) -> dict:
                """ 
                Lista Origem de pedidos. 
                :exemplo de uso:
                {
                
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/origempedido/
                :retorno:  origem_ped_listar_response
                """
                return self._chamar_api(
                    call= 'ListarOrigem',
                    endpoint= 'geral/origempedido/',
                    param = kargs
                )
            
    def listar_bandeiras(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/bandeiracartao/
                :retorno:  ListarBandeirasResponse
                """
                return self._chamar_api(
                    call= 'ListarBandeiras',
                    endpoint= 'geral/bandeiracartao/',
                    param = kargs
                )
            
    def alterar_produto(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_produto_integracao": "1706038658",
                "codigo": "teste0001",
                "descricao": "Produto de teste",
                "unidade": "UN"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_status
                """
                return self._chamar_api(
                    call= 'AlterarProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def associar_cod_int_produto(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_produto": 0,
                "codigo_produto_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_status
                """
                return self._chamar_api(
                    call= 'AssociarCodIntProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def consultar_produto(self, **kargs) -> dict:
                """ 
                Consulta um produto. 
                :exemplo de uso:
                {
                
                "codigo_produto": 0,
                "codigo_produto_integracao": "",
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_cadastro
                """
                return self._chamar_api(
                    call= 'ConsultarProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def excluir_produto(self, **kargs) -> dict:
                """ 
                Exclui um produto 
                :exemplo de uso:
                {
                
                "codigo_produto": 0,
                "codigo_produto_integracao": "",
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_status
                """
                return self._chamar_api(
                    call= 'ExcluirProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def incluir_produto(self, **kargs) -> dict:
                """ 
                Incluir um produto. 
                :exemplo de uso:
                {
                
                "codigo_produto_integracao": "1706038658",
                "codigo": "teste0001",
                "descricao": "Produto de teste",
                "unidade": "UN"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_status
                """
                return self._chamar_api(
                    call= 'IncluirProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def incluir_produtos_por_lote(self, **kargs) -> dict:
                """ 
                DEPRECATED 
                :exemplo de uso:
                {
                
                "lote": 123,
                "produto_servico_cadastro": [
                                
                                                "codigo_produto_integracao": "1628097039",
                                                "codigo": "teste1235",
                                                "descricao": "Produto de teste",
                                                "unidade": "UN",
                                                "ncm": "9504.50.00"
                                ,
                                
                                                "codigo_produto_integracao": "1628097040",
                                                "codigo": "teste1234",
                                                "descricao": "Produto de teste",
                                                "unidade": "UN",
                                                "ncm": "9504.50.00"
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_lote_response
                """
                return self._chamar_api(
                    call= 'IncluirProdutosPorLote',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def listar_produtos(self, **kargs) -> dict:
                """ 
                Lista completa do cadastro de produtos 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50,
                "apenas_importado_api": "N",
                "filtrar_apenas_omiepdv": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_listfull_response
                """
                return self._chamar_api(
                    call= 'ListarProdutos',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def listar_produtos_resumido(self, **kargs) -> dict:
                """ 
                Lista os produtos cadastrados 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50,
                "apenas_importado_api": "N",
                "filtrar_apenas_omiepdv": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_list_response
                """
                return self._chamar_api(
                    call= 'ListarProdutosResumido',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def upsert_produto(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_produto_integracao": "1706038658",
                "codigo": "teste0001",
                "descricao": "Produto de teste",
                "unidade": "UN"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_status
                """
                return self._chamar_api(
                    call= 'UpsertProduto',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def upsert_produtos_por_lote(self, **kargs) -> dict:
                """ 
                DEPRECATED 
                :exemplo de uso:
                {
                
                "lote": 123,
                "produto_servico_cadastro": [
                                
                                                "codigo_produto_integracao": "1628097039",
                                                "codigo": "teste1235",
                                                "descricao": "Produto de teste 1235",
                                                "unidade": "UN",
                                                "ncm": "9504.50.00"
                                ,
                                
                                                "codigo_produto_integracao": "1628097040",
                                                "codigo": "teste1234",
                                                "descricao": "Produto de teste 1234",
                                                "unidade": "UN",
                                                "ncm": "9504.50.00"
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtos/
                :retorno:  produto_servico_lote_response
                """
                return self._chamar_api(
                    call= 'UpsertProdutosPorLote',
                    endpoint= 'geral/produtos/',
                    param = kargs
                )
            
    def alterar_caract_produto(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodProd": 0,
                "cCodIntProd": "",
                "nCodCaract": 0,
                "cCodIntCaract": "",
                "cConteudo": "",
                "cExibirItemNF": "S",
                "cExibirItemPedido": "S",
                "cExibirOrdemProd": "S"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/prodcaract/
                :retorno:  prcAlterarCaractResponse
                """
                return self._chamar_api(
                    call= 'AlterarCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def consultar_caract_produto(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodProd": 0,
                "cCodIntProd": "",
                "nCodCaract": 0,
                "cCodIntCaract": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/prodcaract/
                :retorno:  prcConsultarCaractResponse
                """
                return self._chamar_api(
                    call= 'ConsultarCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def excluir_caract_produto(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodProd": 0,
                "cCodIntProd": "",
                "nCodCaract": 0,
                "cCodIntCaract": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/prodcaract/
                :retorno:  prcExcluirCaractResponse
                """
                return self._chamar_api(
                    call= 'ExcluirCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def incluir_caract_produto(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodProd": 0,
                "cCodIntProd": "",
                "nCodCaract": 0,
                "cCodIntCaract": "",
                "cConteudo": "",
                "cExibirItemNF": "S",
                "cExibirItemPedido": "S",
                "cExibirOrdemProd": "S"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/prodcaract/
                :retorno:  prcIncluirCaractResponse
                """
                return self._chamar_api(
                    call= 'IncluirCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def listar_caract_produto(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50,
                "nCodProd": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/prodcaract/
                :retorno:  prcListarCaractResponse
                """
                return self._chamar_api(
                    call= 'ListarCaractProduto',
                    endpoint= 'geral/prodcaract/',
                    param = kargs
                )
            
    def alterar_estrutura(self, **kargs) -> dict:
                """ 
                Alterar a estrutura de um produto. 
                :exemplo de uso:
                {
                
                "idProduto": 0,
                "intProduto": "",
                "itemMalhaAlterar": [
                                
                                                "idMalha": 0,
                                                "intMalha": "",
                                                "idProdMalha": 0,
                                                "intProdMalha": "",
                                                "quantProdMalha": 0,
                                                "percPerdaProdMalha": 0,
                                                "obsProdMalha": ""
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/malha/
                :retorno:  malhaAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarEstrutura',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def consultar_estrutura(self, **kargs) -> dict:
                """ 
                Consulta a estrutura do produto. 
                :exemplo de uso:
                {
                
                "idProduto": 0,
                "intProduto": "",
                "codProduto": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/malha/
                :retorno:  malhaConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarEstrutura',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def excluir_estrutura(self, **kargs) -> dict:
                """ 
                Excluir item da estrutura de um produto. 
                :exemplo de uso:
                {
                
                "idProduto": 0,
                "intProduto": "",
                "idMalha": 0,
                "intMalha": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/malha/
                :retorno:  malhaExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirEstrutura',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def incluir_estrutura(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "idProduto": 0,
                "intProduto": "",
                "itemMalhaIncluir": [
                                
                                                "intMalha": "",
                                                "idProdMalha": 0,
                                                "intProdMalha": "",
                                                "quantProdMalha": 0,
                                                "percPerdaProdMalha": 0,
                                                "obsProdMalha": ""
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/malha/
                :retorno:  malhaIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirEstrutura',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def listar_estruturas(self, **kargs) -> dict:
                """ 
                Lista as estruturas de produtos. 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 100

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/malha/
                :retorno:  malhaPesquisarResponse
                """
                return self._chamar_api(
                    call= 'ListarEstruturas',
                    endpoint= 'geral/malha/',
                    param = kargs
                )
            
    def alterar_componentes_kit(self, **kargs) -> dict:
                """ 
                Inclui/Altera/Exclui os componentes do KIT. 
                :exemplo de uso:
                {
                
                "codigo_produto": 0,
                "componentes_kit": [
                                
                                                "acao_componente": "I",
                                                "codigo_componente": 0,
                                                "codigo_produto_componente": 0,
                                                "valor_unitario_componente": 1.99,
                                                "quantidade_componente": 1,
                                                "codigo_local_estoque": 0
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/produtoskit/
                :retorno:  AlterarCompKitResponse
                """
                return self._chamar_api(
                    call= 'AlterarComponentesKit',
                    endpoint= 'geral/produtoskit/',
                    param = kargs
                )
            
    def alterar_req(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codCateg": "2.04.06",
                "codIntReqCompra": "INT001",
                "codProj": 0,
                "codReqCompra": 0,
                "dtSugestao": "23/01/2024",
                "obsIntReqCompra": "",
                "obsReqCompra": "",
                "ItensReqCompra": [
                                
                                                "codIntItem": "                    ",
                                                "codIntProd": "",
                                                "codItem": 200000003040063,
                                                "codProd": 993848,
                                                "obsItem": "",
                                                "precoUnit": 12,
                                                "qtde": 1
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/requisicaocompra/
                :retorno:  rcStatus
                """
                return self._chamar_api(
                    call= 'AlterarReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def consultar_req(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codIntReqCompra": "INT001",
                "codReqCompra": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/requisicaocompra/
                :retorno:  requisicaoCadastro
                """
                return self._chamar_api(
                    call= 'ConsultarReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def excluir_req(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codIntReqCompra": "INT001",
                "codReqCompra": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/requisicaocompra/
                :retorno:  rcStatus
                """
                return self._chamar_api(
                    call= 'ExcluirReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def incluir_req(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codCateg": "2.04.06",
                "codIntReqCompra": "INT001",
                "codProj": 0,
                "codReqCompra": 0,
                "dtSugestao": "23/01/2024",
                "obsIntReqCompra": "",
                "obsReqCompra": "",
                "ItensReqCompra": [
                                
                                                "codIntItem": "                    ",
                                                "codIntProd": "",
                                                "codItem": 200000003040063,
                                                "codProd": 993848,
                                                "obsItem": "",
                                                "precoUnit": 12,
                                                "qtde": 1
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/requisicaocompra/
                :retorno:  rcStatus
                """
                return self._chamar_api(
                    call= 'IncluirReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def pesquisar_req(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/requisicaocompra/
                :retorno:  rcListarResponse
                """
                return self._chamar_api(
                    call= 'PesquisarReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def upsert_req(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codCateg": "2.04.06",
                "codIntReqCompra": "INT001",
                "codProj": 0,
                "codReqCompra": 0,
                "dtSugestao": "23/01/2024",
                "obsIntReqCompra": "",
                "obsReqCompra": "",
                "ItensReqCompra": [
                                
                                                "codIntItem": "                    ",
                                                "codIntProd": "",
                                                "codItem": 200000003040063,
                                                "codProd": 993848,
                                                "obsItem": "",
                                                "precoUnit": 12,
                                                "qtde": 1
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/requisicaocompra/
                :retorno:  rcStatus
                """
                return self._chamar_api(
                    call= 'UpsertReq',
                    endpoint= 'produtos/requisicaocompra/',
                    param = kargs
                )
            
    def altera_ped_compra(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cabecalho_alterar": 
                                "cCodIntPed": "INT001",
                                "dDtPrevisao": "05/05/2024",
                                "cCodParc": "",
                                "nQtdeParc": 3,
                                "nCodFor": "14170458",
                                "cCodIntFor": "",
                                "cCodCateg": "",
                                "nCodCompr": 0,
                                "cContato": "",
                                "cContrato": "",
                                "nCodCC": "1208238",
                                "nCodIntCC": 0,
                                "nCodProj": 0,
                                "cObs": "Pedido alterado via API",
                                "cObsInt": "Pedido alterado via API"
                ,
                "frete_alterar": 
                                "nCodTransp": 0,
                                "cCodIntTransp": "",
                                "cTpFrete": "9",
                                "cPlaca": "XXX-9999",
                                "cUF": "SP",
                                "nQtdVol": 5,
                                "cEspVol": "",
                                "cMarVol": "",
                                "cNumVol": "",
                                "nPesoLiq": 5.0,
                                "nPesoBruto": 10.0,
                                "nValFrete": 50.0,
                                "nValSeguro": 10.0,
                                "cLacre": "",
                                "nValOutras": 0.0
                ,
                "departamentos_alterar": [
                                
                                                "cCodDepto": "200000002498904",
                                                "nPerc": 90
                                ,
                                
                                                "cCodDepto": "200000002498905",
                                                "nPerc": 10
                                
                ],
                "produtos_alterar": [
                                
                                                "cCodIntItem": "ITEM001",
                                                "cCodIntProd": "",
                                                "nCodProd": "2037060",
                                                "cProduto": "",
                                                "cDescricao": "",
                                                "cNCM": "",
                                                "cUnidade": "",
                                                "cEAN": "",
                                                "nPesoLiq": 0,
                                                "nPesoBruto": 0,
                                                "nQtde": 10,
                                                "nValUnit": 200,
                                                "nDesconto": 0.0,
                                                "nValorIcms": 360.0,
                                                "nValorSt": 0.0,
                                                "nValorIpi": 20.0,
                                                "nValorPis": 33.0,
                                                "nValorCofins": 152.0,
                                                "cObs": "Item alterado via API",
                                                "cMkpAtuPv": "N",
                                                "cMkpAtuSm": "N",
                                                "nMkpPerc": 0,
                                                "codigo_local_estoque": "",
                                                "cCodCateg": ""
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidocompra/
                :retorno:  com_pedido_alterar_response
                """
                return self._chamar_api(
                    call= 'AlteraPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def consultar_ped_compra(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodPed": 0,
                "cCodIntPed": "INT001",
                "cNumero": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidocompra/
                :retorno:  pedidos_pesquisa
                """
                return self._chamar_api(
                    call= 'ConsultarPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def excluir_ped_compra(self, **kargs) -> dict:
                """ 
                Excluir um Pedido de Compra 
                :exemplo de uso:
                {
                
                "nCodPed": 0,
                "cCodIntPed": "INT001"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidocompra/
                :retorno:  com_pedido_excluir_response
                """
                return self._chamar_api(
                    call= 'ExcluirPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def incluir_ped_compra(self, **kargs) -> dict:
                """ 
                Incluir um Pedido de Compra 
                :exemplo de uso:
                {
                
                "cabecalho_incluir": 
                                "cCodIntPed": "INT001",
                                "dDtPrevisao": "17/03/2024",
                                "cCodParc": "",
                                "nQtdeParc": 1,
                                "nCodFor": "14170458",
                                "cCodIntFor": "",
                                "cCodCateg": "",
                                "nCodCompr": 0,
                                "cContato": "",
                                "cContrato": "",
                                "nCodCC": "1208238",
                                "nCodIntCC": 0,
                                "nCodProj": 0,
                                "cNumPedido": "63411",
                                "cObs": "Pedido incluido via API",
                                "cObsInt": "Pedido Cadastrado via API"
                ,
                "frete_incluir": 
                                "nCodTransp": 0,
                                "cCodIntTransp": "",
                                "cTpFrete": "9",
                                "cPlaca": "XXX-9999",
                                "cUF": "SP",
                                "nQtdVol": 5,
                                "cEspVol": "",
                                "cMarVol": "",
                                "cNumVol": "",
                                "nPesoLiq": 0.0,
                                "nPesoBruto": 0.0,
                                "nValFrete": 0,
                                "nValSeguro": 0.0,
                                "cLacre": "",
                                "nValOutras": 0.0
                ,
                "departamentos_incluir": [
                                
                                                "cCodDepto": "200000002498904",
                                                "nPerc": 50
                                ,
                                
                                                "cCodDepto": "200000002498905",
                                                "nPerc": 50
                                
                ],
                "produtos_incluir": [
                                
                                                "cCodIntItem": "ITEM001",
                                                "cCodIntProd": "",
                                                "nCodProd": "2037060",
                                                "cProduto": "",
                                                "cDescricao": "",
                                                "cNCM": "",
                                                "cUnidade": "",
                                                "cEAN": "",
                                                "nPesoLiq": 0,
                                                "nPesoBruto": 0,
                                                "nQtde": 10,
                                                "nValUnit": 200,
                                                "nDesconto": 0.0,
                                                "nValorIcms": 360.0,
                                                "nValorSt": 0.0,
                                                "nValorIpi": 20.0,
                                                "nValorPis": 33.0,
                                                "nValorCofins": 152.0,
                                                "cObs": "",
                                                "cMkpAtuPv": "N",
                                                "cMkpAtuSm": "N",
                                                "nMkpPerc": 0,
                                                "codigo_local_estoque": "",
                                                "cCodCateg": ""
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidocompra/
                :retorno:  com_pedido_incluir_response
                """
                return self._chamar_api(
                    call= 'IncluirPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def pesquisar_ped_compra(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegsPorPagina": 10,
                "lApenasImportadoApi": "F",
                "lExibirPedidosPendentes": "T",
                "lExibirPedidosFaturados": "F",
                "lExibirPedidosRecebidos": "F",
                "lExibirPedidosCancelados": "F",
                "lExibirPedidosEncerrados": "F",
                "lExibirPedidosRecParciais": "F",
                "lExibirPedidosFatParciais": "F",
                "dDataInicial": "01/01/2021",
                "dDataFinal": "31/12/2021",
                "lApenasAlterados": "F"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidocompra/
                :retorno:  com_pedido_pesquisar_response
                """
                return self._chamar_api(
                    call= 'PesquisarPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def upsert_ped_compra(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cabecalho_upsert": 
                                "cCodIntPed": "INT001",
                                "dDtPrevisao": "10/05/2024",
                                "cCodParc": "",
                                "nQtdeParc": 3,
                                "nCodFor": "14170458",
                                "cCodIntFor": "",
                                "cCodCateg": "",
                                "nCodCompr": 0,
                                "cContato": "",
                                "cContrato": "",
                                "nCodCC": "1208238",
                                "nCodIntCC": 0,
                                "nCodProj": 0,
                                "cObs": "Pedido alterado via API - Upsert",
                                "cObsInt": "Pedido alterado via API - Upsert"
                ,
                "frete_upsert": 
                                "nCodTransp": 0,
                                "cCodIntTransp": "",
                                "cTpFrete": "9",
                                "cPlaca": "XXX-9999",
                                "cUF": "SP",
                                "nQtdVol": 5,
                                "cEspVol": "",
                                "cMarVol": "",
                                "cNumVol": "",
                                "nPesoLiq": 5.0,
                                "nPesoBruto": 10.0,
                                "nValFrete": 50.0,
                                "nValSeguro": 10.0,
                                "cLacre": "",
                                "nValOutras": 0.0
                ,
                "departamentos_upsert": [
                                
                                                "cCodDepto": "200000002498904",
                                                "nPerc": 40
                                ,
                                
                                                "cCodDepto": "200000002498905",
                                                "nPerc": 30
                                ,
                                
                                                "cCodDepto": "200000002498906",
                                                "nPerc": 15
                                ,
                                
                                                "cCodDepto": "200000002498907",
                                                "nPerc": 15
                                
                ],
                "produtos_upsert": [
                                
                                                "cCodIntItem": "ITEM001",
                                                "cCodIntProd": "",
                                                "nCodProd": "2037060",
                                                "cProduto": "",
                                                "cDescricao": "",
                                                "cNCM": "",
                                                "cUnidade": "",
                                                "cEAN": "",
                                                "nPesoLiq": 0,
                                                "nPesoBruto": 0,
                                                "nQtde": 10,
                                                "nValUnit": 200,
                                                "nDesconto": 0.0,
                                                "nValorIcms": 360.0,
                                                "nValorSt": 0.0,
                                                "nValorIpi": 20.0,
                                                "nValorPis": 33.0,
                                                "nValorCofins": 152.0,
                                                "cObs": "Item alterado via API - Upsert",
                                                "cMkpAtuPv": "N",
                                                "cMkpAtuSm": "N",
                                                "nMkpPerc": 0,
                                                "codigo_local_estoque": "",
                                                "cCodCateg": ""
                                ,
                                
                                                "cCodIntItem": "ITEM002",
                                                "cCodIntProd": "",
                                                "nCodProd": "2037060",
                                                "cProduto": "",
                                                "cDescricao": "",
                                                "cNCM": "",
                                                "cUnidade": "",
                                                "cEAN": "",
                                                "nPesoLiq": 0,
                                                "nPesoBruto": 0,
                                                "nQtde": 20,
                                                "nValUnit": 200,
                                                "nDesconto": 0.0,
                                                "nValorIcms": 720.0,
                                                "nValorSt": 0.0,
                                                "nValorIpi": 40.0,
                                                "nValorPis": 66.0,
                                                "nValorCofins": 304.0,
                                                "cObs": "Item inclu\u00eddo via API - Upsert",
                                                "cMkpAtuPv": "N",
                                                "cMkpAtuSm": "N",
                                                "nMkpPerc": 0,
                                                "codigo_local_estoque": "",
                                                "cCodCateg": ""
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidocompra/
                :retorno:  com_pedido_upsert_response
                """
                return self._chamar_api(
                    call= 'UpsertPedCompra',
                    endpoint= 'produtos/pedidocompra/',
                    param = kargs
                )
            
    def alterar_ordem_producao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodIntOP": "OP0001",
                                "dDtPrevisao": "23/01/2024",
                                "nCodProduto": 0,
                                "nQtde": 3
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/op/
                :retorno:  copAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def concluir_ordem_producao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOP": "",
                "nCodOP": 0,
                "dDtConclusao": "23/01/2024",
                "nQtdeProduzida": 3,
                "cObsConclusao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/op/
                :retorno:  copConcluirResponse
                """
                return self._chamar_api(
                    call= 'ConcluirOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def consultar_ordem_producao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOP": "",
                "nCodOP": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/op/
                :retorno:  copConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def excluir_ordem_producao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOP": "",
                "nCodOP": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/op/
                :retorno:  copExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def incluir_ordem_producao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodIntOP": "OP0001",
                                "dDtPrevisao": "23/01/2024",
                                "nCodProduto": 0,
                                "nQtde": 3
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/op/
                :retorno:  copIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def listar_ordem_producao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20,
                "dDtConclusaoDe": "23/01/2024",
                "dDtConclusaoAte": "23/01/2024"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/op/
                :retorno:  copListarResponse
                """
                return self._chamar_api(
                    call= 'ListarOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def reverter_ordem_producao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOP": "",
                "nCodOP": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/op/
                :retorno:  copReverterResponse
                """
                return self._chamar_api(
                    call= 'ReverterOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def upsert_ordem_producao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "identificacao": 
                                "cCodIntOP": "OP0001",
                                "dDtPrevisao": "23/01/2024",
                                "nCodProduto": 0,
                                "nQtde": 3
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/op/
                :retorno:  copUpsertResponse
                """
                return self._chamar_api(
                    call= 'UpsertOrdemProducao',
                    endpoint= 'produtos/op/',
                    param = kargs
                )
            
    def alterar_nota_ent(self, **kargs) -> dict:
                """ 
                Alterar nota de entrada 
                :exemplo de uso:
                {
                
                "cabec": 
                                "cCodIntNotaEnt": "NE1706037880",
                                "dPrevisao": "23/01/2024",
                                "nCodCli": 2370765
                ,
                "infAdic": 
                                "cCodCateg": "2.01.03"
                ,
                "produtos": [
                                
                                                "cCodItInt": "IT1706037880",
                                                "nCodProd": 426738565,
                                                "nQtde": 1,
                                                "nValUnit": 100,
                                                "cCFOP": "1.152"
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentrada/
                :retorno:  neAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def consultar_nota_ent(self, **kargs) -> dict:
                """ 
                Consultar nota de entrada 
                :exemplo de uso:
                {
                
                "nCodNotaEnt": 0,
                "cCodIntNotaEnt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentrada/
                :retorno:  neConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def excluir_nota_ent(self, **kargs) -> dict:
                """ 
                Excluir nota de entrada 
                :exemplo de uso:
                {
                
                "nCodNotaEnt": 0,
                "cCodIntNotaEnt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentrada/
                :retorno:  neExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def incluir_nota_ent(self, **kargs) -> dict:
                """ 
                Incluir nota de entrada 
                :exemplo de uso:
                {
                
                "cabec": 
                                "cCodIntNotaEnt": "NE1706037880",
                                "dPrevisao": "23/01/2024",
                                "nCodCli": 2370765
                ,
                "infAdic": 
                                "cCodCateg": "2.01.03"
                ,
                "produtos": [
                                
                                                "cCodItInt": "IT1706037880",
                                                "nCodProd": 426738565,
                                                "codigo_local_estoque": 464449588,
                                                "nQtde": 1,
                                                "nValUnit": 100,
                                                "cCFOP": "1.152",
                                                "PIS": 
                                                                "cSitTribPIS": "50"
                                                ,
                                                "COFINS": 
                                                                "cSitTribCOFINS": "01"
                                                
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentrada/
                :retorno:  neIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def listar_nota_ent(self, **kargs) -> dict:
                """ 
                Listagem de nota de entrada 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegistrosPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentrada/
                :retorno:  neListarResponse
                """
                return self._chamar_api(
                    call= 'ListarNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def status_nota_ent(self, **kargs) -> dict:
                """ 
                Status de nota de entrada 
                :exemplo de uso:
                {
                
                "nCodNotaEnt": 0,
                "cCodIntNotaEnt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentrada/
                :retorno:  neStatusResponse
                """
                return self._chamar_api(
                    call= 'StatusNotaEnt',
                    endpoint= 'produtos/notaentrada/',
                    param = kargs
                )
            
    def cancelar_nota_ent(self, **kargs) -> dict:
                """ 
                Cancelar nota de entrada 
                :exemplo de uso:
                {
                
                "nCodNotaEnt": 0,
                "cCodIntNotaEnt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentradafat/
                :retorno:  nefatCancelarResponse
                """
                return self._chamar_api(
                    call= 'CancelarNotaEnt',
                    endpoint= 'produtos/notaentradafat/',
                    param = kargs
                )
            
    def concluir_nota_ent(self, **kargs) -> dict:
                """ 
                Concluir nota de entrada 
                :exemplo de uso:
                {
                
                "nCodNotaEnt": 0,
                "cCodIntNotaEnt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentradafat/
                :retorno:  nefatConcluirResponse
                """
                return self._chamar_api(
                    call= 'ConcluirNotaEnt',
                    endpoint= 'produtos/notaentradafat/',
                    param = kargs
                )
            
    def conferir_nota_ent(self, **kargs) -> dict:
                """ 
                Conferir nota de entrada 
                :exemplo de uso:
                {
                
                "nCodNotaEnt": 0,
                "cCodIntNotaEnt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentradafat/
                :retorno:  nefatConferirResponse
                """
                return self._chamar_api(
                    call= 'ConferirNotaEnt',
                    endpoint= 'produtos/notaentradafat/',
                    param = kargs
                )
            
    def duplicar_nota_ent(self, **kargs) -> dict:
                """ 
                Duplicar nota de entrada 
                :exemplo de uso:
                {
                
                "nCodNotaEnt": 0,
                "cCodIntNotaEnt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notaentradafat/
                :retorno:  nefatDuplicarResponse
                """
                return self._chamar_api(
                    call= 'DuplicarNotaEnt',
                    endpoint= 'produtos/notaentradafat/',
                    param = kargs
                )
            
    def alterar_etapa_recebimento(self, **kargs) -> dict:
                """ 
                Alterar etapa recebimento NFe 
                :exemplo de uso:
                {
                
                "nIdReceb": 0,
                "cChaveNfe": "",
                "cEtapa": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/recebimentonfe/
                :retorno:  rcbtoAlterarEtapaResponse
                """
                return self._chamar_api(
                    call= 'AlterarEtapaRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def alterar_recebimento(self, **kargs) -> dict:
                """ 
                Alterar recebimento de NFe 
                :exemplo de uso:
                {
                
                "ide": 
                                "nIdReceb": 0,
                                "cChaveNfe": ""
                ,
                "itensRecebimentoEditar": 
                                "itensIde": 
                                                "nSequencia": 0,
                                                "cAcao": "IGNORAR"
                                
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/recebimentonfe/
                :retorno:  rcbtoAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def concluir_recebimento(self, **kargs) -> dict:
                """ 
                Concluir recebimento de NFe 
                :exemplo de uso:
                {
                
                "nIdReceb": 0,
                "cChaveNfe": "",
                "cEtapa": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/recebimentonfe/
                :retorno:  rcbtoConcluirResponse
                """
                return self._chamar_api(
                    call= 'ConcluirRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def consultar_recebimento(self, **kargs) -> dict:
                """ 
                Consultar recebimento de NFe 
                :exemplo de uso:
                {
                
                "nIdReceb": 0,
                "cChaveNfe": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/recebimentonfe/
                :retorno:  rcbtoConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def listar_recebimentos(self, **kargs) -> dict:
                """ 
                Listar recebimento de NFe 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegistrosPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/recebimentonfe/
                :retorno:  rcbtoListarResponse
                """
                return self._chamar_api(
                    call= 'ListarRecebimentos',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def reverter_recebimento(self, **kargs) -> dict:
                """ 
                Reverter recebimento NFe 
                :exemplo de uso:
                {
                
                "nIdReceb": 0,
                "cChaveNfe": "",
                "cEtapa": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/recebimentonfe/
                :retorno:  rcbtoReverterResponse
                """
                return self._chamar_api(
                    call= 'ReverterRecebimento',
                    endpoint= 'produtos/recebimentonfe/',
                    param = kargs
                )
            
    def alterar_familia(self, **kargs) -> dict:
                """ 
                Altera uma familia de produto 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codInt": "FA1706039033",
                "codFamilia": "",
                "nomeFamilia": "",
                "inativo": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/familias/
                :retorno:  famStatus
                """
                return self._chamar_api(
                    call= 'AlterarFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def consultar_familia(self, **kargs) -> dict:
                """ 
                Consulta uma familia de produto 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/familias/
                :retorno:  famConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def excluir_familia(self, **kargs) -> dict:
                """ 
                Exclui uma familia de produto 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/familias/
                :retorno:  famStatus
                """
                return self._chamar_api(
                    call= 'ExcluirFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def incluir_familia(self, **kargs) -> dict:
                """ 
                Inclui uma familia de produto 
                :exemplo de uso:
                {
                
                "codInt": "FA1706039033",
                "codFamilia": "",
                "nomeFamilia": "",
                "inativo": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/familias/
                :retorno:  famStatus
                """
                return self._chamar_api(
                    call= 'IncluirFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def pesquisar_familias(self, **kargs) -> dict:
                """ 
                Listagem de familias cadastradas 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/familias/
                :retorno:  famListarResponse
                """
                return self._chamar_api(
                    call= 'PesquisarFamilias',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def upsert_familia(self, **kargs) -> dict:
                """ 
                Inclui / Altera uma familia de produto 
                :exemplo de uso:
                {
                
                "codigo": 0,
                "codInt": "FA1706039033",
                "codFamilia": "",
                "nomeFamilia": "",
                "inativo": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/familias/
                :retorno:  famStatus
                """
                return self._chamar_api(
                    call= 'UpsertFamilia',
                    endpoint= 'geral/familias/',
                    param = kargs
                )
            
    def listar_unidades(self, **kargs) -> dict:
                """ 
                Lista as unidades de medidas 
                :exemplo de uso:
                {
                
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/unidade/
                :retorno:  unidade_cadastro_lista
                """
                return self._chamar_api(
                    call= 'ListarUnidades',
                    endpoint= 'geral/unidade/',
                    param = kargs
                )
            
    def listar_compradores(self, **kargs) -> dict:
                """ 
                Lista os compradores cadastrados. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/comprador/
                :retorno:  CompradorListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCompradores',
                    endpoint= 'estoque/comprador/',
                    param = kargs
                )
            
    def listar_produto_fornecedor(self, **kargs) -> dict:
                """ 
                Listar os produtos por fornecedores. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/produtofornecedor/
                :retorno:  pfListarResponse
                """
                return self._chamar_api(
                    call= 'ListarProdutoFornecedor',
                    endpoint= 'estoque/produtofornecedor/',
                    param = kargs
                )
            
    def listar_formas_pag_vendas(self, **kargs) -> dict:
                """ 
                Lista as formas de pagmento de vendas. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/formaspagvendas/
                :retorno:  venparListarResponse
                """
                return self._chamar_api(
                    call= 'ListarFormasPagVendas',
                    endpoint= 'produtos/formaspagvendas/',
                    param = kargs
                )
            
    def consultar_n_c_m(self, **kargs) -> dict:
                """ 
                Consulta um NCM 
                :exemplo de uso:
                {
                
                "cCodigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/ncm/
                :retorno:  ncmConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarNCM',
                    endpoint= 'produtos/ncm/',
                    param = kargs
                )
            
    def listar_n_c_m(self, **kargs) -> dict:
                """ 
                Lista os NCMs cadastrados. 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/ncm/
                :retorno:  ncmListarResponse
                """
                return self._chamar_api(
                    call= 'ListarNCM',
                    endpoint= 'produtos/ncm/',
                    param = kargs
                )
            
    def listar_cenarios(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/cenarios/
                :retorno:  cenariosListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCenarios',
                    endpoint= 'geral/cenarios/',
                    param = kargs
                )
            
    def listar_impostos_cenario(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_cliente_integracao": "CLI00001",
                "consumo_final": "N",
                "codigo_produto_integracao": "PRD00001",
                "codigo_cenario": 152055

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/cenarios/
                :retorno:  cenariosImpostosListarResponse
                """
                return self._chamar_api(
                    call= 'ListarImpostosCenario',
                    endpoint= 'geral/cenarios/',
                    param = kargs
                )
            
    def listar_c_f_o_p(self, **kargs) -> dict:
                """ 
                Listar as CFOPs 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cfop/
                :retorno:  cfopListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCFOP',
                    endpoint= 'produtos/cfop/',
                    param = kargs
                )
            
    def listar_c_s_t(self, **kargs) -> dict:
                """ 
                Listar os CSTs do ICMS 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/icmscst/
                :retorno:  cstListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCST',
                    endpoint= 'produtos/icmscst/',
                    param = kargs
                )
            
    def listar_c_s_o_s_n(self, **kargs) -> dict:
                """ 
                Listar os CSOSN do ICMS. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/icmscsosn/
                :retorno:  csosnListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCSOSN',
                    endpoint= 'produtos/icmscsosn/',
                    param = kargs
                )
            
    def listar_orig_merc(self, **kargs) -> dict:
                """ 
                Listar a origem da mercadoria do ICMS. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/icmsorigem/
                :retorno:  origMercListarResponse
                """
                return self._chamar_api(
                    call= 'ListarOrigMerc',
                    endpoint= 'produtos/icmsorigem/',
                    param = kargs
                )
            
    def listar_cst_pis(self, **kargs) -> dict:
                """ 
                Listar o CST do PIS. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/piscst/
                :retorno:  pisCstListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCstPis',
                    endpoint= 'produtos/piscst/',
                    param = kargs
                )
            
    def listar_cst_cofins(self, **kargs) -> dict:
                """ 
                Listar CST do COFINS. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cofinscst/
                :retorno:  cofinsCstListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCstCofins',
                    endpoint= 'produtos/cofinscst/',
                    param = kargs
                )
            
    def listar_cst_ipi(self, **kargs) -> dict:
                """ 
                Listar CST do IPI. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/ipicst/
                :retorno:  ipiCstListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCstIpi',
                    endpoint= 'produtos/ipicst/',
                    param = kargs
                )
            
    def listar_enq_ipi(self, **kargs) -> dict:
                """ 
                Listar Enquadramento do IPI. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/ipienq/
                :retorno:  ipiEnqListarResponse
                """
                return self._chamar_api(
                    call= 'ListarEnqIpi',
                    endpoint= 'produtos/ipienq/',
                    param = kargs
                )
            
    def listar_tp_calc(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tpcalc/
                :retorno:  tpCalcListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTpCalc',
                    endpoint= 'produtos/tpcalc/',
                    param = kargs
                )
            
    def listar_c_e_s_t(self, **kargs) -> dict:
                """ 
                Listar CEST. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cest/
                :retorno:  cestListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCEST',
                    endpoint= 'produtos/cest/',
                    param = kargs
                )
            
    def alterar_estoque_minimo(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_local_estoque": 0,
                "id_prod": 16487740,
                "cod_int": "",
                "quan_min": "15"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/ajuste/
                :retorno:  estoque_mov_ajuste_estoque_minimo_resposta
                """
                return self._chamar_api(
                    call= 'AlterarEstoqueMinimo',
                    endpoint= 'estoque/ajuste/',
                    param = kargs
                )
            
    def excluir_ajuste_estoque(self, **kargs) -> dict:
                """ 
                Excluir um Movimento de Ajuste de Estoque 
                :exemplo de uso:
                {
                
                "id_ajuste": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/ajuste/
                :retorno:  estoque_mov_ajuste_cadastro_resposta
                """
                return self._chamar_api(
                    call= 'ExcluirAjusteEstoque',
                    endpoint= 'estoque/ajuste/',
                    param = kargs
                )
            
    def incluir_ajuste_estoque(self, **kargs) -> dict:
                """ 
                Incluir um Ajuste de Estoque 
                :exemplo de uso:
                {
                
                "codigo_local_estoque": 0,
                "id_prod": 16487740,
                "data": "23/01/2024",
                "quan": "15",
                "obs": "Ajuste feito pela ferramenta de Teste de API (27501)",
                "origem": "AJU",
                "tipo": "SLD",
                "motivo": "INV",
                "valor": 10

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/ajuste/
                :retorno:  estoque_mov_ajuste_cadastro_resposta
                """
                return self._chamar_api(
                    call= 'IncluirAjusteEstoque',
                    endpoint= 'estoque/ajuste/',
                    param = kargs
                )
            
    def listar_ajuste_estoque(self, **kargs) -> dict:
                """ 
                Listar os ajuste de estoque. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 100,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/ajuste/
                :retorno:  estoque_mov_listar_response
                """
                return self._chamar_api(
                    call= 'ListarAjusteEstoque',
                    endpoint= 'estoque/ajuste/',
                    param = kargs
                )
            
    def listar_movimento_estoque(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50,
                "codigo_local_estoque": 0,
                "idProd": 0,
                "dDtInicial": "23/01/2024",
                "dDtFinal": "23/01/2024",
                "lista_local_estoque": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/consulta/
                :retorno:  ListarMovEstoqueResponse
                """
                return self._chamar_api(
                    call= 'ListarMovimentoEstoque',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def listar_pos_estoque(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50,
                "dDataPosicao": "23/01/2024",
                "cExibeTodos": "N",
                "codigo_local_estoque": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/consulta/
                :retorno:  ListarEstPosResponse
                """
                return self._chamar_api(
                    call= 'ListarPosEstoque',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def listar_saldo_pendente(self, **kargs) -> dict:
                """ 
                Lista o saldo pendente de estoque. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50,
                "codigo_local_estoque": 0,
                "id_prod": 0,
                "tipo": "TODOS"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/consulta/
                :retorno:  estoque_listar_pendente_response
                """
                return self._chamar_api(
                    call= 'ListarSaldoPendente',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def movimento_estoque(self, **kargs) -> dict:
                """ 
                Consulta do Movimento de Estoque 
                :exemplo de uso:
                {
                
                "codigo_local_estoque": 0,
                "id_prod": 0,
                "cod_int": "",
                "dataInicial": "23/01/2024",
                "dataFinal": "23/01/2024"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/consulta/
                :retorno:  estoqueMovimentoResponse
                """
                return self._chamar_api(
                    call= 'MovimentoEstoque',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def posicao_estoque(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_local_estoque": 0,
                "id_prod": 0,
                "cod_int": "",
                "data": "23/01/2024"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/consulta/
                :retorno:  estoque_mov_consulta_cadastro_resposta
                """
                return self._chamar_api(
                    call= 'PosicaoEstoque',
                    endpoint= 'estoque/consulta/',
                    param = kargs
                )
            
    def consultar_previsao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodProd": 1

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/movestoque/
                :retorno:  epPrevisaoResponse
                """
                return self._chamar_api(
                    call= 'ConsultarPrevisao',
                    endpoint= 'estoque/movestoque/',
                    param = kargs
                )
            
    def alterar_local_estoque(self, **kargs) -> dict:
                """ 
                Alterar local de Estoque 
                :exemplo de uso:
                {
                
                "codigo": "L0",
                "descricao": "descri\u00e7\u00e3o de teste",
                "tipo": "1",
                "dispOrdemProducao": "N",
                "codigo_cliente": 0,
                "dispConsumoOP": "N",
                "dispRemessa": "N",
                "dispVenda": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/local/
                :retorno:  alterarLocalResponse
                """
                return self._chamar_api(
                    call= 'AlterarLocalEstoque',
                    endpoint= 'estoque/local/',
                    param = kargs
                )
            
    def incluir_local_estoque(self, **kargs) -> dict:
                """ 
                Adiciona um local de estoque 
                :exemplo de uso:
                {
                
                "codigo": "L0",
                "descricao": "descri\u00e7\u00e3o de teste",
                "tipo": "1",
                "dispOrdemProducao": "N",
                "dispConsumoOP": "N",
                "dispRemessa": "N",
                "dispVenda": "N",
                "consiSugeCompra": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/local/
                :retorno:  incluirLocalResponse
                """
                return self._chamar_api(
                    call= 'IncluirLocalEstoque',
                    endpoint= 'estoque/local/',
                    param = kargs
                )
            
    def listar_locais_estoque(self, **kargs) -> dict:
                """ 
                Lista os Locais de Estoque encontrados. 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/local/
                :retorno:  locaisListarResponse
                """
                return self._chamar_api(
                    call= 'ListarLocaisEstoque',
                    endpoint= 'estoque/local/',
                    param = kargs
                )
            
    def obter_estoque_produto(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cEAN": "",
                "nIdProduto": 0,
                "cCodigo": "",
                "xCodigo": "",
                "dDia": "23/01/2024"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/estoque/resumo/
                :retorno:  ObterEstoqueProdResponse
                """
                return self._chamar_api(
                    call= 'ObterEstoqueProduto',
                    endpoint= 'estoque/resumo/',
                    param = kargs
                )
            
    def adicionar_pedido(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_pedido_integracao": "123456",
                "codigo_cliente": 45621546,
                "codigo_cenario_impostos": 65468465,
                "itens": [
                                
                                                "codigo_produto": 0,
                                                "quantidade": 1,
                                                "valor_unitario": 1,
                                                "cfop": "",
                                                "codigo_cenario_impostos_item": 0
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovenda/
                :retorno:  AdicionarPedidoResponse
                """
                return self._chamar_api(
                    call= 'AdicionarPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def alterar_item_pedido(self, **kargs) -> dict:
                """ 
                Altera um item no pedido de venda. 
                :exemplo de uso:
                {
                
                "codigo_pedido": 0,
                "codigo_item_integracao": "",
                "codigo_item": 0,
                "codigo_produto": 0,
                "quantidade": 1,
                "valor_unitario": 1

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovenda/
                :retorno:  alterarItemPedidoResponse
                """
                return self._chamar_api(
                    call= 'AlterarItemPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def excluir_item_pedido(self, **kargs) -> dict:
                """ 
                Exclui um item no pedido de venda. 
                :exemplo de uso:
                {
                
                "codigo_pedido": 0,
                "codigo_item_integracao": "",
                "codigo_item": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovenda/
                :retorno:  excluirItemPedidoResponse
                """
                return self._chamar_api(
                    call= 'ExcluirItemPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def excluir_itens_pedido(self, **kargs) -> dict:
                """ 
                Exclui todos os itens do pedido de venda. 
                :exemplo de uso:
                {
                
                "codigo_pedido": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovenda/
                :retorno:  excluirItensPedidoResponse
                """
                return self._chamar_api(
                    call= 'ExcluirItensPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def incluir_item_pedido(self, **kargs) -> dict:
                """ 
                Inclui um item no pedido de venda. 
                :exemplo de uso:
                {
                
                "codigo_pedido": 0,
                "codigo_item_integracao": "",
                "codigo_produto": 0,
                "quantidade": 1,
                "valor_unitario": 1,
                "cfop": "",
                "codigo_cenario_impostos_item": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovenda/
                :retorno:  incluirItemPedidoResponse
                """
                return self._chamar_api(
                    call= 'IncluirItemPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def totalizar_pedido(self, **kargs) -> dict:
                """ 
                Recalcula os totais do pedido de venda. 
                :exemplo de uso:
                {
                
                "codigo_pedido": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovenda/
                :retorno:  totalizarPedidoResponse
                """
                return self._chamar_api(
                    call= 'TotalizarPedido',
                    endpoint= 'produtos/pedidovenda/',
                    param = kargs
                )
            
    def alterar_ped_faturado(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "codigo_pedido": 0,
                "codigo_pedido_integracao": "",
                "codigo_rastreio": "",
                "previsao_entrega": "",
                "obs_venda": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedido/
                :retorno:  pvpAlterarPedFatResponse
                """
                return self._chamar_api(
                    call= 'AlterarPedFaturado',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def alterar_pedido_venda(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cabecalho": 
                                "bloqueado": "N",
                                "codigo_cliente": 3792227,
                                "codigo_pedido_integracao": "1706040938",
                                "data_previsao": "23/01/2024",
                                "etapa": "50",
                                "quantidade_itens": 1
                ,
                "det": [
                                
                                                "ide": 
                                                                "codigo_item_integracao": "4422421",
                                                                "simples_nacional": "S"
                                                ,
                                                "imposto": 
                                                                "cofins_padrao": 
                                                                                "aliq_cofins": 3,
                                                                                "base_cofins": 400,
                                                                                "cod_sit_trib_cofins": "01",
                                                                                "tipo_calculo_cofins": "B",
                                                                                "valor_cofins": 12
                                                                ,
                                                                "icms_sn": 
                                                                                "aliq_icms_sn": 1.25,
                                                                                "cod_sit_trib_icms_sn": 101,
                                                                                "origem_icms_sn": 0,
                                                                                "valor_credito_icms_sn": 5
                                                                ,
                                                                "ipi": 
                                                                                "cod_sit_trib_ipi": 51
                                                                ,
                                                                "pis_padrao": 
                                                                                "aliq_pis": 0.65,
                                                                                "base_pis": 400,
                                                                                "cod_sit_trib_pis": "01",
                                                                                "tipo_calculo_pis": "B",
                                                                                "valor_pis": 2.6
                                                                
                                                ,
                                                "inf_adic": 
                                                                "peso_bruto": 150,
                                                                "peso_liquido": 150
                                                ,
                                                "produto": 
                                                                "cfop": "5.102",
                                                                "codigo_produto": "4422421",
                                                                "descricao": "Telefone Celular X",
                                                                "ncm": "9403.30.00",
                                                                "quantidade": 1,
                                                                "tipo_desconto": "V",
                                                                "unidade": "UN",
                                                                "valor_desconto": 0,
                                                                "valor_mercadoria": 200,
                                                                "valor_total": 200,
                                                                "valor_unitario": 200
                                                
                                
                ],
                "informacoes_adicionais": 
                                "codigo_categoria": "1.01.03",
                                "codigo_conta_corrente": 11850365,
                                "consumidor_final": "S",
                                "enviar_email": "N"
                ,
                "lista_parcelas": 
                                "parcela": [
                                                
                                                                "data_vencimento": "24/01/2024",
                                                                "numero_parcela": 1,
                                                                "percentual": 50,
                                                                "valor": 100
                                                ,
                                                
                                                                "data_vencimento": "14/07/2024",
                                                                "numero_parcela": 2,
                                                                "percentual": 50,
                                                                "valor": 100
                                                
                                ]
                ,
                "total_pedido": 
                                "base_calculo_icms": 200,
                                "valor_mercadorias": 200,
                                "valor_total_pedido": 200
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedido/
                :retorno:  pedido_venda_produto_response
                """
                return self._chamar_api(
                    call= 'AlterarPedidoVenda',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def consultar_pedido(self, **kargs) -> dict:
                """ 
                Consulta de Pedido de Venda de Produto 
                :exemplo de uso:
                {
                
                "codigo_pedido": 25953530

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedido/
                :retorno:  pvpConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def excluir_pedido(self, **kargs) -> dict:
                """ 
                Excluir pedido de venda de produto 
                :exemplo de uso:
                {
                
                "codigo_pedido": 0,
                "codigo_pedido_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedido/
                :retorno:  pvpExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def incluir_pedido(self, **kargs) -> dict:
                """ 
                Inclui um pedido de venda de produto 
                :exemplo de uso:
                {
                
                "cabecalho": 
                                "codigo_cliente": 3792227,
                                "codigo_pedido_integracao": "1706040938",
                                "data_previsao": "23/01/2024",
                                "etapa": "10",
                                "numero_pedido": "51732",
                                "codigo_parcela": "999",
                                "quantidade_itens": 2
                ,
                "det": [
                                
                                                "ide": 
                                                                "codigo_item_integracao": "4422421"
                                                ,
                                                "inf_adic": 
                                                                "peso_bruto": 150,
                                                                "peso_liquido": 150
                                                ,
                                                "produto": 
                                                                "cfop": "5.102",
                                                                "codigo_produto": "4422421",
                                                                "descricao": "Telefone Celular X",
                                                                "ncm": "9403.30.00",
                                                                "quantidade": 1,
                                                                "tipo_desconto": "V",
                                                                "unidade": "UN",
                                                                "valor_desconto": 0,
                                                                "valor_unitario": 200
                                                
                                
                ],
                "frete": 
                                "modalidade": "9"
                ,
                "informacoes_adicionais": 
                                "codigo_categoria": "1.01.03",
                                "codigo_conta_corrente": 11850365,
                                "consumidor_final": "S",
                                "enviar_email": "N"
                ,
                "lista_parcelas": 
                                "parcela": [
                                                
                                                                "data_vencimento": "24/01/2024",
                                                                "numero_parcela": 1,
                                                                "percentual": 50,
                                                                "valor": 100
                                                ,
                                                
                                                                "data_vencimento": "05/03/2024",
                                                                "numero_parcela": 2,
                                                                "percentual": 50,
                                                                "valor": 100
                                                
                                ]
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedido/
                :retorno:  pedido_venda_produto_response
                """
                return self._chamar_api(
                    call= 'IncluirPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def listar_pedidos(self, **kargs) -> dict:
                """ 
                Listar os pedidos de venda de produto 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 100,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedido/
                :retorno:  pvpListarResponse
                """
                return self._chamar_api(
                    call= 'ListarPedidos',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def simular_impostos(self, **kargs) -> dict:
                """ 
                Simula os impostos de um pedido de venda. 
                :exemplo de uso:
                {
                
                "codigo_cliente": 0,
                "consumidor_final": "",
                "frete_simul": 
                                "valor_frete": 0,
                                "valor_seguro": 0,
                                "outras_despesas": 0
                ,
                "det_simul": [
                                
                                                "codigo_cenario_impostos_item": 0,
                                                "produto_simul": 
                                                                "codigo_produto": 0,
                                                                "quantidade": 0,
                                                                "valor_unitario": 0,
                                                                "valor_desconto": 0
                                                
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedido/
                :retorno:  pvpSimularImpResponse
                """
                return self._chamar_api(
                    call= 'SimularImpostos',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def status_pedido(self, **kargs) -> dict:
                """ 
                Consulta do Status do Pedido 
                :exemplo de uso:
                {
                
                "codigo_pedido": 0,
                "codigo_pedido_integracao": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedido/
                :retorno:  pvpStatusResponse
                """
                return self._chamar_api(
                    call= 'StatusPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def trocar_etapa_pedido(self, **kargs) -> dict:
                """ 
                Troca etapa do pedido. 
                :exemplo de uso:
                {
                
                "codigo_pedido": 0,
                "codigo_pedido_integracao": "",
                "etapa": "20"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedido/
                :retorno:  pvpTrocarEtapaResponse
                """
                return self._chamar_api(
                    call= 'TrocarEtapaPedido',
                    endpoint= 'produtos/pedido/',
                    param = kargs
                )
            
    def associar_cod_int_pedido_venda(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntPed": "",
                "nCodPed": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovendafat/
                :retorno:  pvpAssociarCodIntResponse
                """
                return self._chamar_api(
                    call= 'AssociarCodIntPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def cancelar_pedido_venda(self, **kargs) -> dict:
                """ 
                Cancela um pedido de venda de produto. 
                :exemplo de uso:
                {
                
                "cCodIntPed": "",
                "nCodPed": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovendafat/
                :retorno:  pvpCancelarResponse
                """
                return self._chamar_api(
                    call= 'CancelarPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def duplicar_pedido_venda(self, **kargs) -> dict:
                """ 
                Duplica um pedido de venda de produto. 
                :exemplo de uso:
                {
                
                "cCodIntPed": "",
                "nCodPed": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovendafat/
                :retorno:  pvpDuplicarResponse
                """
                return self._chamar_api(
                    call= 'DuplicarPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def faturar_pedido_venda(self, **kargs) -> dict:
                """ 
                Fatura um pedido de venda de produto. 
                :exemplo de uso:
                {
                
                "cCodIntPed": "",
                "nCodPed": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovendafat/
                :retorno:  pvpFaturarResponse
                """
                return self._chamar_api(
                    call= 'FaturarPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def obter_pedidos_venda(self, **kargs) -> dict:
                """ 
                Retorna a lista de pedidos de venda a serem faturados. 
                :exemplo de uso:
                {
                
                "cEtapa": "50"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovendafat/
                :retorno:  pvpObterResponse
                """
                return self._chamar_api(
                    call= 'ObterPedidosVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def validar_pedido_venda(self, **kargs) -> dict:
                """ 
                Valida um pedido de venda de produto para faturamento. 
                :exemplo de uso:
                {
                
                "cCodIntPed": "",
                "nCodPed": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidovendafat/
                :retorno:  pvpValidarResponse
                """
                return self._chamar_api(
                    call= 'ValidarPedidoVenda',
                    endpoint= 'produtos/pedidovendafat/',
                    param = kargs
                )
            
    def listar_etapas_pedido(self, **kargs) -> dict:
                """ 
                Lista as etapas do Pedido de Venda de Produtos. 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/pedidoetapas/
                :retorno:  pEtapaListarResponse
                """
                return self._chamar_api(
                    call= 'ListarEtapasPedido',
                    endpoint= 'produtos/pedidoetapas/',
                    param = kargs
                )
            
    def averbacao_c_te(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorCTe",
                "cAppVersao": "1.01.02",
                "cAppId": "Cte01",
                "cChaveCte": "",
                "cXmlCteAverb": "",
                "cMd5CteAverb": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteAverbacaoResponse
                """
                return self._chamar_api(
                    call= 'AverbacaoCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def cancelar_c_te(self, **kargs) -> dict:
                """ 
                Cancela um CT-e. 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorCTe",
                "cAppVersao": "1.01.02",
                "cAppId": "Cte01",
                "cChaveCte": "",
                "cXmlCteCanc": "",
                "cMd5CteCanc": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteCancelarResponse
                """
                return self._chamar_api(
                    call= 'CancelarCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def carta_correcao_c_te(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorCTe",
                "cAppVersao": "1.01.02",
                "cAppId": "Cte01",
                "cChaveCte": "",
                "cXmlCteCC": "",
                "cMd5CteCC": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteCCResponse
                """
                return self._chamar_api(
                    call= 'CartaCorrecaoCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def excluir_c_te(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cChaveCte": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def excluir_fatura_c_te(self, **kargs) -> dict:
                """ 
                Exclui uma fatura de um grupo de CT-es. 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorCTe",
                "cAppVersao": "1.01.02",
                "cAppId": "Cte01",
                "nIdFaturamento": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteExcluirFatResponse
                """
                return self._chamar_api(
                    call= 'ExcluirFaturaCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def faturar_c_te(self, **kargs) -> dict:
                """ 
                Gera uma fatura para um grupo de CT-es. 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorCTe",
                "cAppVersao": "1.01.02",
                "cAppId": "Cte01",
                "CNPJCliente": "",
                "cCategoria": "1.01.02",
                "nContaCorrente": 0,
                "dVencimento": "",
                "nValorFatura": 100,
                "itensFatura": [
                                
                                                "nSeq": 1,
                                                "cChaveCte": "",
                                                "nValorCte": 30
                                ,
                                
                                                "nSeq": 2,
                                                "cChaveCte": "",
                                                "nValorCte": 70
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteFaturarResponse
                """
                return self._chamar_api(
                    call= 'FaturarCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def faturar_lote_c_te(self, **kargs) -> dict:
                """ 
                Gera uma fatura por lote para um grupo de CT-es. 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorCTe",
                "cAppVersao": "1.01.02",
                "cAppId": "Cte01",
                "nIdFaturamento": 0,
                "CNPJCliente": "",
                "cConcluirFatura": "N",
                "itensFatura": [
                                
                                                "nSeq": 1,
                                                "cChaveCte": "",
                                                "nValorCte": 30
                                ,
                                
                                                "nSeq": 2,
                                                "cChaveCte": "",
                                                "nValorCte": 70
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteFaturarLoteResponse
                """
                return self._chamar_api(
                    call= 'FaturarLoteCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def importar_c_te(self, **kargs) -> dict:
                """ 
                Importar o XML de um CT-e. 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorCTe",
                "cAppVersao": "1.01.02",
                "cAppId": "Cte01",
                "cChaveCte": "",
                "cXmlCte": "",
                "cMd5Cte": "",
                "cCategoria": "1.01.02",
                "nContaCorrente": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteImportarResponse
                """
                return self._chamar_api(
                    call= 'ImportarCTe',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def listar_n_fe_transp(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteListarNFeResponse
                """
                return self._chamar_api(
                    call= 'ListarNFeTransp',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def status_fatura(self, **kargs) -> dict:
                """ 
                Retorna o Status da Fatura inclusa. 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorCTe",
                "cAppVersao": "1.01.02",
                "cAppId": "Cte01",
                "nIdFaturamento": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cte/
                :retorno:  cteStatusFaturaResponse
                """
                return self._chamar_api(
                    call= 'StatusFatura',
                    endpoint= 'produtos/cte/',
                    param = kargs
                )
            
    def alterar_remessa(self, **kargs) -> dict:
                """ 
                Altera uma remessa 
                :exemplo de uso:
                {
                
                "cabec": 
                                "cCodIntRem": "",
                                "dPrevisao": "",
                                "nCodCli": 0,
                                "nCodRem": 0,
                                "nCodVend": ""
                ,
                "email": 
                                "cEmail": ""
                ,
                "frete": 
                                "cEspVol": "",
                                "cMarVol": "",
                                "cNumVol": "",
                                "cPlaca": "",
                                "cTpFrete": "",
                                "cUF": "",
                                "nCodTransp": 0,
                                "nPesoBruto": 0,
                                "nPesoLiq": 0,
                                "nQtdVol": 0,
                                "nValFrete": 0,
                                "nValOutras": 0,
                                "nValSeguro": 0
                ,
                "infAdic": 
                                "cCodCateg": "",
                                "cConsFinal": "",
                                "cContato": "",
                                "cDadosAdic": "",
                                "cNumCtr": "",
                                "cPedido": "",
                                "nCodProj": 0
                ,
                "obs": 
                                "cObs": ""
                ,
                "produtos": [
                                
                                                "cCodItInt": "",
                                                "nCodIt": 0,
                                                "nCodProd": 0,
                                                "nQtde": 0,
                                                "nValUnit": 0
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/remessa/
                :retorno:  remessaStatus
                """
                return self._chamar_api(
                    call= 'AlterarRemessa',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def consultar_remessa(self, **kargs) -> dict:
                """ 
                Consulta uma remessa. 
                :exemplo de uso:
                {
                
                "nCodRem": 0,
                "cCodIntRem": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/remessa/
                :retorno:  remessas
                """
                return self._chamar_api(
                    call= 'ConsultarRemessa',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def incluir_remessa(self, **kargs) -> dict:
                """ 
                Inclui uma nova remessa 
                :exemplo de uso:
                {
                
                "cabec": 
                                "cCodIntRem": "",
                                "dPrevisao": "",
                                "nCodCli": 0,
                                "nCodRem": 0,
                                "nCodVend": ""
                ,
                "email": 
                                "cEmail": ""
                ,
                "frete": 
                                "cEspVol": "",
                                "cMarVol": "",
                                "cNumVol": "",
                                "cPlaca": "",
                                "cTpFrete": "",
                                "cUF": "",
                                "nCodTransp": 0,
                                "nPesoBruto": 0,
                                "nPesoLiq": 0,
                                "nQtdVol": 0,
                                "nValFrete": 0,
                                "nValOutras": 0,
                                "nValSeguro": 0
                ,
                "infAdic": 
                                "cCodCateg": "",
                                "cConsFinal": "",
                                "cContato": "",
                                "cDadosAdic": "",
                                "cNumCtr": "",
                                "cPedido": "",
                                "nCodProj": 0
                ,
                "obs": 
                                "cObs": ""
                ,
                "produtos": [
                                
                                                "cCodItInt": "",
                                                "nCodIt": 0,
                                                "nCodProd": 0,
                                                "nQtde": 0,
                                                "nValUnit": 0
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/remessa/
                :retorno:  remessaStatus
                """
                return self._chamar_api(
                    call= 'IncluirRemessa',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def listar_remessas(self, **kargs) -> dict:
                """ 
                Lista as remessas cadastradas. 
                :exemplo de uso:
                {
                
                "nPagina": 1

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/remessa/
                :retorno:  remessaListarResponse
                """
                return self._chamar_api(
                    call= 'ListarRemessas',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def status_remessa(self, **kargs) -> dict:
                """ 
                Retorna o status da remessa 
                :exemplo de uso:
                {
                
                "nCodRem": 0,
                "cCodIntRem": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/remessa/
                :retorno:  remessaStatusResponse
                """
                return self._chamar_api(
                    call= 'StatusRemessa',
                    endpoint= 'produtos/remessa/',
                    param = kargs
                )
            
    def cancelar_remessa(self, **kargs) -> dict:
                """ 
                Cancelar remessa de produto 
                :exemplo de uso:
                {
                
                "nCodRem": 0,
                "cCodIntRem": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/remessafat/
                :retorno:  remessaFatCancelarResponse
                """
                return self._chamar_api(
                    call= 'CancelarRemessa',
                    endpoint= 'produtos/remessafat/',
                    param = kargs
                )
            
    def concluir_remessa(self, **kargs) -> dict:
                """ 
                Concluir remessa de produto 
                :exemplo de uso:
                {
                
                "nCodRem": 0,
                "cCodIntRem": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/remessafat/
                :retorno:  remessaFatConcluirResponse
                """
                return self._chamar_api(
                    call= 'ConcluirRemessa',
                    endpoint= 'produtos/remessafat/',
                    param = kargs
                )
            
    def conferir_remessa(self, **kargs) -> dict:
                """ 
                Conferir remessa de produto 
                :exemplo de uso:
                {
                
                "nCodRem": 0,
                "cCodIntRem": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/remessafat/
                :retorno:  remessaFatConferirResponse
                """
                return self._chamar_api(
                    call= 'ConferirRemessa',
                    endpoint= 'produtos/remessafat/',
                    param = kargs
                )
            
    def duplicar_remessa(self, **kargs) -> dict:
                """ 
                Duplicar remessa de produto 
                :exemplo de uso:
                {
                
                "nCodRem": 0,
                "cCodIntRem": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/remessafat/
                :retorno:  remessaFatDuplicarResponse
                """
                return self._chamar_api(
                    call= 'DuplicarRemessa',
                    endpoint= 'produtos/remessafat/',
                    param = kargs
                )
            
    def obter_demonst(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nIdNf": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osdocs/
                :retorno:  ObterDemonstResponse
                """
                return self._chamar_api(
                    call= 'ObterDemonst',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def obter_n_f_se(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nIdNf": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osdocs/
                :retorno:  ObterNFSeResponse
                """
                return self._chamar_api(
                    call= 'ObterNFSe',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def obter_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cEtapa": "50"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osp/
                :retorno:  osObterResponse
                """
                return self._chamar_api(
                    call= 'ObterOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def obter_r_p_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nIdNf": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osdocs/
                :retorno:  ObterRPSResponse
                """
                return self._chamar_api(
                    call= 'ObterRPS',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def obter_recibo(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nIdRec": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osdocs/
                :retorno:  ObterReciboResponse
                """
                return self._chamar_api(
                    call= 'ObterRecibo',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def obter_via_unica(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nIdNf": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osdocs/
                :retorno:  ObterViaUnicaResponse
                """
                return self._chamar_api(
                    call= 'ObterViaUnica',
                    endpoint= 'servicos/osdocs/',
                    param = kargs
                )
            
    def fechar_caixa(self, **kargs) -> dict:
                """ 
                Efetua o fechamento de um determinado caixa. 
                :exemplo de uso:
                {
                
                "emissor": 
                                "emiNome": "OmiePDV",
                                "emiVersao": "1.0",
                                "emiSerial": "ASDadsADSasdADS",
                                "emiId": "01"
                ,
                "seqCaixa": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscalincluir/
                :retorno:  cfFecharCaixaResponse
                """
                return self._chamar_api(
                    call= 'FecharCaixa',
                    endpoint= 'produtos/cupomfiscalincluir/',
                    param = kargs
                )
            
    def incluir_cfe_sat(self, **kargs) -> dict:
                """ 
                Incluir Cupom Fiscal para SAT. 
                :exemplo de uso:
                {
                
                "caixa": 
                                "lCxAberto": true,
                                "seqCaixa": 3428,
                                "seqCupom": 384559
                ,
                "cfeSat": 
                                "chCFe": "99999999999999999999999999999999999999999999",
                                "dEmi": "07/02/2022",
                                "det": [
                                                
                                                                "imposto": 
                                                                                "ICMS": 
                                                                                                "CST": "60"
                                                                                ,
                                                                                "vTotTrib": 5.98
                                                                ,
                                                                "lCanc": false,
                                                                "prod": 
                                                                                "cUn": "UN",
                                                                                "vAcresc": 0,
                                                                                "vDesc": 0,
                                                                                "vItem": 21.47,
                                                                                "vProd": 19.0,
                                                                                "vUnit": 19.0
                                                                ,
                                                                "prodIdent": 
                                                                                "emiProduto": "30218001",
                                                                                "idLocalEstoque": 393938380,
                                                                                "idProduto": 453975843
                                                                ,
                                                                "seqItem": 1
                                                
                                ],
                                "hEmi": "16:53:23",
                                "lCanc": false,
                                "nCFe": "034799",
                                "total": 
                                                "vAcresc": 0,
                                                "vCF": 28.82,
                                                "vDesc": 0,
                                                "vItem": 25.5,
                                                "vTotTrib": 8.33
                                ,
                                "tpAmb": "P"
                ,
                "cupomIdent": 
                                "idCliente": 423856753
                ,
                "emissor": 
                                "emiId": "001",
                                "emiNome": "SeuPDV",
                                "emiSerial": "X128992",
                                "emiVersao": "04.08"
                ,
                "formasPag": [
                                
                                                "lCanc": false,
                                                "pag": 
                                                                "pTaxa": 2.65,
                                                                "vLiq": 28.82,
                                                                "vPag": 28.82,
                                                                "vTaxa": 0.76,
                                                                "vTroco": 0
                                                ,
                                                "pagIdent": 
                                                                "cCategoria": "1.01.95",
                                                                "cTipoPag": "CRC",
                                                                "idConta": 372946272
                                                ,
                                                "parcelas": [
                                                                
                                                                                "dVenc": "10/02/2022",
                                                                                "nParc": 1,
                                                                                "vParc": 28.82
                                                                
                                                ],
                                                "seqPag": 1
                                
                ],
                "sat": 
                                "satMd5": "f13df5c85a499d7cekei3f7dacd31c6b5",
                                "satModelo": "DIMEP",
                                "satProt": "12345678",
                                "satSerie": "000756735",
                                "satSessao": "68670",
                                "satXml": "SEU_XML"
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscalincluir/
                :retorno:  cfIncluirSatResponse
                """
                return self._chamar_api(
                    call= 'IncluirCfeSat',
                    endpoint= 'produtos/cupomfiscalincluir/',
                    param = kargs
                )
            
    def incluir_cupom(self, **kargs) -> dict:
                """ 
                Incluir Cupom Fiscal (ECF). 
                :exemplo de uso:
                {
                
                "emissor": 
                                "emiNome": "EmissorPDV",
                                "emiVersao": "1.0",
                                "emiSerial": "781818814968638",
                                "emiId": "001"
                ,
                "ecf": 
                                "ecfSerie": "BE051475610000201537",
                                "ecfModelo": "MP-2100 TH FI"
                ,
                "caixa": 
                                "seqCaixa": "47419",
                                "seqCupom": "1706041149"
                ,
                "cupom": 
                                "nCOO": "1706041149",
                                "nCCF": "1706041149",
                                "dEmi": "23/01/2024",
                                "hEmi": "13:14:30",
                                "lCanc": false,
                                "det": [
                                                
                                                                "seqItem": 1,
                                                                "lCanc": false,
                                                                "prod": 
                                                                                "cProd": "700309",
                                                                                "xProd": "Misiones de Rengo Carmenere 2016",
                                                                                "CFOP": "5.101",
                                                                                "NCM": "2204.21.00",
                                                                                "cEAN": "",
                                                                                "cUn": "GF",
                                                                                "nQuant": 10,
                                                                                "vUnit": 5.5,
                                                                                "vProd": 55,
                                                                                "vDesc": 0,
                                                                                "vAcresc": 0,
                                                                                "vItem": 55
                                                                ,
                                                                "prodIdent": 
                                                                                "idProduto": 369356862,
                                                                                "emiProduto": "3229"
                                                                ,
                                                                "imposto": 
                                                                                "vTotTrib": 5,
                                                                                "ICMS": 
                                                                                                "CST": "00",
                                                                                                "vBC": 55,
                                                                                                "pICMS": 18,
                                                                                                "vICMS": 9.9
                                                                                
                                                                
                                                ,
                                                
                                                                "seqItem": 2,
                                                                "lCanc": false,
                                                                "prod": 
                                                                                "cProd": "700307",
                                                                                "xProd": "Periquita Reserva 2014",
                                                                                "CFOP": "5.101",
                                                                                "NCM": "2204.21.00",
                                                                                "cEAN": "",
                                                                                "cUn": "GF",
                                                                                "nQuant": 10,
                                                                                "vUnit": 4,
                                                                                "vProd": 40,
                                                                                "vDesc": 0,
                                                                                "vAcresc": 0,
                                                                                "vItem": 40
                                                                ,
                                                                "prodIdent": 
                                                                                "idProduto": 369356851,
                                                                                "emiProduto": "3224"
                                                                ,
                                                                "imposto": 
                                                                                "vTotTrib": 5,
                                                                                "ICMS": 
                                                                                                "CST": "00",
                                                                                                "vBC": 40,
                                                                                                "pICMS": 18,
                                                                                                "vICMS": 7.2
                                                                                
                                                                
                                                
                                ],
                                "outrasInf": 
                                                "nMesa": 0,
                                                "nPessoas": 0
                                ,
                                "total": 
                                                "vItem": 95,
                                                "vICMS": 17.1,
                                                "vDesc": 0,
                                                "vAcresc": 0,
                                                "vTaxa": 3,
                                                "vCF": 95,
                                                "vTotTrib": 10
                                
                ,
                "cupomIdent": 
                                "idCliente": 0,
                                "idVendedor": 0,
                                "idProjeto": 0,
                                "cUsuario": ""
                ,
                "formasPag": [
                                
                                                "seqPag": 1,
                                                "lCanc": false,
                                                "pag": 
                                                                "vPag": 40,
                                                                "vTroco": 0,
                                                                "vTaxa": 0,
                                                                "pTaxa": 0,
                                                                "vLiq": 40
                                                ,
                                                "pagIdent": 
                                                                "cCategoria": "1.01.03",
                                                                "cTipoPag": "CRT",
                                                                "idConta": 1610386
                                                ,
                                                "TEF": 
                                                                "NSU": "1029333",
                                                                "nNumeroAut": "2222",
                                                                "nValorAut": 100,
                                                                "cTipoCartao": "D",
                                                                "cRedeTef": "VISANET",
                                                                "cBandeiraTef": "VISA",
                                                                "nParcTef": 2
                                                ,
                                                "parcelas": [
                                                                
                                                                                "nParc": 1,
                                                                                "dVenc": "24/01/2024",
                                                                                "vParc": 25
                                                                ,
                                                                
                                                                                "nParc": 2,
                                                                                "dVenc": "03/04/2024",
                                                                                "vParc": 15
                                                                
                                                ]
                                ,
                                
                                                "seqPag": 2,
                                                "lCanc": false,
                                                "pag": 
                                                                "vPag": 55,
                                                                "vTroco": 0,
                                                                "vTaxa": 0,
                                                                "pTaxa": 0,
                                                                "vLiq": 55
                                                ,
                                                "pagIdent": 
                                                                "cCategoria": "1.01.03",
                                                                "cTipoPag": "CHQ",
                                                                "idConta": 1208238
                                                ,
                                                "Cheque": 
                                                                "chBanco": "001",
                                                                "chAgencia": "4321",
                                                                "chConta": "003004",
                                                                "chSerie": "01",
                                                                "chNumero": "01234"
                                                
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscalincluir/
                :retorno:  cfIncluirEcfResponse
                """
                return self._chamar_api(
                    call= 'IncluirCupom',
                    endpoint= 'produtos/cupomfiscalincluir/',
                    param = kargs
                )
            
    def incluir_nfce(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "NFe": 
                                "chNFe": "99999999999999999999999999999999999999999999",
                                "dEmi": "dd/mm/aaaa",
                                "det": [
                                                
                                                                "lCanc": false,
                                                                "lNaoMovEstoque": false,
                                                                "prod": 
                                                                                "CFOP": "5405",
                                                                                "NCM": "04061090",
                                                                                "cEAN": "SEM GTIN",
                                                                                "cProd": "325",
                                                                                "cUn": "UN",
                                                                                "nQuant": 1,
                                                                                "vAcresc": 0,
                                                                                "vDesc": 0,
                                                                                "vItem": 15,
                                                                                "vProd": 15,
                                                                                "vUnit": 15,
                                                                                "xProd": "REQUEIJAO CREMOSO 400GR MINAS MILK"
                                                                ,
                                                                "prodIdent": 
                                                                                "emiProduto": "325",
                                                                                "idLocalEstoque": "1205784081",
                                                                                "idProduto": 1208514897
                                                                ,
                                                                "seqItem": 1
                                                
                                ],
                                "hEmi": "08:24:01",
                                "lCanc": false,
                                "nNF": "000016064",
                                "serie": "002",
                                "total": 
                                                "vAcresc": "0.00",
                                                "vCF": "25.00",
                                                "vDesc": "0.00",
                                                "vICMS": "0.00",
                                                "vItem": "25.00",
                                                "vTaxa": 0,
                                                "vTotTrib": 0
                                ,
                                "tpAmb": "P",
                                "tpEmis": "1"
                ,
                "caixa": 
                                "lCxAberto": false,
                                "seqCaixa": 710,
                                "seqCupom": 1012303
                ,
                "cupomIdent": 
                                "idCliente": 120834285,
                                "idProjeto": 0,
                                "idVendedor": 0
                ,
                "emissor": 
                                "emiId": "0001",
                                "emiNome": "SEU_PDV",
                                "emiSerial": "WD-WXS1A499REDFTB58F00D65",
                                "emiVersao": "1.9.00"
                ,
                "formasPag": [
                                
                                                "Parcelas": [
                                                                
                                                                                "dVenc": "dd/mm/aaaa",
                                                                                "nParc": "001/001",
                                                                                "vParc": 25
                                                                
                                                ],
                                                "TEF": 
                                                                "NSU": "",
                                                                "cBandeiraTef": "",
                                                                "cRedeTef": "Outros",
                                                                "cTipoCartao": "",
                                                                "nNumeroAut": "",
                                                                "nParcTef": 0,
                                                                "nValorAut": 25
                                                ,
                                                "lCanc": false,
                                                "lNaoGerarTitulo": false,
                                                "pag": 
                                                                "pTaxa": 0,
                                                                "vLiq": 25,
                                                                "vPag": 25,
                                                                "vTaxa": 0,
                                                                "vTroco": 0
                                                ,
                                                "pagIdent": 
                                                                "cCategoria": "1.01.03",
                                                                "cTipoPag": "CRT",
                                                                "idConta": 1298842804
                                                ,
                                                "seqPag": 1
                                
                ],
                "nfce": 
                                "nfceMd5": "754d4c0594e4ebcbcf7fdd75547f9d7d",
                                "nfceProt": "999999999999999",
                                "nfceXml": "SEU_XML"
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscalincluir/
                :retorno:  cfIncluirNfceResponse
                """
                return self._chamar_api(
                    call= 'IncluirNfce',
                    endpoint= 'produtos/cupomfiscalincluir/',
                    param = kargs
                )
            
    def inutilizar_nfce(self, **kargs) -> dict:
                """ 
                Inutiliza um lote de NFC-e. 
                :exemplo de uso:
                {
                
                "emissor": 
                                "emiNome": "OmiePDV",
                                "emiVersao": "1.0",
                                "emiSerial": "ASDadsADSasdADS",
                                "emiId": "01"
                ,
                "nfceInut": 
                                "nfceProtInut": 0,
                                "nfceXmlInut": "",
                                "nfceMd5Inut": ""
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscalincluir/
                :retorno:  cfInutilizarNfceResponse
                """
                return self._chamar_api(
                    call= 'InutilizarNfce',
                    endpoint= 'produtos/cupomfiscalincluir/',
                    param = kargs
                )
            
    def cancelar_cupom(self, **kargs) -> dict:
                """ 
                Cancela um cupom Fiscal 
                :exemplo de uso:
                {
                
                "nIdCupom": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscal/
                :retorno:  cfCancelarResponse
                """
                return self._chamar_api(
                    call= 'CancelarCupom',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def cancelar_n_f_c_e(self, **kargs) -> dict:
                """ 
                Cancelar NFC-e. 
                :exemplo de uso:
                {
                
                "nCodigoPDV": 0,
                "nNumeroCaixa": 0,
                "cDataEmissao": "",
                "IdenticacaoNFCE": 
                                "nNumeroNFCE": 0,
                                "nSerieNFCE": 0,
                                "nChaveNFCE": ""
                ,
                "DadosCancNFCE": 
                                "nProtCancNFCE": 0,
                                "nChaveCancNFCE": "",
                                "cXmlCancNFCE": "",
                                "cDataCancelamento": "",
                                "cHoraCancelamento": ""
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscal/
                :retorno:  cfCancelarNfceResponse
                """
                return self._chamar_api(
                    call= 'CancelarNFCE',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def cancelar_s_a_t(self, **kargs) -> dict:
                """ 
                Cancelar CF-e-SAT. 
                :exemplo de uso:
                {
                
                "nCodigoPDV": 0,
                "nNumeroCaixa": 0,
                "cDataEmissao": "",
                "IdenticacaoSAT": 
                                "nNumeroSAT": 0,
                                "nChaveSAT": "",
                                "cNumeroSerieSAT": ""
                ,
                "DadosCancSAT": 
                                "nProtCancSAT": 0,
                                "nChaveCancSAT": "",
                                "cXmlCancSAT": "",
                                "cDataCancelamento": "",
                                "cHoraCancelamento": ""
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscal/
                :retorno:  cfCancelarSatResponse
                """
                return self._chamar_api(
                    call= 'CancelarSAT',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def devolver_cupom(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nIdCupom": 0,
                "nIdMotivDevol": 0,
                "itens": [
                                
                                                "nIdItem": 0,
                                                "nQuant": 0
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscal/
                :retorno:  cfDevolverCupomResponse
                """
                return self._chamar_api(
                    call= 'DevolverCupom',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def excluir_cupom(self, **kargs) -> dict:
                """ 
                Exclui um Cupom Fiscal. 
                :exemplo de uso:
                {
                
                "nIdCupom": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscal/
                :retorno:  cfExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirCupom',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def excluir_cupons_por_numero(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodigoPDV": 0,
                "nNumeroCaixa": 0,
                "cDataEmissao": "",
                "nNumCupom": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscal/
                :retorno:  cfExcluirPorNumResponse
                """
                return self._chamar_api(
                    call= 'ExcluirCuponsPorNumero',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def excluir_lote(self, **kargs) -> dict:
                """ 
                Excluir o lote 
                :exemplo de uso:
                {
                
                "nNumLote": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscal/
                :retorno:  cfExcluirLoteResponse
                """
                return self._chamar_api(
                    call= 'ExcluirLote',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def listar_cupons(self, **kargs) -> dict:
                """ 
                Lista os Cupons Fiscais. 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50,
                "dDtEmisInicial": "",
                "dDtEmisFinal": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscal/
                :retorno:  cfListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCupons',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def obter_proximo_lote(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodigoPDV": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscal/
                :retorno:  cfObterProxLoteResponse
                """
                return self._chamar_api(
                    call= 'ObterProximoLote',
                    endpoint= 'produtos/cupomfiscal/',
                    param = kargs
                )
            
    def cupons_fiscais(self, **kargs) -> dict:
                """ 
                Listagem dos cupons fiscais. 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscalconsultar/
                :retorno:  cfcListarResponse
                """
                return self._chamar_api(
                    call= 'CuponsFiscais',
                    endpoint= 'produtos/cupomfiscalconsultar/',
                    param = kargs
                )
            
    def cupons_itens(self, **kargs) -> dict:
                """ 
                Listagem dos itens dos cupons fiscais 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscalconsultar/
                :retorno:  cfcItensResponse
                """
                return self._chamar_api(
                    call= 'CuponsItens',
                    endpoint= 'produtos/cupomfiscalconsultar/',
                    param = kargs
                )
            
    def cupons_pagamentos(self, **kargs) -> dict:
                """ 
                Listagem dos pagamentos dos cupons fiscais 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/cupomfiscalconsultar/
                :retorno:  cfcPagamentosResponse
                """
                return self._chamar_api(
                    call= 'CuponsPagamentos',
                    endpoint= 'produtos/cupomfiscalconsultar/',
                    param = kargs
                )
            
    def importar_n_f_ce(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "emiNome": "GeradorNFe",
                "emiVersao": "1.01.02",
                "emiId": "PDV01",
                "chNFe": "",
                "nfceXml": "",
                "nfceMd5": "",
                "cAcaoCliente": "INCLUIR",
                "idCliente": 0,
                "idVendedor": 0,
                "idProjeto": 0,
                "idLocalEstoque": 0,
                "cNaoMovEstoque": "N",
                "cNaoGerarTitulo": "N",
                "cIncluirProduto": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/nfce/
                :retorno:  ImportarNfceResponse
                """
                return self._chamar_api(
                    call= 'ImportarNFCe',
                    endpoint= 'produtos/nfce/',
                    param = kargs
                )
            
    def importar_cfe_sat(self, **kargs) -> dict:
                """ 
                Importa o XML de um CF-e SAT. 
                :exemplo de uso:
                {
                
                "emiNome": "GeradorNFe",
                "emiVersao": "1.01.02",
                "emiId": "PDV01",
                "chNFe": "",
                "satXml": "",
                "satMd5": "",
                "cAcaoCliente": "INCLUIR",
                "idCliente": 0,
                "idVendedor": 0,
                "idProjeto": 0,
                "idLocalEstoque": 0,
                "cNaoMovEstoque": "N",
                "cNaoGerarTitulo": "N",
                "cIncluirProduto": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/sat/
                :retorno:  ImportarSatResponse
                """
                return self._chamar_api(
                    call= 'ImportarCfeSat',
                    endpoint= 'produtos/sat/',
                    param = kargs
                )
            
    def alterar_preco_item(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodTabPreco": 0,
                "nCodProd": 0,
                "nValorTabela": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprAltPrecoItemResponse
                """
                return self._chamar_api(
                    call= 'AlterarPrecoItem',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def alterar_tabela_preco(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodTabPreco": 0,
                "cCodIntTabPreco": "TP1706038805",
                "cNome": "",
                "cCodigo": "",
                "cOrigem": "",
                "produtos": 
                                "cTodosProdutos": "S",
                                "nCodFamilia": 0,
                                "cNCM": "",
                                "nCodCaract": 0,
                                "cConteudo": "",
                                "nCodFornec": 0
                ,
                "clientes": 
                                "cTodosClientes": "S",
                                "nCodTag": 0,
                                "cTag": "",
                                "cUF": ""
                ,
                "outrasInfo": 
                                "nCodOrigTab": 0,
                                "nPercAcrescimo": 0,
                                "nPercDesconto": 0
                ,
                "caracteristicas": 
                                "cTemValidade": "S",
                                "dDtInicial": "23/01/2024",
                                "dDtFinal": "23/01/2024",
                                "cTemDesconto": "",
                                "nDescSugerido": 0,
                                "nPercDescMax": 0,
                                "cArredPreco": "N"
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def ativar_tabela_preco(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodTabPreco": 0,
                "cCodIntTabPreco": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprAtivarResponse
                """
                return self._chamar_api(
                    call= 'AtivarTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def atualizar_produtos(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodTabPreco": 0,
                "cCodIntTabPreco": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprAtualizarResponse
                """
                return self._chamar_api(
                    call= 'AtualizarProdutos',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def consultar_tabela_preco(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodTabPreco": 0,
                "cCodIntTabPreco": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def excluir_tabela_preco(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodTabPreco": 0,
                "cCodIntTabPreco": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def incluir_tabela_preco(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntTabPreco": "TP1706038805",
                "cNome": "",
                "cCodigo": "",
                "cOrigem": "",
                "produtos": 
                                "cTodosProdutos": "S",
                                "nCodFamilia": 0,
                                "cNCM": "",
                                "nCodCaract": 0,
                                "cConteudo": "",
                                "nCodFornec": 0
                ,
                "clientes": 
                                "cTodosClientes": "S",
                                "nCodTag": 0,
                                "cTag": "",
                                "cUF": ""
                ,
                "outrasInfo": 
                                "nCodOrigTab": 0,
                                "nPercAcrescimo": 0,
                                "nPercDesconto": 0
                ,
                "caracteristicas": 
                                "cTemValidade": "S",
                                "dDtInicial": "23/01/2024",
                                "dDtFinal": "23/01/2024",
                                "cTemDesconto": "",
                                "nDescSugerido": 0,
                                "nPercDescMax": 0,
                                "cArredPreco": "N"
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def listar_tabela_itens(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20,
                "nCodTabPreco": 0,
                "cCodIntTabPreco": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprItensListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTabelaItens',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def listar_tabelas_preco(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTabelasPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def suspender_tabela_preco(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodTabPreco": 0,
                "cCodIntTabPreco": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/tabelaprecos/
                :retorno:  tprSuspenderResponse
                """
                return self._chamar_api(
                    call= 'SuspenderTabelaPreco',
                    endpoint= 'produtos/tabelaprecos/',
                    param = kargs
                )
            
    def alterar_caracteristica(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodCaract": 0,
                "cCodIntCaract": "",
                "cNomeCaract": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/caracteristicas/
                :retorno:  caractAlterarResponse
                """
                return self._chamar_api(
                    call= 'AlterarCaracteristica',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def consultar_caracteristica(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodCaract": 0,
                "cCodIntCaract": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/caracteristicas/
                :retorno:  caractConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarCaracteristica',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def excluir_caracteristica(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodCaract": 0,
                "cCodIntCaract": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/caracteristicas/
                :retorno:  caractExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirCaracteristica',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def incluir_caracteristica(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntCaract": "CPROD1706041243",
                "cNomeCaract": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/caracteristicas/
                :retorno:  caractIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirCaracteristica',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def listar_caracteristicas(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/caracteristicas/
                :retorno:  caractListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCaracteristicas',
                    endpoint= 'geral/caracteristicas/',
                    param = kargs
                )
            
    def listar_etapas_faturamento(self, **kargs) -> dict:
                """ 
                Lista as etapas do faturamento 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/etapafat/
                :retorno:  etaproListarResponse
                """
                return self._chamar_api(
                    call= 'ListarEtapasFaturamento',
                    endpoint= 'produtos/etapafat/',
                    param = kargs
                )
            
    def listar_meios_pagamento(self, **kargs) -> dict:
                """ 
                Listagem de meios de pagamento 
                :exemplo de uso:
                {
                
                "codigo": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/meiospagamento/
                :retorno:  MeiosPagamentoPesquisarResponse
                """
                return self._chamar_api(
                    call= 'ListarMeiosPagamento',
                    endpoint= 'geral/meiospagamento/',
                    param = kargs
                )
            
    def listar_motivos_devol(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/geral/motivodevolucao/
                :retorno:  ListarMotivoDevolResponse
                """
                return self._chamar_api(
                    call= 'ListarMotivosDevol',
                    endpoint= 'geral/motivodevolucao/',
                    param = kargs
                )
            
    def listar_n_f_s_es(self, **kargs) -> dict:
                """ 
                Lista de NFS-es. 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/nfse/
                :retorno:  nfseListarResponse
                """
                return self._chamar_api(
                    call= 'ListarNFSEs',
                    endpoint= 'servicos/nfse/',
                    param = kargs
                )
            
    def get_url_danfe(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodNF": 0,
                "cCodNFInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notafiscalutil/
                :retorno:  nfUtil_GetUrlDanfe_response
                """
                return self._chamar_api(
                    call= 'GetUrlDanfe',
                    endpoint= 'produtos/notafiscalutil/',
                    param = kargs
                )
            
    def get_url_logo(self, **kargs) -> dict:
                """ 
                Retorna a URL do Logotipo 
                :exemplo de uso:
                {
                
                "nCodEmpr": 0,
                "cCodEmprInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notafiscalutil/
                :retorno:  nfUtil_GetUrlLogo_response
                """
                return self._chamar_api(
                    call= 'GetUrlLogo',
                    endpoint= 'produtos/notafiscalutil/',
                    param = kargs
                )
            
    def get_url_nota_fiscal(self, **kargs) -> dict:
                """ 
                Retorna a URL da Nota Fiscal 
                :exemplo de uso:
                {
                
                "nCodNF": 0,
                "cCodNFInt": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/notafiscalutil/
                :retorno:  nfUtil_GetUrlNF_response
                """
                return self._chamar_api(
                    call= 'GetUrlNotaFiscal',
                    endpoint= 'produtos/notafiscalutil/',
                    param = kargs
                )
            
    def excluir_n_fe(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cChaveNFe": "",
                "nIdImportacao": 0,
                "nIdNFe": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/nfe/
                :retorno:  nfeExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirNFe',
                    endpoint= 'produtos/nfe/',
                    param = kargs
                )
            
    def importar_canc_n_fe(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorNFe",
                "cAppVersao": "1.01.02",
                "cAppId": "NFe01",
                "cChaveNFe": "",
                "cXmlNFeCanc": "",
                "cMd5NFeCanc": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/nfe/
                :retorno:  nfeCancelarResponse
                """
                return self._chamar_api(
                    call= 'ImportarCancNFe',
                    endpoint= 'produtos/nfe/',
                    param = kargs
                )
            
    def importar_n_fe(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cAppNome": "GeradorNFe",
                "cAppVersao": "1.01.02",
                "cAppId": "NFe01",
                "cChaveNFe": "",
                "cXmlNFe": "",
                "cMd5NFe": "",
                "cOperacao": "11",
                "cOrigem": "API",
                "nCliente": 0,
                "cCategoria": "1.01.02",
                "nContaCorrente": 0,
                "codigo_local_estoque": 0,
                "lNaoMovEstoque": true,
                "lNaoGerarTitulo": false,
                "lNaoIncluirCliente": false,
                "lNaoIncluirProduto": true

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/nfe/
                :retorno:  nfeImportarResponse
                """
                return self._chamar_api(
                    call= 'ImportarNFe',
                    endpoint= 'produtos/nfe/',
                    param = kargs
                )
            
    def listar_n_fe(self, **kargs) -> dict:
                """ 
                Lista as NFes importadas. 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 50,
                "dDataEmissaoInicial": "23/01/2024",
                "dDataEmissaoFinal": "23/01/2024"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/produtos/nfe/
                :retorno:  nfeListarResponse
                """
                return self._chamar_api(
                    call= 'ListarNFe',
                    endpoint= 'produtos/nfe/',
                    param = kargs
                )
            
    def alterar_cadastro_servico(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "intEditar": 
                                "cCodIntServ": "",
                                "nCodServ": 0
                ,
                "descricao": 
                                "cDescrCompleta": "descricao"
                ,
                "cabecalho": 
                                "cDescricao": "Descricao",
                                "cCodigo": "",
                                "cIdTrib": "",
                                "cCodServMun": "",
                                "cCodLC116": "",
                                "nIdNBS": "",
                                "nPrecoUnit": 10.99,
                                "cCodCateg": ""
                ,
                "impostos": 
                                "nAliqISS": 0,
                                "cRetISS": "N",
                                "nAliqPIS": 0,
                                "cRetPIS": "N",
                                "nAliqCOFINS": 0,
                                "cRetCOFINS": "N",
                                "nAliqCSLL": 0,
                                "cRetCSLL": "N",
                                "nAliqIR": 0,
                                "cRetIR": "N",
                                "nAliqINSS": 0,
                                "cRetINSS": "N",
                                "nRedBaseINSS": 0,
                                "nRedBaseCOFINS": 0,
                                "nRedBasePIS": 0,
                                "lDeduzISS": false
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/servico/
                :retorno:  srvEditarResponse
                """
                return self._chamar_api(
                    call= 'AlterarCadastroServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def associar_cod_int_servico(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nCodServ": 0,
                "cCodIntServ": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/servico/
                :retorno:  srvAssociarResponse
                """
                return self._chamar_api(
                    call= 'AssociarCodIntServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def consultar_cadastro_servico(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntServ": "",
                "nCodServ": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/servico/
                :retorno:  srvConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarCadastroServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def excluir_cadastro_servico(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntServ": "",
                "nCodServ": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/servico/
                :retorno:  srvExcluirResponse
                """
                return self._chamar_api(
                    call= 'ExcluirCadastroServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def incluir_cadastro_servico(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "intIncluir": 
                                "cCodIntServ": "1234"
                ,
                "descricao": 
                                "cDescrCompleta": "descricao"
                ,
                "cabecalho": 
                                "cDescricao": "Descricao",
                                "cCodigo": "1234",
                                "cIdTrib": "",
                                "cCodServMun": "",
                                "cCodLC116": "",
                                "nIdNBS": "",
                                "nPrecoUnit": 10.99,
                                "cCodCateg": ""
                ,
                "impostos": 
                                "nAliqISS": 0,
                                "cRetISS": "N",
                                "nAliqPIS": 0,
                                "cRetPIS": "N",
                                "nAliqCOFINS": 0,
                                "cRetCOFINS": "N",
                                "nAliqCSLL": 0,
                                "cRetCSLL": "N",
                                "nAliqIR": 0,
                                "cRetIR": "N",
                                "nAliqINSS": 0,
                                "cRetINSS": "N",
                                "nRedBaseINSS": 0,
                                "nRedBaseCOFINS": 0,
                                "nRedBasePIS": 0,
                                "lDeduzISS": false
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/servico/
                :retorno:  srvIncluirResponse
                """
                return self._chamar_api(
                    call= 'IncluirCadastroServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def listar_cadastro_servico(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/servico/
                :retorno:  srvListarResponse
                """
                return self._chamar_api(
                    call= 'ListarCadastroServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def upsert_cadastro_servico(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "intEditar": 
                                "cCodIntServ": "",
                                "nCodServ": 0
                ,
                "descricao": 
                                "cDescrCompleta": "descricao"
                ,
                "cabecalho": 
                                "cDescricao": "Descricao",
                                "cCodigo": "",
                                "cIdTrib": "",
                                "cCodServMun": "",
                                "cCodLC116": "",
                                "nIdNBS": "",
                                "nPrecoUnit": 10.99,
                                "cCodCateg": ""
                ,
                "impostos": 
                                "nAliqISS": 0,
                                "cRetISS": "N",
                                "nAliqPIS": 0,
                                "cRetPIS": "N",
                                "nAliqCOFINS": 0,
                                "cRetCOFINS": "N",
                                "nAliqCSLL": 0,
                                "cRetCSLL": "N",
                                "nAliqIR": 0,
                                "cRetIR": "N",
                                "nAliqINSS": 0,
                                "cRetINSS": "N",
                                "nRedBaseINSS": 0,
                                "nRedBaseCOFINS": 0,
                                "nRedBasePIS": 0,
                                "lDeduzISS": false
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/servico/
                :retorno:  srvUpsertResponse
                """
                return self._chamar_api(
                    call= 'UpsertCadastroServico',
                    endpoint= 'servicos/servico/',
                    param = kargs
                )
            
    def alterar_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "Cabecalho": 
                                "nCodOS": "1706038451",
                                "cCodParc": "999",
                                "cEtapa": "20",
                                "dDtPrevisao": "23/01/2024",
                                "nCodCli": 2485994,
                                "nQtdeParc": 7
                ,
                "Departamentos": [],
                "Email": 
                                "cEnvBoleto": "N",
                                "cEnvLink": "N",
                                "cEnviarPara": "teste@omie.com.br"
                ,
                "InformacoesAdicionais": 
                                "cCidPrestServ": "SAO PAULO (SP)",
                                "cCodCateg": "1.01.02",
                                "cDadosAdicNF": "OS incluida via API de teste 42123",
                                "nCodCC": 11850365
                ,
                "ServicosPrestados": [
                                
                                                "cCodServLC116": "7.07",
                                                "cCodServMun": "01015",
                                                "cDadosAdicItem": "Servi\u00e7os prestados",
                                                "cDescServ": "Servi\u00e7o prestado 001",
                                                "cRetemISS": "N",
                                                "cTribServ": "01",
                                                "impostos": 
                                                                "cRetemIRRF": "S",
                                                                "cRetemPIS": "S",
                                                                "nAliqCOFINS": 0,
                                                                "nAliqCSLL": 0,
                                                                "nAliqIRRF": 15,
                                                                "nAliqISS": 3,
                                                                "nAliqPIS": 4.5
                                                ,
                                                "nQtde": 3,
                                                "nValUnit": 1000
                                ,
                                
                                                "impostos": 
                                                                "cRetemIRRF": "S",
                                                                "cRetemPIS": "S",
                                                                "nAliqIRRF": 15,
                                                                "nAliqISS": 3,
                                                                "nAliqPIS": 4.5
                                                ,
                                                "nCodServico": 2342423,
                                                "nQtde": 12,
                                                "nValUnit": 35
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/os/
                :retorno:  osStatus
                """
                return self._chamar_api(
                    call= 'AlterarOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def consultar_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0,
                "cNumOS": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/os/
                :retorno:  osCadastro
                """
                return self._chamar_api(
                    call= 'ConsultarOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def excluir_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0,
                "cNumOS": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/os/
                :retorno:  osStatus
                """
                return self._chamar_api(
                    call= 'ExcluirOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def incluir_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "Cabecalho": 
                                "cCodIntOS": "1706038451",
                                "cCodParc": "999",
                                "cEtapa": "20",
                                "dDtPrevisao": "23/01/2024",
                                "nCodCli": 2485994,
                                "nQtdeParc": 7
                ,
                "Departamentos": [],
                "Email": 
                                "cEnvBoleto": "N",
                                "cEnvLink": "N",
                                "cEnviarPara": "teste@omie.com.br"
                ,
                "InformacoesAdicionais": 
                                "cCidPrestServ": "SAO PAULO (SP)",
                                "cCodCateg": "1.01.02",
                                "cDadosAdicNF": "OS incluida via API de teste 41384",
                                "nCodCC": 11850365
                ,
                "ServicosPrestados": [
                                
                                                "cCodServLC116": "7.07",
                                                "cCodServMun": "01015",
                                                "cDadosAdicItem": "Servi\u00e7os prestados",
                                                "cDescServ": "Servi\u00e7o prestado 001",
                                                "cRetemISS": "N",
                                                "cTribServ": "01",
                                                "impostos": 
                                                                "cRetemIRRF": "S",
                                                                "cRetemPIS": "S",
                                                                "nAliqCOFINS": 0,
                                                                "nAliqCSLL": 0,
                                                                "nAliqIRRF": 15,
                                                                "nAliqISS": 3,
                                                                "nAliqPIS": 4.5
                                                ,
                                                "nQtde": 3,
                                                "nValUnit": 1000
                                ,
                                
                                                "impostos": 
                                                                "cRetemIRRF": "S",
                                                                "cRetemPIS": "S",
                                                                "nAliqIRRF": 15,
                                                                "nAliqISS": 3,
                                                                "nAliqPIS": 4.5
                                                ,
                                                "nCodServico": 2342423,
                                                "nQtde": 12,
                                                "nValUnit": 35
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/os/
                :retorno:  osStatus
                """
                return self._chamar_api(
                    call= 'IncluirOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def listar_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/os/
                :retorno:  osListarResponse
                """
                return self._chamar_api(
                    call= 'ListarOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def status_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/os/
                :retorno:  osStatusResponse
                """
                return self._chamar_api(
                    call= 'StatusOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def trocar_etapa_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0,
                "cNumOS": "",
                "cEtapa": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/os/
                :retorno:  osTrocarEtapaResponse
                """
                return self._chamar_api(
                    call= 'TrocarEtapaOS',
                    endpoint= 'servicos/os/',
                    param = kargs
                )
            
    def associar_cod_int_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osp/
                :retorno:  osAssociarCodIntResponse
                """
                return self._chamar_api(
                    call= 'AssociarCodIntOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def cancelar_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osp/
                :retorno:  osCancelarResponse
                """
                return self._chamar_api(
                    call= 'CancelarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def duplicar_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osp/
                :retorno:  osDuplicarResponse
                """
                return self._chamar_api(
                    call= 'DuplicarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def faturar_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osp/
                :retorno:  osFaturarResponse
                """
                return self._chamar_api(
                    call= 'FaturarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def reenviar_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osp/
                :retorno:  osReenviarResponse
                """
                return self._chamar_api(
                    call= 'ReenviarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def validar_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntOS": "",
                "nCodOS": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/osp/
                :retorno:  osValidarResponse
                """
                return self._chamar_api(
                    call= 'ValidarOS',
                    endpoint= 'servicos/osp/',
                    param = kargs
                )
            
    def faturar_lote_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cEtapa": "50"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/oslote/
                :retorno:  FaturarLoteOSResponse
                """
                return self._chamar_api(
                    call= 'FaturarLoteOS',
                    endpoint= 'servicos/oslote/',
                    param = kargs
                )
            
    def listar_lote_nfse(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "dDtFat": "23/01/2024",
                "cStatusLote": "001"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/oslote/
                :retorno:  ListarLoteNfseResponse
                """
                return self._chamar_api(
                    call= 'ListarLoteNfse',
                    endpoint= 'servicos/oslote/',
                    param = kargs
                )
            
    def listar_lotes_o_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "dDtIncDe": "23/01/2024",
                "dDtIncAte": "23/01/2024"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/oslote/
                :retorno:  ListarLotesOSResponse
                """
                return self._chamar_api(
                    call= 'ListarLotesOS',
                    endpoint= 'servicos/oslote/',
                    param = kargs
                )
            
    def status_lote_o_s(self, **kargs) -> dict:
                """ 
                Status do lote faturado a partir do ID. 
                :exemplo de uso:
                {
                
                "nIdLoteFat": 45223245

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/oslote/
                :retorno:  StatusLoteOsResponse
                """
                return self._chamar_api(
                    call= 'StatusLoteOS',
                    endpoint= 'servicos/oslote/',
                    param = kargs
                )
            
    def alterar_contrato(self, **kargs) -> dict:
                """ 
                Alterar um Contrato 
                :exemplo de uso:
                {
                
                "cabecalho": 
                                "cCodIntCtr": "019289Tb2",
                                "cCodSit": "10",
                                "cNumCtr": "2020/01001",
                                "cTipoFat": "01",
                                "dVigFinal": "30/03/2022",
                                "dVigInicial": "29/03/2020",
                                "nCodCli": 2370765,
                                "nDiaFat": 30,
                                "nValTotMes": 3302
                ,
                "departamentos": [],
                "emailCliente": 
                                "cEnviarBoleto": "",
                                "cEnviarLinkNfse": "",
                                "cEnviarRecibo": "",
                                "cUtilizarEmails": ""
                ,
                "infAdic": 
                                "cCidPrestServ": "PETROPOLIS (RJ)",
                                "cCodART": "",
                                "cCodCateg": "1.01.02",
                                "cCodObra": "",
                                "cContato": "",
                                "cDadosAdicNF": "",
                                "nCodCC": 1208238,
                                "nCodProj": 0,
                                "nCodVend": 0
                ,
                "itensContrato": [
                                
                                                "itemCabecalho": 
                                                                "codIntItem": "1",
                                                                "cCodCategItem": "",
                                                                "cNaoGerarFinanceiro": "N",
                                                                "codLC116": "3.05",
                                                                "codNBS": "",
                                                                "codServMunic": "01292",
                                                                "codServico": 0,
                                                                "natOperacao": "01",
                                                                "quant": 1,
                                                                "seq": 1,
                                                                "valorDed": 0,
                                                                "valorTotal": 3002,
                                                                "valorUnit": 3002
                                                ,
                                                "itemDescrServ": 
                                                                "descrCompleta": "Servi\u00e7os prestados"
                                                ,
                                                "itemImpostos": 
                                                                "aliqCOFINS": 0,
                                                                "aliqCSLL": 0,
                                                                "aliqINSS": 0,
                                                                "aliqIR": 0,
                                                                "aliqISS": 5,
                                                                "aliqPIS": 0,
                                                                "redBaseINSS": 0,
                                                                "retCOFINS": "",
                                                                "retCSLL": "",
                                                                "retINSS": "",
                                                                "retIR": "",
                                                                "retISS": "N",
                                                                "retPIS": "",
                                                                "valorCOFINS": 0,
                                                                "valorCSLL": 0,
                                                                "valorINSS": 0,
                                                                "valorIR": 0,
                                                                "valorISS": 150.1,
                                                                "valorPIS": 0
                                                ,
                                                "itemLeiTranspImp": 
                                                                "aliMunicipal": 0,
                                                                "aliqEstadual": 0,
                                                                "aliqFederal": 0,
                                                                "chave": "",
                                                                "fonte": ""
                                                
                                ,
                                
                                                "itemCabecalho": 
                                                                "codIntItem": "2",
                                                                "cCodCategItem": "",
                                                                "cNaoGerarFinanceiro": "N",
                                                                "codLC116": "17.01",
                                                                "codNBS": "",
                                                                "codServMunic": "0162-8/99",
                                                                "codServico": 3412648,
                                                                "natOperacao": "01",
                                                                "quant": 1,
                                                                "seq": 2,
                                                                "valorDed": 0,
                                                                "valorTotal": 300,
                                                                "valorUnit": 300
                                                ,
                                                "itemDescrServ": 
                                                                "descrCompleta": "Homologa\u00e7\u00e3o de processo cont\u00e1bil"
                                                ,
                                                "itemImpostos": 
                                                                "aliqCOFINS": 0,
                                                                "aliqCSLL": 0,
                                                                "aliqINSS": 0,
                                                                "aliqIR": 0,
                                                                "aliqISS": 3,
                                                                "aliqPIS": 0,
                                                                "redBaseINSS": 0,
                                                                "retCOFINS": "",
                                                                "retCSLL": "",
                                                                "retINSS": "",
                                                                "retIR": "",
                                                                "retISS": "N",
                                                                "retPIS": "",
                                                                "valorCOFINS": 0,
                                                                "valorCSLL": 0,
                                                                "valorINSS": 0,
                                                                "valorIR": 0,
                                                                "valorISS": 9,
                                                                "valorPIS": 0
                                                ,
                                                "itemLeiTranspImp": 
                                                                "aliMunicipal": 0,
                                                                "aliqEstadual": 0,
                                                                "aliqFederal": 0,
                                                                "chave": "",
                                                                "fonte": ""
                                                
                                
                ],
                "observacoes": 
                                "cObsContrato": ""
                ,
                "vencTextos": 
                                "cAdContrato": "N",
                                "cAdPeriodo": "N",
                                "cAdVenc": " ",
                                "cAntecipar": "",
                                "cCodPerRef": "001",
                                "cDiaFim": 0,
                                "cDiaIni": 0,
                                "cPostergar": "",
                                "cProxMes": "",
                                "cTpVenc": "001",
                                "nDiaFixo": 0,
                                "nDias": 5
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contrato/
                :retorno:  csStatus
                """
                return self._chamar_api(
                    call= 'AlterarContrato',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def consultar_contrato(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "contratoChave": 
                                "nCodCtr": 2203958
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contrato/
                :retorno:  csConsultarResponse
                """
                return self._chamar_api(
                    call= 'ConsultarContrato',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def excluir_item(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "contratoChave": 
                                "nCodCtr": 0,
                                "cCodIntCtr": ""
                ,
                "ItensExclusao": [
                                
                                                "codItem": 0,
                                                "codIntItem": ""
                                
                ]

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contrato/
                :retorno:  csExcluirItemResponse
                """
                return self._chamar_api(
                    call= 'ExcluirItem',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def incluir_contrato(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cabecalho": 
                                "cCodIntCtr": "019289Tb2",
                                "cCodSit": "10",
                                "cNumCtr": "2020/01001",
                                "cTipoFat": "01",
                                "dVigFinal": "30/03/2022",
                                "dVigInicial": "29/03/2020",
                                "nCodCli": 2370765,
                                "nDiaFat": 30,
                                "nValTotMes": 3302
                ,
                "departamentos": [],
                "emailCliente": 
                                "cEnviarBoleto": "",
                                "cEnviarLinkNfse": "",
                                "cEnviarRecibo": "",
                                "cUtilizarEmails": ""
                ,
                "infAdic": 
                                "cCidPrestServ": "PETROPOLIS (RJ)",
                                "cCodART": "",
                                "cCodCateg": "1.01.02",
                                "cCodObra": "",
                                "cContato": "",
                                "cDadosAdicNF": "",
                                "nCodCC": 1208238,
                                "nCodProj": 0,
                                "nCodVend": 0
                ,
                "itensContrato": [
                                
                                                "itemCabecalho": 
                                                                "codIntItem": "1",
                                                                "cCodCategItem": "",
                                                                "cNaoGerarFinanceiro": "N",
                                                                "codLC116": "3.05",
                                                                "codNBS": "",
                                                                "codServMunic": "01292",
                                                                "codServico": 0,
                                                                "natOperacao": "01",
                                                                "quant": 1,
                                                                "seq": 1,
                                                                "valorDed": 0,
                                                                "valorTotal": 3002,
                                                                "valorUnit": 3002
                                                ,
                                                "itemDescrServ": 
                                                                "descrCompleta": "Servi\u00e7os prestados"
                                                ,
                                                "itemImpostos": 
                                                                "aliqCOFINS": 0,
                                                                "aliqCSLL": 0,
                                                                "aliqINSS": 0,
                                                                "aliqIR": 0,
                                                                "aliqISS": 5,
                                                                "aliqPIS": 0,
                                                                "redBaseINSS": 0,
                                                                "retCOFINS": "",
                                                                "retCSLL": "",
                                                                "retINSS": "",
                                                                "retIR": "",
                                                                "retISS": "N",
                                                                "retPIS": "",
                                                                "valorCOFINS": 0,
                                                                "valorCSLL": 0,
                                                                "valorINSS": 0,
                                                                "valorIR": 0,
                                                                "valorISS": 150.1,
                                                                "valorPIS": 0
                                                ,
                                                "itemLeiTranspImp": 
                                                                "aliMunicipal": 0,
                                                                "aliqEstadual": 0,
                                                                "aliqFederal": 0,
                                                                "chave": "",
                                                                "fonte": ""
                                                
                                ,
                                
                                                "itemCabecalho": 
                                                                "codIntItem": "2",
                                                                "cCodCategItem": "",
                                                                "cNaoGerarFinanceiro": "N",
                                                                "codLC116": "17.01",
                                                                "codNBS": "",
                                                                "codServMunic": "0162-8/99",
                                                                "codServico": 3412648,
                                                                "natOperacao": "01",
                                                                "quant": 1,
                                                                "seq": 2,
                                                                "valorDed": 0,
                                                                "valorTotal": 300,
                                                                "valorUnit": 300
                                                ,
                                                "itemDescrServ": 
                                                                "descrCompleta": "Homologa\u00e7\u00e3o de processo cont\u00e1bil"
                                                ,
                                                "itemImpostos": 
                                                                "aliqCOFINS": 0,
                                                                "aliqCSLL": 0,
                                                                "aliqINSS": 0,
                                                                "aliqIR": 0,
                                                                "aliqISS": 3,
                                                                "aliqPIS": 0,
                                                                "redBaseINSS": 0,
                                                                "retCOFINS": "",
                                                                "retCSLL": "",
                                                                "retINSS": "",
                                                                "retIR": "",
                                                                "retISS": "N",
                                                                "retPIS": "",
                                                                "valorCOFINS": 0,
                                                                "valorCSLL": 0,
                                                                "valorINSS": 0,
                                                                "valorIR": 0,
                                                                "valorISS": 9,
                                                                "valorPIS": 0
                                                ,
                                                "itemLeiTranspImp": 
                                                                "aliMunicipal": 0,
                                                                "aliqEstadual": 0,
                                                                "aliqFederal": 0,
                                                                "chave": "",
                                                                "fonte": ""
                                                
                                
                ],
                "observacoes": 
                                "cObsContrato": ""
                ,
                "vencTextos": 
                                "cAdContrato": "N",
                                "cAdPeriodo": "N",
                                "cAdVenc": " ",
                                "cAntecipar": "",
                                "cCodPerRef": "001",
                                "cDiaFim": 0,
                                "cDiaIni": 0,
                                "cPostergar": "",
                                "cProxMes": "",
                                "cTpVenc": "001",
                                "nDiaFixo": 0,
                                "nDias": 5
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contrato/
                :retorno:  csStatus
                """
                return self._chamar_api(
                    call= 'IncluirContrato',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def listar_contratos(self, **kargs) -> dict:
                """ 
                Lista os contratos cadastrados. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 50,
                "apenas_importado_api": "N"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contrato/
                :retorno:  csListarResponse
                """
                return self._chamar_api(
                    call= 'ListarContratos',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def upsert_contrato(self, **kargs) -> dict:
                """ 
                Inclui / Altera um contrato 
                :exemplo de uso:
                {
                
                "cabecalho": 
                                "cCodIntCtr": "019289Tb2",
                                "cCodSit": "10",
                                "cNumCtr": "2020/01001",
                                "cTipoFat": "01",
                                "dVigFinal": "30/03/2022",
                                "dVigInicial": "29/03/2020",
                                "nCodCli": 2370765,
                                "nDiaFat": 30,
                                "nValTotMes": 3302
                ,
                "departamentos": [],
                "emailCliente": 
                                "cEnviarBoleto": "",
                                "cEnviarLinkNfse": "",
                                "cEnviarRecibo": "",
                                "cUtilizarEmails": ""
                ,
                "infAdic": 
                                "cCidPrestServ": "PETROPOLIS (RJ)",
                                "cCodART": "",
                                "cCodCateg": "1.01.02",
                                "cCodObra": "",
                                "cContato": "",
                                "cDadosAdicNF": "",
                                "nCodCC": 1208238,
                                "nCodProj": 0,
                                "nCodVend": 0
                ,
                "itensContrato": [
                                
                                                "itemCabecalho": 
                                                                "codIntItem": "1",
                                                                "cCodCategItem": "",
                                                                "cNaoGerarFinanceiro": "N",
                                                                "codLC116": "3.05",
                                                                "codNBS": "",
                                                                "codServMunic": "01292",
                                                                "codServico": 0,
                                                                "natOperacao": "01",
                                                                "quant": 1,
                                                                "seq": 1,
                                                                "valorDed": 0,
                                                                "valorTotal": 3002,
                                                                "valorUnit": 3002
                                                ,
                                                "itemDescrServ": 
                                                                "descrCompleta": "Servi\u00e7os prestados"
                                                ,
                                                "itemImpostos": 
                                                                "aliqCOFINS": 0,
                                                                "aliqCSLL": 0,
                                                                "aliqINSS": 0,
                                                                "aliqIR": 0,
                                                                "aliqISS": 5,
                                                                "aliqPIS": 0,
                                                                "redBaseINSS": 0,
                                                                "retCOFINS": "",
                                                                "retCSLL": "",
                                                                "retINSS": "",
                                                                "retIR": "",
                                                                "retISS": "N",
                                                                "retPIS": "",
                                                                "valorCOFINS": 0,
                                                                "valorCSLL": 0,
                                                                "valorINSS": 0,
                                                                "valorIR": 0,
                                                                "valorISS": 150.1,
                                                                "valorPIS": 0
                                                ,
                                                "itemLeiTranspImp": 
                                                                "aliMunicipal": 0,
                                                                "aliqEstadual": 0,
                                                                "aliqFederal": 0,
                                                                "chave": "",
                                                                "fonte": ""
                                                
                                ,
                                
                                                "itemCabecalho": 
                                                                "codIntItem": "2",
                                                                "cCodCategItem": "",
                                                                "cNaoGerarFinanceiro": "N",
                                                                "codLC116": "17.01",
                                                                "codNBS": "",
                                                                "codServMunic": "0162-8/99",
                                                                "codServico": 3412648,
                                                                "natOperacao": "01",
                                                                "quant": 1,
                                                                "seq": 2,
                                                                "valorDed": 0,
                                                                "valorTotal": 300,
                                                                "valorUnit": 300
                                                ,
                                                "itemDescrServ": 
                                                                "descrCompleta": "Homologa\u00e7\u00e3o de processo cont\u00e1bil"
                                                ,
                                                "itemImpostos": 
                                                                "aliqCOFINS": 0,
                                                                "aliqCSLL": 0,
                                                                "aliqINSS": 0,
                                                                "aliqIR": 0,
                                                                "aliqISS": 3,
                                                                "aliqPIS": 0,
                                                                "redBaseINSS": 0,
                                                                "retCOFINS": "",
                                                                "retCSLL": "",
                                                                "retINSS": "",
                                                                "retIR": "",
                                                                "retISS": "N",
                                                                "retPIS": "",
                                                                "valorCOFINS": 0,
                                                                "valorCSLL": 0,
                                                                "valorINSS": 0,
                                                                "valorIR": 0,
                                                                "valorISS": 9,
                                                                "valorPIS": 0
                                                ,
                                                "itemLeiTranspImp": 
                                                                "aliMunicipal": 0,
                                                                "aliqEstadual": 0,
                                                                "aliqFederal": 0,
                                                                "chave": "",
                                                                "fonte": ""
                                                
                                
                ],
                "observacoes": 
                                "cObsContrato": ""
                ,
                "vencTextos": 
                                "cAdContrato": "N",
                                "cAdPeriodo": "N",
                                "cAdVenc": " ",
                                "cAntecipar": "",
                                "cCodPerRef": "001",
                                "cDiaFim": 0,
                                "cDiaIni": 0,
                                "cPostergar": "",
                                "cProxMes": "",
                                "cTpVenc": "001",
                                "nDiaFixo": 0,
                                "nDias": 5
                

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contrato/
                :retorno:  csStatus
                """
                return self._chamar_api(
                    call= 'UpsertContrato',
                    endpoint= 'servicos/contrato/',
                    param = kargs
                )
            
    def ativar_contrato(self, **kargs) -> dict:
                """ 
                Ativa um contrato 
                :exemplo de uso:
                {
                
                "nCodCtr": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratofat/
                :retorno:  ctrAtivarResponse
                """
                return self._chamar_api(
                    call= 'AtivarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def cancelar_contrato(self, **kargs) -> dict:
                """ 
                Cancela contrato 
                :exemplo de uso:
                {
                
                "nCodCtr": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratofat/
                :retorno:  ctrCancelarResponse
                """
                return self._chamar_api(
                    call= 'CancelarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def faturar_contrato(self, **kargs) -> dict:
                """ 
                Fatura um contrato. 
                :exemplo de uso:
                {
                
                "nCodCtr": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratofat/
                :retorno:  ctrFaturarResponse
                """
                return self._chamar_api(
                    call= 'FaturarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def obter_contratos(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cEtapa": "50"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratofat/
                :retorno:  ctrObterResponse
                """
                return self._chamar_api(
                    call= 'ObterContratos',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def reativar_contrato(self, **kargs) -> dict:
                """ 
                Reativar contrato 
                :exemplo de uso:
                {
                
                "nCodCtr": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratofat/
                :retorno:  ctrReativarResponse
                """
                return self._chamar_api(
                    call= 'ReativarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def suspender_contrato(self, **kargs) -> dict:
                """ 
                Suspende contrato 
                :exemplo de uso:
                {
                
                "nCodCtr": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratofat/
                :retorno:  ctrSuspenderResponse
                """
                return self._chamar_api(
                    call= 'SuspenderContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def validar_contrato(self, **kargs) -> dict:
                """ 
                Valida os dados de um contrato para faturamento. 
                :exemplo de uso:
                {
                
                "nCodCtr": 0

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratofat/
                :retorno:  ctrValidarResponse
                """
                return self._chamar_api(
                    call= 'ValidarContrato',
                    endpoint= 'servicos/contratofat/',
                    param = kargs
                )
            
    def faturar_lote_contrato(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "cCodIntLote": "9999999"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratolote/
                :retorno:  FaturarLoteContratoResponse
                """
                return self._chamar_api(
                    call= 'FaturarLoteContrato',
                    endpoint= 'servicos/contratolote/',
                    param = kargs
                )
            
    def listar_lotes_contrato(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "dDtIncDe": "23/01/2024",
                "dDtIncAte": "23/01/2024"

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratolote/
                :retorno:  ListarLotesContratoResponse
                """
                return self._chamar_api(
                    call= 'ListarLotesContrato',
                    endpoint= 'servicos/contratolote/',
                    param = kargs
                )
            
    def status_lote_contrato(self, **kargs) -> dict:
                """ 
                Status do lote faturado a partir do ID. 
                :exemplo de uso:
                {
                
                "nIdLoteFat": 45223245

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratolote/
                :retorno:  StatusLoteContratoResponse
                """
                return self._chamar_api(
                    call= 'StatusLoteContrato',
                    endpoint= 'servicos/contratolote/',
                    param = kargs
                )
            
    def listar_serv_munic(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/listaservico/
                :retorno:  sermListarResponse
                """
                return self._chamar_api(
                    call= 'ListarServMunic',
                    endpoint= 'servicos/listaservico/',
                    param = kargs
                )
            
    def listar_tipos_trib(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/tipotrib/
                :retorno:  tribListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTiposTrib',
                    endpoint= 'servicos/tipotrib/',
                    param = kargs
                )
            
    def listar_l_c116(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/lc116/
                :retorno:  lc116ListarResponse
                """
                return self._chamar_api(
                    call= 'ListarLC116',
                    endpoint= 'servicos/lc116/',
                    param = kargs
                )
            
    def listar_n_b_s(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/nbs/
                :retorno:  nbsListarResponse
                """
                return self._chamar_api(
                    call= 'ListarNBS',
                    endpoint= 'servicos/nbs/',
                    param = kargs
                )
            
    def listar_produtos_i_b_p_t(self, **kargs) -> dict:
                """ 
                Lista os produtos da Tabela do IBPT. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/ibpt/
                :retorno:  ibptListarProdResponse
                """
                return self._chamar_api(
                    call= 'ListarProdutosIBPT',
                    endpoint= 'servicos/ibpt/',
                    param = kargs
                )
            
    def listar_servicos_i_b_p_t(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/ibpt/
                :retorno:  ibptListarServResponse
                """
                return self._chamar_api(
                    call= 'ListarServicosIBPT',
                    endpoint= 'servicos/ibpt/',
                    param = kargs
                )
            
    def listar_tipo_fat_contrato(self, **kargs) -> dict:
                """ 
                Lista os tipos de faturamento de contrato. 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/contratotpfat/
                :retorno:  tfCtrListarResponse
                """
                return self._chamar_api(
                    call= 'ListarTipoFatContrato',
                    endpoint= 'servicos/contratotpfat/',
                    param = kargs
                )
            
    def listar_tipo_utilizacao(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/tipoutilizacao/
                :retorno:  tipoUtilizacaoResponse
                """
                return self._chamar_api(
                    call= 'ListarTipoUtilizacao',
                    endpoint= 'servicos/tipoutilizacao/',
                    param = kargs
                )
            
    def listar_classificacao_servico(self, **kargs) -> dict:
                """ 
                 
                :exemplo de uso:
                {
                
                "pagina": 1,
                "registros_por_pagina": 20

                }
                
                :link metodo: https://app.omie.com.br/api/v1/servicos/classificacaoservico/
                :retorno:  classificaServicoResponse
                """
                return self._chamar_api(
                    call= 'ListarClassificacaoServico',
                    endpoint= 'servicos/classificacaoservico/',
                    param = kargs
                )
            
    def listar_documentos(self, **kargs) -> dict:
                """ 
                Lista de XMLs de Documentos Fiscais. 
                :exemplo de uso:
                {
                
                "nPagina": 1,
                "nRegPorPagina": 20,
                "cModelo": "55",
                "dEmiInicial": "",
                "dEmiFinal": ""

                }
                
                :link metodo: https://app.omie.com.br/api/v1/contador/xml/
                :retorno:  xmlListarDocumentosResponse
                """
                return self._chamar_api(
                    call= 'ListarDocumentos',
                    endpoint= 'contador/xml/',
                    param = kargs
                )
            