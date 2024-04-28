<?php

include("omieBase.php");

class OmieAuto extends OmieBase{


    public function alterarCliente(array $parametros): array { 
                    //Altera os dados do cliente
                    return $this->chamarApi(
                        "geral/clientes/",
                        "AlterarCliente",
                        $parametros
                    );
            }
                
    public function associarCodIntCliente(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "AssociarCodIntCliente",
                        $parametros
                    );
            }
                
    public function consultarCliente(array $parametros): array { 
                    //Consulta os dados de um cliente 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "ConsultarCliente",
                        $parametros
                    );
            }
                
    public function excluirCliente(array $parametros): array { 
                    //Exclui um cliente da base de dados. 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "ExcluirCliente",
                        $parametros
                    );
            }
                
    public function incluirCliente(array $parametros): array { 
                    //Inclui o cliente no Omie 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "IncluirCliente",
                        $parametros
                    );
            }
                
    public function incluirClientesPorLote(array $parametros): array { 
                    //DEPRECATED 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "IncluirClientesPorLote",
                        $parametros
                    );
            }
                
    public function listarClientes(array $parametros): array { 
                    //Lista os clientes cadastrados 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "ListarClientes",
                        $parametros
                    );
            }
                
    public function listarClientesResumido(array $parametros): array { 
                    //Realiza pesquisa dos clientes 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "ListarClientesResumido",
                        $parametros
                    );
            }
                
    public function upsertCliente(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "UpsertCliente",
                        $parametros
                    );
            }
                
    public function upsertClienteCpfCnpj(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "UpsertClienteCpfCnpj",
                        $parametros
                    );
            }
                
    public function upsertClientesPorLote(array $parametros): array { 
                    //DEPRECATED 
                    return $this->chamarApi(
                        "geral/clientes/",
                        "UpsertClientesPorLote",
                        $parametros
                    );
            }
                
    public function alterarCaractCliente(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/clientescaract/",
                        "AlterarCaractCliente",
                        $parametros
                    );
            }
                
    public function consultarCaractCliente(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/clientescaract/",
                        "ConsultarCaractCliente",
                        $parametros
                    );
            }
                
    public function excluirCaractCliente(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/clientescaract/",
                        "ExcluirCaractCliente",
                        $parametros
                    );
            }
                
    public function excluirTodasCaractCliente(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/clientescaract/",
                        "ExcluirTodasCaractCliente",
                        $parametros
                    );
            }
                
    public function incluirCaractCliente(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/clientescaract/",
                        "IncluirCaractCliente",
                        $parametros
                    );
            }
                
    public function excluirTags(array $parametros): array { 
                    //Remove tags associadas a um cliente. 
                    return $this->chamarApi(
                        "geral/clientetag/",
                        "ExcluirTags",
                        $parametros
                    );
            }
                
    public function excluirTodas(array $parametros): array { 
                    //Remove todas as tags associadas a um cliente. 
                    return $this->chamarApi(
                        "geral/clientetag/",
                        "ExcluirTodas",
                        $parametros
                    );
            }
                
    public function incluirTags(array $parametros): array { 
                    //Associa tags a um cliente. 
                    return $this->chamarApi(
                        "geral/clientetag/",
                        "IncluirTags",
                        $parametros
                    );
            }
                
    public function listarTags(array $parametros): array { 
                    //Lista as tags de um determinado cliente. 
                    return $this->chamarApi(
                        "geral/clientetag/",
                        "ListarTags",
                        $parametros
                    );
            }
                
    public function alterarProjeto(array $parametros): array { 
                    //Altera um projeto 
                    return $this->chamarApi(
                        "geral/projetos/",
                        "AlterarProjeto",
                        $parametros
                    );
            }
                
    public function consultarProjeto(array $parametros): array { 
                    //Consulta um projeto 
                    return $this->chamarApi(
                        "geral/projetos/",
                        "ConsultarProjeto",
                        $parametros
                    );
            }
                
    public function excluirProjeto(array $parametros): array { 
                    //Exclui um projeto 
                    return $this->chamarApi(
                        "geral/projetos/",
                        "ExcluirProjeto",
                        $parametros
                    );
            }
                
    public function incluirProjeto(array $parametros): array { 
                    //Inclui um novo projeto 
                    return $this->chamarApi(
                        "geral/projetos/",
                        "IncluirProjeto",
                        $parametros
                    );
            }
                
    public function listarProjetos(array $parametros): array { 
                    //Lista os projetos cadastrados 
                    return $this->chamarApi(
                        "geral/projetos/",
                        "ListarProjetos",
                        $parametros
                    );
            }
                
    public function upsertProjeto(array $parametros): array { 
                    //Inclui / Altera um projeto. 
                    return $this->chamarApi(
                        "geral/projetos/",
                        "UpsertProjeto",
                        $parametros
                    );
            }
                
    public function consultarEmpresa(array $parametros): array { 
                    //Realiza a consulta de um registro especifico 
                    return $this->chamarApi(
                        "geral/empresas/",
                        "ConsultarEmpresa",
                        $parametros
                    );
            }
                
    public function listarEmpresas(array $parametros): array { 
                    //Lista as empresas cadastradas no Omie. 
                    return $this->chamarApi(
                        "geral/empresas/",
                        "ListarEmpresas",
                        $parametros
                    );
            }
                
    public function alterarDepartamento(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/departamentos/",
                        "AlterarDepartamento",
                        $parametros
                    );
            }
                
    public function consultarDepartamento(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/departamentos/",
                        "ConsultarDepartamento",
                        $parametros
                    );
            }
                
    public function excluirDepartamento(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/departamentos/",
                        "ExcluirDepartamento",
                        $parametros
                    );
            }
                
    public function incluirDepartamento(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/departamentos/",
                        "IncluirDepartamento",
                        $parametros
                    );
            }
                
    public function listarDepartamentos(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/departamentos/",
                        "ListarDepartamentos",
                        $parametros
                    );
            }
                
    public function listarDepatartamentos(array $parametros): array { 
                    //DEPRECATED 
                    return $this->chamarApi(
                        "geral/departamentos/",
                        "ListarDepatartamentos",
                        $parametros
                    );
            }
                
    public function alterarCategoria(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/categorias/",
                        "AlterarCategoria",
                        $parametros
                    );
            }
                
    public function alterarGrupoCategoria(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/categorias/",
                        "AlterarGrupoCategoria",
                        $parametros
                    );
            }
                
    public function consultarCategoria(array $parametros): array { 
                    //Consulta uma categoria 
                    return $this->chamarApi(
                        "geral/categorias/",
                        "ConsultarCategoria",
                        $parametros
                    );
            }
                
    public function incluirCategoria(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/categorias/",
                        "IncluirCategoria",
                        $parametros
                    );
            }
                
    public function incluirGrupoCategoria(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/categorias/",
                        "IncluirGrupoCategoria",
                        $parametros
                    );
            }
                
    public function listarCategorias(array $parametros): array { 
                    //Lista as categorias cadastradas 
                    return $this->chamarApi(
                        "geral/categorias/",
                        "ListarCategorias",
                        $parametros
                    );
            }
                
    public function listarParcelas(array $parametros): array { 
                    //Lista de Parcelas cadastradas. 
                    return $this->chamarApi(
                        "geral/parcelas/",
                        "ListarParcelas",
                        $parametros
                    );
            }
                
    public function listarTipoAtiv(array $parametros): array { 
                    //Listar Tipos de Atividade. 
                    return $this->chamarApi(
                        "geral/tpativ/",
                        "ListarTipoAtiv",
                        $parametros
                    );
            }
                
    public function listarCNAE(array $parametros): array { 
                    //Listar os CNAEs cadastrados 
                    return $this->chamarApi(
                        "produtos/cnae/",
                        "ListarCNAE",
                        $parametros
                    );
            }
                
    public function pesquisarCidades(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/cidades/",
                        "PesquisarCidades",
                        $parametros
                    );
            }
                
    public function listarPaises(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/paises/",
                        "ListarPaises",
                        $parametros
                    );
            }
                
    public function listarTiposAnexos(array $parametros): array { 
                    //Listagem de tipos de anexos. 
                    return $this->chamarApi(
                        "geral/tiposanexo/",
                        "ListarTiposAnexos",
                        $parametros
                    );
            }
                
    public function consultarAnexo(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/anexo/",
                        "ConsultarAnexo",
                        $parametros
                    );
            }
                
    public function excluirAnexo(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/anexo/",
                        "ExcluirAnexo",
                        $parametros
                    );
            }
                
    public function incluirAnexo(array $parametros): array { 
                    //Inclui o anexo para um documento. 
                    return $this->chamarApi(
                        "geral/anexo/",
                        "IncluirAnexo",
                        $parametros
                    );
            }
                
    public function listarAnexo(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/anexo/",
                        "ListarAnexo",
                        $parametros
                    );
            }
                
    public function obterAnexo(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/anexo/",
                        "ObterAnexo",
                        $parametros
                    );
            }
                
    public function alterarTipoEntrega(array $parametros): array { 
                    //Alterar tipo de entrega 
                    return $this->chamarApi(
                        "geral/tiposentrega/",
                        "AlterarTipoEntrega",
                        $parametros
                    );
            }
                
    public function consultarTipoEntrega(array $parametros): array { 
                    //Consultar tipo de entrega 
                    return $this->chamarApi(
                        "geral/tiposentrega/",
                        "ConsultarTipoEntrega",
                        $parametros
                    );
            }
                
    public function excluirTipoEntrega(array $parametros): array { 
                    //Excluir tipo de entrega 
                    return $this->chamarApi(
                        "geral/tiposentrega/",
                        "ExcluirTipoEntrega",
                        $parametros
                    );
            }
                
    public function incluirTipoEntrega(array $parametros): array { 
                    //Incluir tipo de entrega 
                    return $this->chamarApi(
                        "geral/tiposentrega/",
                        "IncluirTipoEntrega",
                        $parametros
                    );
            }
                
    public function listarTipoEntrega(array $parametros): array { 
                    //Listar tipo de entrega 
                    return $this->chamarApi(
                        "geral/tiposentrega/",
                        "ListarTipoEntrega",
                        $parametros
                    );
            }
                
    public function listarTipoAssinante(array $parametros): array { 
                    //Lista os tipos de assinante 
                    return $this->chamarApi(
                        "geral/tipoassinante/",
                        "ListarTipoAssinante",
                        $parametros
                    );
            }
                
    public function alterarConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contas/",
                        "AlterarConta",
                        $parametros
                    );
            }
                
    public function consultarConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contas/",
                        "ConsultarConta",
                        $parametros
                    );
            }
                
    public function excluirConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contas/",
                        "ExcluirConta",
                        $parametros
                    );
            }
                
    public function incluirConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contas/",
                        "IncluirConta",
                        $parametros
                    );
            }
                
    public function listarContas(array $parametros): array { 
                    //Lista as contas do CRM. 
                    return $this->chamarApi(
                        "crm/contas/",
                        "ListarContas",
                        $parametros
                    );
            }
                
    public function upsertConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contas/",
                        "UpsertConta",
                        $parametros
                    );
            }
                
    public function verificarConta(array $parametros): array { 
                    //Verifica se uma conta foi criada a partir do nome e e-mail. 
                    return $this->chamarApi(
                        "crm/contas/",
                        "VerificarConta",
                        $parametros
                    );
            }
                
    public function alterarCaractConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contascaract/",
                        "AlterarCaractConta",
                        $parametros
                    );
            }
                
    public function consultarCaractConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contascaract/",
                        "ConsultarCaractConta",
                        $parametros
                    );
            }
                
    public function excluirCaractConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contascaract/",
                        "ExcluirCaractConta",
                        $parametros
                    );
            }
                
    public function excluirTodasCaractConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contascaract/",
                        "ExcluirTodasCaractConta",
                        $parametros
                    );
            }
                
    public function incluirCaractConta(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contascaract/",
                        "IncluirCaractConta",
                        $parametros
                    );
            }
                
    public function alterarContato(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contatos/",
                        "AlterarContato",
                        $parametros
                    );
            }
                
    public function consultarContato(array $parametros): array { 
                    //Consulta o Contato 
                    return $this->chamarApi(
                        "crm/contatos/",
                        "ConsultarContato",
                        $parametros
                    );
            }
                
    public function excluirContato(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contatos/",
                        "ExcluirContato",
                        $parametros
                    );
            }
                
    public function incluirContato(array $parametros): array { 
                    //Inclui um novo Contato 
                    return $this->chamarApi(
                        "crm/contatos/",
                        "IncluirContato",
                        $parametros
                    );
            }
                
    public function listarContatos(array $parametros): array { 
                    //Lista os contatos do CRM. 
                    return $this->chamarApi(
                        "crm/contatos/",
                        "ListarContatos",
                        $parametros
                    );
            }
                
    public function upsertContato(array $parametros): array { 
                    //Upsert do contato 
                    return $this->chamarApi(
                        "crm/contatos/",
                        "UpsertContato",
                        $parametros
                    );
            }
                
    public function verificarContato(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/contatos/",
                        "VerificarContato",
                        $parametros
                    );
            }
                
    public function alterarOportunidade(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/oportunidades/",
                        "AlterarOportunidade",
                        $parametros
                    );
            }
                
    public function consultarOportunidade(array $parametros): array { 
                    //Consulta de oportunidade. 
                    return $this->chamarApi(
                        "crm/oportunidades/",
                        "ConsultarOportunidade",
                        $parametros
                    );
            }
                
    public function excluirOportunidade(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/oportunidades/",
                        "ExcluirOportunidade",
                        $parametros
                    );
            }
                
    public function incluirOportunidade(array $parametros): array { 
                    //Incluir uma oportunidade. 
                    return $this->chamarApi(
                        "crm/oportunidades/",
                        "IncluirOportunidade",
                        $parametros
                    );
            }
                
    public function listarOportunidades(array $parametros): array { 
                    //Lista de oportunidades. 
                    return $this->chamarApi(
                        "crm/oportunidades/",
                        "ListarOportunidades",
                        $parametros
                    );
            }
                
    public function upsertOportunidade(array $parametros): array { 
                    //Upsert de oportunidade. 
                    return $this->chamarApi(
                        "crm/oportunidades/",
                        "UpsertOportunidade",
                        $parametros
                    );
            }
                
    public function obterListaOp(array $parametros): array { 
                    //Lista de Oportunidades. 
                    return $this->chamarApi(
                        "crm/oportunidades-resumo/",
                        "ObterListaOp",
                        $parametros
                    );
            }
                
    public function obterResumoOp(array $parametros): array { 
                    //Resumo das oportunidades. 
                    return $this->chamarApi(
                        "crm/oportunidades-resumo/",
                        "ObterResumoOp",
                        $parametros
                    );
            }
                
    public function alterarTarefa(array $parametros): array { 
                    //Altera uma tarefa. 
                    return $this->chamarApi(
                        "crm/tarefas/",
                        "AlterarTarefa",
                        $parametros
                    );
            }
                
    public function calendarioTarefas(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/tarefas/",
                        "CalendarioTarefas",
                        $parametros
                    );
            }
                
    public function consultarTarefa(array $parametros): array { 
                    //Consulta uma tarefa da oportunidade. 
                    return $this->chamarApi(
                        "crm/tarefas/",
                        "ConsultarTarefa",
                        $parametros
                    );
            }
                
    public function excluirTarefa(array $parametros): array { 
                    //Exclui um tarefa. 
                    return $this->chamarApi(
                        "crm/tarefas/",
                        "ExcluirTarefa",
                        $parametros
                    );
            }
                
    public function incluirTarefa(array $parametros): array { 
                    //Inclui uma tarefa na oportunidade. 
                    return $this->chamarApi(
                        "crm/tarefas/",
                        "IncluirTarefa",
                        $parametros
                    );
            }
                
    public function listarEmailsTarefas(array $parametros): array { 
                    //Lista os  emails tarefas. 
                    return $this->chamarApi(
                        "crm/tarefas/",
                        "ListarEmailsTarefas",
                        $parametros
                    );
            }
                
    public function listarTarefas(array $parametros): array { 
                    //Tarefas da oportunidade. 
                    return $this->chamarApi(
                        "crm/tarefas/",
                        "ListarTarefas",
                        $parametros
                    );
            }
                
    public function upsertTarefa(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/tarefas/",
                        "UpsertTarefa",
                        $parametros
                    );
            }
                
    public function obterDetalhesTarefa(array $parametros): array { 
                    //Consulta os detalhes de uma tafera. 
                    return $this->chamarApi(
                        "crm/tarefas-resumo/",
                        "ObterDetalhesTarefa",
                        $parametros
                    );
            }
                
    public function obterListaTarefas(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/tarefas-resumo/",
                        "ObterListaTarefas",
                        $parametros
                    );
            }
                
    public function obterResumoTarefas(array $parametros): array { 
                    //Resumos das tarefas do CRM. 
                    return $this->chamarApi(
                        "crm/tarefas-resumo/",
                        "ObterResumoTarefas",
                        $parametros
                    );
            }
                
    public function listarSolucoes(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/solucoes/",
                        "ListarSolucoes",
                        $parametros
                    );
            }
                
    public function listarFases(array $parametros): array { 
                    //Fases da Oportunidade 
                    return $this->chamarApi(
                        "crm/fases/",
                        "ListarFases",
                        $parametros
                    );
            }
                
    public function listarUsuarios(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/usuarios/",
                        "ListarUsuarios",
                        $parametros
                    );
            }
                
    public function obterUsuarios(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "crm/usuarios/",
                        "ObterUsuarios",
                        $parametros
                    );
            }
                
    public function listarStatus(array $parametros): array { 
                    //Status da oportunidade. 
                    return $this->chamarApi(
                        "crm/status/",
                        "ListarStatus",
                        $parametros
                    );
            }
                
    public function listarMotivos(array $parametros): array { 
                    //Motivos da oportunidade. 
                    return $this->chamarApi(
                        "crm/motivos/",
                        "ListarMotivos",
                        $parametros
                    );
            }
                
    public function listarTipos(array $parametros): array { 
                    //Tipos de oportunidades. 
                    return $this->chamarApi(
                        "crm/tipos/",
                        "ListarTipos",
                        $parametros
                    );
            }
                
    public function listarParceiros(array $parametros): array { 
                    //Parceiros e equipes da oportunidade. 
                    return $this->chamarApi(
                        "crm/parceiros/",
                        "ListarParceiros",
                        $parametros
                    );
            }
                
    public function listarFinders(array $parametros): array { 
                    //Finders da oportunidade. 
                    return $this->chamarApi(
                        "crm/finders/",
                        "ListarFinders",
                        $parametros
                    );
            }
                
    public function listarOrigens(array $parametros): array { 
                    //Origens da oportunidade. 
                    return $this->chamarApi(
                        "crm/origens/",
                        "ListarOrigens",
                        $parametros
                    );
            }
                
    public function listarConcorrentes(array $parametros): array { 
                    //Concorrentes da oportunidade. 
                    return $this->chamarApi(
                        "crm/concorrentes/",
                        "ListarConcorrentes",
                        $parametros
                    );
            }
                
    public function listarVerticais(array $parametros): array { 
                    //Lista as verticais cadastradas. 
                    return $this->chamarApi(
                        "crm/verticais/",
                        "ListarVerticais",
                        $parametros
                    );
            }
                
    public function alterarVendedor(array $parametros): array { 
                    //Altera os dados de um vendedor 
                    return $this->chamarApi(
                        "geral/vendedores/",
                        "AlterarVendedor",
                        $parametros
                    );
            }
                
    public function consultarVendedor(array $parametros): array { 
                    //Consulta os dados de um vendedor 
                    return $this->chamarApi(
                        "geral/vendedores/",
                        "ConsultarVendedor",
                        $parametros
                    );
            }
                
    public function excluirVendedor(array $parametros): array { 
                    //Exclui um vendedor 
                    return $this->chamarApi(
                        "geral/vendedores/",
                        "ExcluirVendedor",
                        $parametros
                    );
            }
                
    public function incluirVendedor(array $parametros): array { 
                    //Inclui um vendedor 
                    return $this->chamarApi(
                        "geral/vendedores/",
                        "IncluirVendedor",
                        $parametros
                    );
            }
                
    public function listarVendedores(array $parametros): array { 
                    //Listagem de Vendedores 
                    return $this->chamarApi(
                        "geral/vendedores/",
                        "ListarVendedores",
                        $parametros
                    );
            }
                
    public function upsertVendedor(array $parametros): array { 
                    //Inclui / Altera um vendedor 
                    return $this->chamarApi(
                        "geral/vendedores/",
                        "UpsertVendedor",
                        $parametros
                    );
            }
                
    public function consultarTipoTarefa(array $parametros): array { 
                    //Consulta tipo de tarefa 
                    return $this->chamarApi(
                        "crm/tipostarefa/",
                        "ConsultarTipoTarefa",
                        $parametros
                    );
            }
                
    public function excluirTipoTarefa(array $parametros): array { 
                    //Excluir tipo de tarefa 
                    return $this->chamarApi(
                        "crm/tipostarefa/",
                        "ExcluirTipoTarefa",
                        $parametros
                    );
            }
                
    public function listarTiposTarefa(array $parametros): array { 
                    //Lista tipos de tarefa 
                    return $this->chamarApi(
                        "crm/tipostarefa/",
                        "ListarTiposTarefa",
                        $parametros
                    );
            }
                
    public function alterarContaCorrente(array $parametros): array { 
                    //Altera a Conta Corrente 
                    return $this->chamarApi(
                        "geral/contacorrente/",
                        "AlterarContaCorrente",
                        $parametros
                    );
            }
                
    public function consultarContaCorrente(array $parametros): array { 
                    //Realiza a consulta de uma conta corrente 
                    return $this->chamarApi(
                        "geral/contacorrente/",
                        "ConsultarContaCorrente",
                        $parametros
                    );
            }
                
    public function excluirContaCorrente(array $parametros): array { 
                    //Excluir a Conta Corrente 
                    return $this->chamarApi(
                        "geral/contacorrente/",
                        "ExcluirContaCorrente",
                        $parametros
                    );
            }
                
    public function incluirContaCorrente(array $parametros): array { 
                    //Inclui uma conta corrente 
                    return $this->chamarApi(
                        "geral/contacorrente/",
                        "IncluirContaCorrente",
                        $parametros
                    );
            }
                
    public function listarContasCorrentes(array $parametros): array { 
                    //Listar Contas Correntes 
                    return $this->chamarApi(
                        "geral/contacorrente/",
                        "ListarContasCorrentes",
                        $parametros
                    );
            }
                
    public function listarResumoContasCorrentes(array $parametros): array { 
                    //Listar resumida de Contas correntes. 
                    return $this->chamarApi(
                        "geral/contacorrente/",
                        "ListarResumoContasCorrentes",
                        $parametros
                    );
            }
                
    public function pesquisarContaCorrente(array $parametros): array { 
                    //DEPRECATED 
                    return $this->chamarApi(
                        "geral/contacorrente/",
                        "PesquisarContaCorrente",
                        $parametros
                    );
            }
                
    public function upsertContaCorrente(array $parametros): array { 
                    //Upsert da Conta Corrente 
                    return $this->chamarApi(
                        "geral/contacorrente/",
                        "UpsertContaCorrente",
                        $parametros
                    );
            }
                
    public function upsertContaCorrentePorLote(array $parametros): array { 
                    //Upsert por lote de Conta Corrente 
                    return $this->chamarApi(
                        "geral/contacorrente/",
                        "UpsertContaCorrentePorLote",
                        $parametros
                    );
            }
                
    public function alterarLancCC(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/contacorrentelancamentos/",
                        "AlterarLancCC",
                        $parametros
                    );
            }
                
    public function consultaLancCC(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/contacorrentelancamentos/",
                        "ConsultaLancCC",
                        $parametros
                    );
            }
                
    public function excluirLancCC(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/contacorrentelancamentos/",
                        "ExcluirLancCC",
                        $parametros
                    );
            }
                
    public function incluirLancCC(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/contacorrentelancamentos/",
                        "IncluirLancCC",
                        $parametros
                    );
            }
                
    public function listarLancCC(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/contacorrentelancamentos/",
                        "ListarLancCC",
                        $parametros
                    );
            }
                
    public function alterarContaPagar(array $parametros): array { 
                    //Altera uma conta a pagar 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "AlterarContaPagar",
                        $parametros
                    );
            }
                
    public function cancelarPagamento(array $parametros): array { 
                    //Cancela um pagamento realizado no Contas a Pagar 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "CancelarPagamento",
                        $parametros
                    );
            }
                
    public function consultarContaPagar(array $parametros): array { 
                    //Consulta uma conta a pagar 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "ConsultarContaPagar",
                        $parametros
                    );
            }
                
    public function excluirContaPagar(array $parametros): array { 
                    //Exclui uma conta a pagar 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "ExcluirContaPagar",
                        $parametros
                    );
            }
                
    public function incluirContaPagar(array $parametros): array { 
                    //Inclui uma conta a Pagar. 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "IncluirContaPagar",
                        $parametros
                    );
            }
                
    public function incluirContaPagarPorLote(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "IncluirContaPagarPorLote",
                        $parametros
                    );
            }
                
    public function lancarPagamento(array $parametros): array { 
                    //Efetua a baixa de um pagamento do contas a pagar. 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "LancarPagamento",
                        $parametros
                    );
            }
                
    public function listarContasPagar(array $parametros): array { 
                    //Listar as Contas a Pagar 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "ListarContasPagar",
                        $parametros
                    );
            }
                
    public function upsertContaPagar(array $parametros): array { 
                    //Upsert do Contas a Pagar 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "UpsertContaPagar",
                        $parametros
                    );
            }
                
    public function upsertContaPagarPorLote(array $parametros): array { 
                    //Efetua o UPSERT do Contas a Pagar por Lote 
                    return $this->chamarApi(
                        "financas/contapagar/",
                        "UpsertContaPagarPorLote",
                        $parametros
                    );
            }
                
    public function alterarContaReceber(array $parametros): array { 
                    //Altera um conta a receber 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "AlterarContaReceber",
                        $parametros
                    );
            }
                
    public function cancelarContaReceber(array $parametros): array { 
                    //Cancelamento do boleto gerado de uma conta a receber 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "CancelarContaReceber",
                        $parametros
                    );
            }
                
    public function cancelarRecebimento(array $parametros): array { 
                    //Efetua o cancelamento de um recebimento de Contas a Receber. 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "CancelarRecebimento",
                        $parametros
                    );
            }
                
    public function conciliarRecebimento(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "ConciliarRecebimento",
                        $parametros
                    );
            }
                
    public function consultarContaReceber(array $parametros): array { 
                    //Consulta uma Conta a Receber 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "ConsultarContaReceber",
                        $parametros
                    );
            }
                
    public function desconciliarRecebimento(array $parametros): array { 
                    //Desconciliar o Recebimento 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "DesconciliarRecebimento",
                        $parametros
                    );
            }
                
    public function excluirContaReceber(array $parametros): array { 
                    //Exclui uma conta a receber 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "ExcluirContaReceber",
                        $parametros
                    );
            }
                
    public function incluirContaReceber(array $parametros): array { 
                    //Inclui uma conta a Receber 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "IncluirContaReceber",
                        $parametros
                    );
            }
                
    public function incluirContaReceberPorLote(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "IncluirContaReceberPorLote",
                        $parametros
                    );
            }
                
    public function lancarRecebimento(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "LancarRecebimento",
                        $parametros
                    );
            }
                
    public function listarContasReceber(array $parametros): array { 
                    //Lista as contas a receber cadastradas. 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "ListarContasReceber",
                        $parametros
                    );
            }
                
    public function upsertContaReceber(array $parametros): array { 
                    //Executa o Upsert do Contas a receber 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "UpsertContaReceber",
                        $parametros
                    );
            }
                
    public function upsertContaReceberPorLote(array $parametros): array { 
                    //Efetua o UPSERT do Contas a Receber por Lote. 
                    return $this->chamarApi(
                        "financas/contareceber/",
                        "UpsertContaReceberPorLote",
                        $parametros
                    );
            }
                
    public function cancelarBoleto(array $parametros): array { 
                    //Cancela o Boleto. 
                    return $this->chamarApi(
                        "financas/contareceberboleto/",
                        "CancelarBoleto",
                        $parametros
                    );
            }
                
    public function gerarBoleto(array $parametros): array { 
                    //Gera um Boleto referente a um Contas a Receber. 
                    return $this->chamarApi(
                        "financas/contareceberboleto/",
                        "GerarBoleto",
                        $parametros
                    );
            }
                
    public function obterBoleto(array $parametros): array { 
                    //Disponibiliza o link de Download do Boleto. 
                    return $this->chamarApi(
                        "financas/contareceberboleto/",
                        "ObterBoleto",
                        $parametros
                    );
            }
                
    public function prorrogarBoleto(array $parametros): array { 
                    //Prorroga o vencimento do Boleto. 
                    return $this->chamarApi(
                        "financas/contareceberboleto/",
                        "ProrrogarBoleto",
                        $parametros
                    );
            }
                
    public function cancelarPix(array $parametros): array { 
                    //Efetua o cancelamento de um PIX 
                    return $this->chamarApi(
                        "financas/pix/",
                        "CancelarPix",
                        $parametros
                    );
            }
                
    public function gerarPix(array $parametros): array { 
                    //Gera o QrCode de um PIX. 
                    return $this->chamarApi(
                        "financas/pix/",
                        "GerarPix",
                        $parametros
                    );
            }
                
    public function gerarQrCodePix(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/pix/",
                        "GerarQrCodePix",
                        $parametros
                    );
            }
                
    public function listarPix(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/pix/",
                        "ListarPix",
                        $parametros
                    );
            }
                
    public function listarStatusPix(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/pix/",
                        "ListarStatusPix",
                        $parametros
                    );
            }
                
    public function obterPix(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/pix/",
                        "ObterPix",
                        $parametros
                    );
            }
                
    public function obterStatusPix(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/pix/",
                        "ObterStatusPix",
                        $parametros
                    );
            }
                
    public function listarExtrato(array $parametros): array { 
                    //Listagem do Extrato 
                    return $this->chamarApi(
                        "financas/extrato/",
                        "ListarExtrato",
                        $parametros
                    );
            }
                
    public function listarOrcamentos(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/caixa/",
                        "ListarOrcamentos",
                        $parametros
                    );
            }
                
    public function obterURLBoleto(array $parametros): array { 
                    //DEPRECATED 
                    return $this->chamarApi(
                        "financas/pesquisartitulos/",
                        "ObterURLBoleto",
                        $parametros
                    );
            }
                
    public function pesquisarExcluidos(array $parametros): array { 
                    //DEPRECATED 
                    return $this->chamarApi(
                        "financas/pesquisartitulos/",
                        "PesquisarExcluidos",
                        $parametros
                    );
            }
                
    public function pesquisarLancamentos(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "financas/pesquisartitulos/",
                        "PesquisarLancamentos",
                        $parametros
                    );
            }
                
    public function listarMovimentos(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "estoque/movestoque/",
                        "ListarMovimentos",
                        $parametros
                    );
            }
                
    public function obterResumoContador(array $parametros): array { 
                    //Obtem o resumo do painel do contador. 
                    return $this->chamarApi(
                        "contador/resumo/",
                        "ObterResumoContador",
                        $parametros
                    );
            }
                
    public function consultarBanco(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/bancos/",
                        "ConsultarBanco",
                        $parametros
                    );
            }
                
    public function listarBancos(array $parametros): array { 
                    //Exibe uma lista com os banco cadastrados. 
                    return $this->chamarApi(
                        "geral/bancos/",
                        "ListarBancos",
                        $parametros
                    );
            }
                
    public function consultarTipoDocumento(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/tiposdoc/",
                        "ConsultarTipoDocumento",
                        $parametros
                    );
            }
                
    public function pesquisarTipoDocumento(array $parametros): array { 
                    //Pesquisa o tipo de documento 
                    return $this->chamarApi(
                        "geral/tiposdoc/",
                        "PesquisarTipoDocumento",
                        $parametros
                    );
            }
                
    public function listarTiposCC(array $parametros): array { 
                    //Listar os tipos de contas correntes. 
                    return $this->chamarApi(
                        "geral/tipocc/",
                        "ListarTiposCC",
                        $parametros
                    );
            }
                
    public function listarCadastroDRE(array $parametros): array { 
                    //Lista as contas do DRE 
                    return $this->chamarApi(
                        "geral/dre/",
                        "ListarCadastroDRE",
                        $parametros
                    );
            }
                
    public function consultarFinalTransf(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/finaltransf/",
                        "ConsultarFinalTransf",
                        $parametros
                    );
            }
                
    public function listarFinalTransf(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/finaltransf/",
                        "ListarFinalTransf",
                        $parametros
                    );
            }
                
    public function listarOrigem(array $parametros): array { 
                    //Lista Origem de pedidos. 
                    return $this->chamarApi(
                        "geral/origempedido/",
                        "ListarOrigem",
                        $parametros
                    );
            }
                
    public function listarBandeiras(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/bandeiracartao/",
                        "ListarBandeiras",
                        $parametros
                    );
            }
                
    public function alterarProduto(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "AlterarProduto",
                        $parametros
                    );
            }
                
    public function associarCodIntProduto(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "AssociarCodIntProduto",
                        $parametros
                    );
            }
                
    public function consultarProduto(array $parametros): array { 
                    //Consulta um produto. 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "ConsultarProduto",
                        $parametros
                    );
            }
                
    public function excluirProduto(array $parametros): array { 
                    //Exclui um produto 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "ExcluirProduto",
                        $parametros
                    );
            }
                
    public function incluirProduto(array $parametros): array { 
                    //Incluir um produto. 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "IncluirProduto",
                        $parametros
                    );
            }
                
    public function incluirProdutosPorLote(array $parametros): array { 
                    //DEPRECATED 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "IncluirProdutosPorLote",
                        $parametros
                    );
            }
                
    public function listarProdutos(array $parametros): array { 
                    //Lista completa do cadastro de produtos 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "ListarProdutos",
                        $parametros
                    );
            }
                
    public function listarProdutosResumido(array $parametros): array { 
                    //Lista os produtos cadastrados 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "ListarProdutosResumido",
                        $parametros
                    );
            }
                
    public function upsertProduto(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "UpsertProduto",
                        $parametros
                    );
            }
                
    public function upsertProdutosPorLote(array $parametros): array { 
                    //DEPRECATED 
                    return $this->chamarApi(
                        "geral/produtos/",
                        "UpsertProdutosPorLote",
                        $parametros
                    );
            }
                
    public function alterarCaractProduto(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/prodcaract/",
                        "AlterarCaractProduto",
                        $parametros
                    );
            }
                
    public function consultarCaractProduto(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/prodcaract/",
                        "ConsultarCaractProduto",
                        $parametros
                    );
            }
                
    public function excluirCaractProduto(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/prodcaract/",
                        "ExcluirCaractProduto",
                        $parametros
                    );
            }
                
    public function incluirCaractProduto(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/prodcaract/",
                        "IncluirCaractProduto",
                        $parametros
                    );
            }
                
    public function listarCaractProduto(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/prodcaract/",
                        "ListarCaractProduto",
                        $parametros
                    );
            }
                
    public function alterarEstrutura(array $parametros): array { 
                    //Alterar a estrutura de um produto. 
                    return $this->chamarApi(
                        "geral/malha/",
                        "AlterarEstrutura",
                        $parametros
                    );
            }
                
    public function consultarEstrutura(array $parametros): array { 
                    //Consulta a estrutura do produto. 
                    return $this->chamarApi(
                        "geral/malha/",
                        "ConsultarEstrutura",
                        $parametros
                    );
            }
                
    public function excluirEstrutura(array $parametros): array { 
                    //Excluir item da estrutura de um produto. 
                    return $this->chamarApi(
                        "geral/malha/",
                        "ExcluirEstrutura",
                        $parametros
                    );
            }
                
    public function incluirEstrutura(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/malha/",
                        "IncluirEstrutura",
                        $parametros
                    );
            }
                
    public function listarEstruturas(array $parametros): array { 
                    //Lista as estruturas de produtos. 
                    return $this->chamarApi(
                        "geral/malha/",
                        "ListarEstruturas",
                        $parametros
                    );
            }
                
    public function alterarComponentesKit(array $parametros): array { 
                    //Inclui/Altera/Exclui os componentes do KIT. 
                    return $this->chamarApi(
                        "geral/produtoskit/",
                        "AlterarComponentesKit",
                        $parametros
                    );
            }
                
    public function alterarReq(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/requisicaocompra/",
                        "AlterarReq",
                        $parametros
                    );
            }
                
    public function consultarReq(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/requisicaocompra/",
                        "ConsultarReq",
                        $parametros
                    );
            }
                
    public function excluirReq(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/requisicaocompra/",
                        "ExcluirReq",
                        $parametros
                    );
            }
                
    public function incluirReq(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/requisicaocompra/",
                        "IncluirReq",
                        $parametros
                    );
            }
                
    public function pesquisarReq(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/requisicaocompra/",
                        "PesquisarReq",
                        $parametros
                    );
            }
                
    public function upsertReq(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/requisicaocompra/",
                        "UpsertReq",
                        $parametros
                    );
            }
                
    public function alteraPedCompra(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/pedidocompra/",
                        "AlteraPedCompra",
                        $parametros
                    );
            }
                
    public function consultarPedCompra(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/pedidocompra/",
                        "ConsultarPedCompra",
                        $parametros
                    );
            }
                
    public function excluirPedCompra(array $parametros): array { 
                    //Excluir um Pedido de Compra 
                    return $this->chamarApi(
                        "produtos/pedidocompra/",
                        "ExcluirPedCompra",
                        $parametros
                    );
            }
                
    public function incluirPedCompra(array $parametros): array { 
                    //Incluir um Pedido de Compra 
                    return $this->chamarApi(
                        "produtos/pedidocompra/",
                        "IncluirPedCompra",
                        $parametros
                    );
            }
                
    public function pesquisarPedCompra(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/pedidocompra/",
                        "PesquisarPedCompra",
                        $parametros
                    );
            }
                
    public function upsertPedCompra(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/pedidocompra/",
                        "UpsertPedCompra",
                        $parametros
                    );
            }
                
    public function alterarOrdemProducao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/op/",
                        "AlterarOrdemProducao",
                        $parametros
                    );
            }
                
    public function concluirOrdemProducao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/op/",
                        "ConcluirOrdemProducao",
                        $parametros
                    );
            }
                
    public function consultarOrdemProducao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/op/",
                        "ConsultarOrdemProducao",
                        $parametros
                    );
            }
                
    public function excluirOrdemProducao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/op/",
                        "ExcluirOrdemProducao",
                        $parametros
                    );
            }
                
    public function incluirOrdemProducao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/op/",
                        "IncluirOrdemProducao",
                        $parametros
                    );
            }
                
    public function listarOrdemProducao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/op/",
                        "ListarOrdemProducao",
                        $parametros
                    );
            }
                
    public function reverterOrdemProducao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/op/",
                        "ReverterOrdemProducao",
                        $parametros
                    );
            }
                
    public function upsertOrdemProducao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/op/",
                        "UpsertOrdemProducao",
                        $parametros
                    );
            }
                
    public function alterarNotaEnt(array $parametros): array { 
                    //Alterar nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentrada/",
                        "AlterarNotaEnt",
                        $parametros
                    );
            }
                
    public function consultarNotaEnt(array $parametros): array { 
                    //Consultar nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentrada/",
                        "ConsultarNotaEnt",
                        $parametros
                    );
            }
                
    public function excluirNotaEnt(array $parametros): array { 
                    //Excluir nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentrada/",
                        "ExcluirNotaEnt",
                        $parametros
                    );
            }
                
    public function incluirNotaEnt(array $parametros): array { 
                    //Incluir nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentrada/",
                        "IncluirNotaEnt",
                        $parametros
                    );
            }
                
    public function listarNotaEnt(array $parametros): array { 
                    //Listagem de nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentrada/",
                        "ListarNotaEnt",
                        $parametros
                    );
            }
                
    public function statusNotaEnt(array $parametros): array { 
                    //Status de nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentrada/",
                        "StatusNotaEnt",
                        $parametros
                    );
            }
                
    public function cancelarNotaEnt(array $parametros): array { 
                    //Cancelar nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentradafat/",
                        "CancelarNotaEnt",
                        $parametros
                    );
            }
                
    public function concluirNotaEnt(array $parametros): array { 
                    //Concluir nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentradafat/",
                        "ConcluirNotaEnt",
                        $parametros
                    );
            }
                
    public function conferirNotaEnt(array $parametros): array { 
                    //Conferir nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentradafat/",
                        "ConferirNotaEnt",
                        $parametros
                    );
            }
                
    public function duplicarNotaEnt(array $parametros): array { 
                    //Duplicar nota de entrada 
                    return $this->chamarApi(
                        "produtos/notaentradafat/",
                        "DuplicarNotaEnt",
                        $parametros
                    );
            }
                
    public function alterarEtapaRecebimento(array $parametros): array { 
                    //Alterar etapa recebimento NFe 
                    return $this->chamarApi(
                        "produtos/recebimentonfe/",
                        "AlterarEtapaRecebimento",
                        $parametros
                    );
            }
                
    public function alterarRecebimento(array $parametros): array { 
                    //Alterar recebimento de NFe 
                    return $this->chamarApi(
                        "produtos/recebimentonfe/",
                        "AlterarRecebimento",
                        $parametros
                    );
            }
                
    public function concluirRecebimento(array $parametros): array { 
                    //Concluir recebimento de NFe 
                    return $this->chamarApi(
                        "produtos/recebimentonfe/",
                        "ConcluirRecebimento",
                        $parametros
                    );
            }
                
    public function consultarRecebimento(array $parametros): array { 
                    //Consultar recebimento de NFe 
                    return $this->chamarApi(
                        "produtos/recebimentonfe/",
                        "ConsultarRecebimento",
                        $parametros
                    );
            }
                
    public function listarRecebimentos(array $parametros): array { 
                    //Listar recebimento de NFe 
                    return $this->chamarApi(
                        "produtos/recebimentonfe/",
                        "ListarRecebimentos",
                        $parametros
                    );
            }
                
    public function reverterRecebimento(array $parametros): array { 
                    //Reverter recebimento NFe 
                    return $this->chamarApi(
                        "produtos/recebimentonfe/",
                        "ReverterRecebimento",
                        $parametros
                    );
            }
                
    public function alterarFamilia(array $parametros): array { 
                    //Altera uma familia de produto 
                    return $this->chamarApi(
                        "geral/familias/",
                        "AlterarFamilia",
                        $parametros
                    );
            }
                
    public function consultarFamilia(array $parametros): array { 
                    //Consulta uma familia de produto 
                    return $this->chamarApi(
                        "geral/familias/",
                        "ConsultarFamilia",
                        $parametros
                    );
            }
                
    public function excluirFamilia(array $parametros): array { 
                    //Exclui uma familia de produto 
                    return $this->chamarApi(
                        "geral/familias/",
                        "ExcluirFamilia",
                        $parametros
                    );
            }
                
    public function incluirFamilia(array $parametros): array { 
                    //Inclui uma familia de produto 
                    return $this->chamarApi(
                        "geral/familias/",
                        "IncluirFamilia",
                        $parametros
                    );
            }
                
    public function pesquisarFamilias(array $parametros): array { 
                    //Listagem de familias cadastradas 
                    return $this->chamarApi(
                        "geral/familias/",
                        "PesquisarFamilias",
                        $parametros
                    );
            }
                
    public function upsertFamilia(array $parametros): array { 
                    //Inclui / Altera uma familia de produto 
                    return $this->chamarApi(
                        "geral/familias/",
                        "UpsertFamilia",
                        $parametros
                    );
            }
                
    public function listarUnidades(array $parametros): array { 
                    //Lista as unidades de medidas 
                    return $this->chamarApi(
                        "geral/unidade/",
                        "ListarUnidades",
                        $parametros
                    );
            }
                
    public function listarCompradores(array $parametros): array { 
                    //Lista os compradores cadastrados. 
                    return $this->chamarApi(
                        "estoque/comprador/",
                        "ListarCompradores",
                        $parametros
                    );
            }
                
    public function listarProdutoFornecedor(array $parametros): array { 
                    //Listar os produtos por fornecedores. 
                    return $this->chamarApi(
                        "estoque/produtofornecedor/",
                        "ListarProdutoFornecedor",
                        $parametros
                    );
            }
                
    public function listarFormasPagVendas(array $parametros): array { 
                    //Lista as formas de pagmento de vendas. 
                    return $this->chamarApi(
                        "produtos/formaspagvendas/",
                        "ListarFormasPagVendas",
                        $parametros
                    );
            }
                
    public function consultarNCM(array $parametros): array { 
                    //Consulta um NCM 
                    return $this->chamarApi(
                        "produtos/ncm/",
                        "ConsultarNCM",
                        $parametros
                    );
            }
                
    public function listarNCM(array $parametros): array { 
                    //Lista os NCMs cadastrados. 
                    return $this->chamarApi(
                        "produtos/ncm/",
                        "ListarNCM",
                        $parametros
                    );
            }
                
    public function listarCenarios(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/cenarios/",
                        "ListarCenarios",
                        $parametros
                    );
            }
                
    public function listarImpostosCenario(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/cenarios/",
                        "ListarImpostosCenario",
                        $parametros
                    );
            }
                
    public function listarCFOP(array $parametros): array { 
                    //Listar as CFOPs 
                    return $this->chamarApi(
                        "produtos/cfop/",
                        "ListarCFOP",
                        $parametros
                    );
            }
                
    public function listarCST(array $parametros): array { 
                    //Listar os CSTs do ICMS 
                    return $this->chamarApi(
                        "produtos/icmscst/",
                        "ListarCST",
                        $parametros
                    );
            }
                
    public function listarCSOSN(array $parametros): array { 
                    //Listar os CSOSN do ICMS. 
                    return $this->chamarApi(
                        "produtos/icmscsosn/",
                        "ListarCSOSN",
                        $parametros
                    );
            }
                
    public function listarOrigMerc(array $parametros): array { 
                    //Listar a origem da mercadoria do ICMS. 
                    return $this->chamarApi(
                        "produtos/icmsorigem/",
                        "ListarOrigMerc",
                        $parametros
                    );
            }
                
    public function listarCstPis(array $parametros): array { 
                    //Listar o CST do PIS. 
                    return $this->chamarApi(
                        "produtos/piscst/",
                        "ListarCstPis",
                        $parametros
                    );
            }
                
    public function listarCstCofins(array $parametros): array { 
                    //Listar CST do COFINS. 
                    return $this->chamarApi(
                        "produtos/cofinscst/",
                        "ListarCstCofins",
                        $parametros
                    );
            }
                
    public function listarCstIpi(array $parametros): array { 
                    //Listar CST do IPI. 
                    return $this->chamarApi(
                        "produtos/ipicst/",
                        "ListarCstIpi",
                        $parametros
                    );
            }
                
    public function listarEnqIpi(array $parametros): array { 
                    //Listar Enquadramento do IPI. 
                    return $this->chamarApi(
                        "produtos/ipienq/",
                        "ListarEnqIpi",
                        $parametros
                    );
            }
                
    public function listarTpCalc(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tpcalc/",
                        "ListarTpCalc",
                        $parametros
                    );
            }
                
    public function listarCEST(array $parametros): array { 
                    //Listar CEST. 
                    return $this->chamarApi(
                        "produtos/cest/",
                        "ListarCEST",
                        $parametros
                    );
            }
                
    public function alterarEstoqueMinimo(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "estoque/ajuste/",
                        "AlterarEstoqueMinimo",
                        $parametros
                    );
            }
                
    public function excluirAjusteEstoque(array $parametros): array { 
                    //Excluir um Movimento de Ajuste de Estoque 
                    return $this->chamarApi(
                        "estoque/ajuste/",
                        "ExcluirAjusteEstoque",
                        $parametros
                    );
            }
                
    public function incluirAjusteEstoque(array $parametros): array { 
                    //Incluir um Ajuste de Estoque 
                    return $this->chamarApi(
                        "estoque/ajuste/",
                        "IncluirAjusteEstoque",
                        $parametros
                    );
            }
                
    public function listarAjusteEstoque(array $parametros): array { 
                    //Listar os ajuste de estoque. 
                    return $this->chamarApi(
                        "estoque/ajuste/",
                        "ListarAjusteEstoque",
                        $parametros
                    );
            }
                
    public function listarMovimentoEstoque(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "estoque/consulta/",
                        "ListarMovimentoEstoque",
                        $parametros
                    );
            }
                
    public function listarPosEstoque(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "estoque/consulta/",
                        "ListarPosEstoque",
                        $parametros
                    );
            }
                
    public function listarSaldoPendente(array $parametros): array { 
                    //Lista o saldo pendente de estoque. 
                    return $this->chamarApi(
                        "estoque/consulta/",
                        "ListarSaldoPendente",
                        $parametros
                    );
            }
                
    public function movimentoEstoque(array $parametros): array { 
                    //Consulta do Movimento de Estoque 
                    return $this->chamarApi(
                        "estoque/consulta/",
                        "MovimentoEstoque",
                        $parametros
                    );
            }
                
    public function posicaoEstoque(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "estoque/consulta/",
                        "PosicaoEstoque",
                        $parametros
                    );
            }
                
    public function consultarPrevisao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "estoque/movestoque/",
                        "ConsultarPrevisao",
                        $parametros
                    );
            }
                
    public function alterarLocalEstoque(array $parametros): array { 
                    //Alterar local de Estoque 
                    return $this->chamarApi(
                        "estoque/local/",
                        "AlterarLocalEstoque",
                        $parametros
                    );
            }
                
    public function incluirLocalEstoque(array $parametros): array { 
                    //Adiciona um local de estoque 
                    return $this->chamarApi(
                        "estoque/local/",
                        "IncluirLocalEstoque",
                        $parametros
                    );
            }
                
    public function listarLocaisEstoque(array $parametros): array { 
                    //Lista os Locais de Estoque encontrados. 
                    return $this->chamarApi(
                        "estoque/local/",
                        "ListarLocaisEstoque",
                        $parametros
                    );
            }
                
    public function obterEstoqueProduto(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "estoque/resumo/",
                        "ObterEstoqueProduto",
                        $parametros
                    );
            }
                
    public function adicionarPedido(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/pedidovenda/",
                        "AdicionarPedido",
                        $parametros
                    );
            }
                
    public function alterarItemPedido(array $parametros): array { 
                    //Altera um item no pedido de venda. 
                    return $this->chamarApi(
                        "produtos/pedidovenda/",
                        "AlterarItemPedido",
                        $parametros
                    );
            }
                
    public function excluirItemPedido(array $parametros): array { 
                    //Exclui um item no pedido de venda. 
                    return $this->chamarApi(
                        "produtos/pedidovenda/",
                        "ExcluirItemPedido",
                        $parametros
                    );
            }
                
    public function excluirItensPedido(array $parametros): array { 
                    //Exclui todos os itens do pedido de venda. 
                    return $this->chamarApi(
                        "produtos/pedidovenda/",
                        "ExcluirItensPedido",
                        $parametros
                    );
            }
                
    public function incluirItemPedido(array $parametros): array { 
                    //Inclui um item no pedido de venda. 
                    return $this->chamarApi(
                        "produtos/pedidovenda/",
                        "IncluirItemPedido",
                        $parametros
                    );
            }
                
    public function totalizarPedido(array $parametros): array { 
                    //Recalcula os totais do pedido de venda. 
                    return $this->chamarApi(
                        "produtos/pedidovenda/",
                        "TotalizarPedido",
                        $parametros
                    );
            }
                
    public function alterarPedFaturado(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/pedido/",
                        "AlterarPedFaturado",
                        $parametros
                    );
            }
                
    public function alterarPedidoVenda(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/pedido/",
                        "AlterarPedidoVenda",
                        $parametros
                    );
            }
                
    public function consultarPedido(array $parametros): array { 
                    //Consulta de Pedido de Venda de Produto 
                    return $this->chamarApi(
                        "produtos/pedido/",
                        "ConsultarPedido",
                        $parametros
                    );
            }
                
    public function excluirPedido(array $parametros): array { 
                    //Excluir pedido de venda de produto 
                    return $this->chamarApi(
                        "produtos/pedido/",
                        "ExcluirPedido",
                        $parametros
                    );
            }
                
    public function incluirPedido(array $parametros): array { 
                    //Inclui um pedido de venda de produto 
                    return $this->chamarApi(
                        "produtos/pedido/",
                        "IncluirPedido",
                        $parametros
                    );
            }
                
    public function listarPedidos(array $parametros): array { 
                    //Listar os pedidos de venda de produto 
                    return $this->chamarApi(
                        "produtos/pedido/",
                        "ListarPedidos",
                        $parametros
                    );
            }
                
    public function simularImpostos(array $parametros): array { 
                    //Simula os impostos de um pedido de venda. 
                    return $this->chamarApi(
                        "produtos/pedido/",
                        "SimularImpostos",
                        $parametros
                    );
            }
                
    public function statusPedido(array $parametros): array { 
                    //Consulta do Status do Pedido 
                    return $this->chamarApi(
                        "produtos/pedido/",
                        "StatusPedido",
                        $parametros
                    );
            }
                
    public function trocarEtapaPedido(array $parametros): array { 
                    //Troca etapa do pedido. 
                    return $this->chamarApi(
                        "produtos/pedido/",
                        "TrocarEtapaPedido",
                        $parametros
                    );
            }
                
    public function associarCodIntPedidoVenda(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/pedidovendafat/",
                        "AssociarCodIntPedidoVenda",
                        $parametros
                    );
            }
                
    public function cancelarPedidoVenda(array $parametros): array { 
                    //Cancela um pedido de venda de produto. 
                    return $this->chamarApi(
                        "produtos/pedidovendafat/",
                        "CancelarPedidoVenda",
                        $parametros
                    );
            }
                
    public function duplicarPedidoVenda(array $parametros): array { 
                    //Duplica um pedido de venda de produto. 
                    return $this->chamarApi(
                        "produtos/pedidovendafat/",
                        "DuplicarPedidoVenda",
                        $parametros
                    );
            }
                
    public function faturarPedidoVenda(array $parametros): array { 
                    //Fatura um pedido de venda de produto. 
                    return $this->chamarApi(
                        "produtos/pedidovendafat/",
                        "FaturarPedidoVenda",
                        $parametros
                    );
            }
                
    public function obterPedidosVenda(array $parametros): array { 
                    //Retorna a lista de pedidos de venda a serem faturados. 
                    return $this->chamarApi(
                        "produtos/pedidovendafat/",
                        "ObterPedidosVenda",
                        $parametros
                    );
            }
                
    public function validarPedidoVenda(array $parametros): array { 
                    //Valida um pedido de venda de produto para faturamento. 
                    return $this->chamarApi(
                        "produtos/pedidovendafat/",
                        "ValidarPedidoVenda",
                        $parametros
                    );
            }
                
    public function listarEtapasPedido(array $parametros): array { 
                    //Lista as etapas do Pedido de Venda de Produtos. 
                    return $this->chamarApi(
                        "produtos/pedidoetapas/",
                        "ListarEtapasPedido",
                        $parametros
                    );
            }
                
    public function averbacaoCTe(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "AverbacaoCTe",
                        $parametros
                    );
            }
                
    public function cancelarCTe(array $parametros): array { 
                    //Cancela um CT-e. 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "CancelarCTe",
                        $parametros
                    );
            }
                
    public function cartaCorrecaoCTe(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "CartaCorrecaoCTe",
                        $parametros
                    );
            }
                
    public function excluirCTe(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "ExcluirCTe",
                        $parametros
                    );
            }
                
    public function excluirFaturaCTe(array $parametros): array { 
                    //Exclui uma fatura de um grupo de CT-es. 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "ExcluirFaturaCTe",
                        $parametros
                    );
            }
                
    public function faturarCTe(array $parametros): array { 
                    //Gera uma fatura para um grupo de CT-es. 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "FaturarCTe",
                        $parametros
                    );
            }
                
    public function faturarLoteCTe(array $parametros): array { 
                    //Gera uma fatura por lote para um grupo de CT-es. 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "FaturarLoteCTe",
                        $parametros
                    );
            }
                
    public function importarCTe(array $parametros): array { 
                    //Importar o XML de um CT-e. 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "ImportarCTe",
                        $parametros
                    );
            }
                
    public function listarNFeTransp(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "ListarNFeTransp",
                        $parametros
                    );
            }
                
    public function statusFatura(array $parametros): array { 
                    //Retorna o Status da Fatura inclusa. 
                    return $this->chamarApi(
                        "produtos/cte/",
                        "StatusFatura",
                        $parametros
                    );
            }
                
    public function alterarRemessa(array $parametros): array { 
                    //Altera uma remessa 
                    return $this->chamarApi(
                        "produtos/remessa/",
                        "AlterarRemessa",
                        $parametros
                    );
            }
                
    public function consultarRemessa(array $parametros): array { 
                    //Consulta uma remessa. 
                    return $this->chamarApi(
                        "produtos/remessa/",
                        "ConsultarRemessa",
                        $parametros
                    );
            }
                
    public function incluirRemessa(array $parametros): array { 
                    //Inclui uma nova remessa 
                    return $this->chamarApi(
                        "produtos/remessa/",
                        "IncluirRemessa",
                        $parametros
                    );
            }
                
    public function listarRemessas(array $parametros): array { 
                    //Lista as remessas cadastradas. 
                    return $this->chamarApi(
                        "produtos/remessa/",
                        "ListarRemessas",
                        $parametros
                    );
            }
                
    public function statusRemessa(array $parametros): array { 
                    //Retorna o status da remessa 
                    return $this->chamarApi(
                        "produtos/remessa/",
                        "StatusRemessa",
                        $parametros
                    );
            }
                
    public function cancelarRemessa(array $parametros): array { 
                    //Cancelar remessa de produto 
                    return $this->chamarApi(
                        "produtos/remessafat/",
                        "CancelarRemessa",
                        $parametros
                    );
            }
                
    public function concluirRemessa(array $parametros): array { 
                    //Concluir remessa de produto 
                    return $this->chamarApi(
                        "produtos/remessafat/",
                        "ConcluirRemessa",
                        $parametros
                    );
            }
                
    public function conferirRemessa(array $parametros): array { 
                    //Conferir remessa de produto 
                    return $this->chamarApi(
                        "produtos/remessafat/",
                        "ConferirRemessa",
                        $parametros
                    );
            }
                
    public function duplicarRemessa(array $parametros): array { 
                    //Duplicar remessa de produto 
                    return $this->chamarApi(
                        "produtos/remessafat/",
                        "DuplicarRemessa",
                        $parametros
                    );
            }
                
    public function obterDemonst(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osdocs/",
                        "ObterDemonst",
                        $parametros
                    );
            }
                
    public function obterNFSe(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osdocs/",
                        "ObterNFSe",
                        $parametros
                    );
            }
                
    public function obterOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osp/",
                        "ObterOS",
                        $parametros
                    );
            }
                
    public function obterRPS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osdocs/",
                        "ObterRPS",
                        $parametros
                    );
            }
                
    public function obterRecibo(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osdocs/",
                        "ObterRecibo",
                        $parametros
                    );
            }
                
    public function obterViaUnica(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osdocs/",
                        "ObterViaUnica",
                        $parametros
                    );
            }
                
    public function fecharCaixa(array $parametros): array { 
                    //Efetua o fechamento de um determinado caixa. 
                    return $this->chamarApi(
                        "produtos/cupomfiscalincluir/",
                        "FecharCaixa",
                        $parametros
                    );
            }
                
    public function incluirCfeSat(array $parametros): array { 
                    //Incluir Cupom Fiscal para SAT. 
                    return $this->chamarApi(
                        "produtos/cupomfiscalincluir/",
                        "IncluirCfeSat",
                        $parametros
                    );
            }
                
    public function incluirCupom(array $parametros): array { 
                    //Incluir Cupom Fiscal (ECF). 
                    return $this->chamarApi(
                        "produtos/cupomfiscalincluir/",
                        "IncluirCupom",
                        $parametros
                    );
            }
                
    public function incluirNfce(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/cupomfiscalincluir/",
                        "IncluirNfce",
                        $parametros
                    );
            }
                
    public function inutilizarNfce(array $parametros): array { 
                    //Inutiliza um lote de NFC-e. 
                    return $this->chamarApi(
                        "produtos/cupomfiscalincluir/",
                        "InutilizarNfce",
                        $parametros
                    );
            }
                
    public function cancelarCupom(array $parametros): array { 
                    //Cancela um cupom Fiscal 
                    return $this->chamarApi(
                        "produtos/cupomfiscal/",
                        "CancelarCupom",
                        $parametros
                    );
            }
                
    public function cancelarNFCE(array $parametros): array { 
                    //Cancelar NFC-e. 
                    return $this->chamarApi(
                        "produtos/cupomfiscal/",
                        "CancelarNFCE",
                        $parametros
                    );
            }
                
    public function cancelarSAT(array $parametros): array { 
                    //Cancelar CF-e-SAT. 
                    return $this->chamarApi(
                        "produtos/cupomfiscal/",
                        "CancelarSAT",
                        $parametros
                    );
            }
                
    public function devolverCupom(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/cupomfiscal/",
                        "DevolverCupom",
                        $parametros
                    );
            }
                
    public function excluirCupom(array $parametros): array { 
                    //Exclui um Cupom Fiscal. 
                    return $this->chamarApi(
                        "produtos/cupomfiscal/",
                        "ExcluirCupom",
                        $parametros
                    );
            }
                
    public function excluirCuponsPorNumero(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/cupomfiscal/",
                        "ExcluirCuponsPorNumero",
                        $parametros
                    );
            }
                
    public function excluirLote(array $parametros): array { 
                    //Excluir o lote 
                    return $this->chamarApi(
                        "produtos/cupomfiscal/",
                        "ExcluirLote",
                        $parametros
                    );
            }
                
    public function listarCupons(array $parametros): array { 
                    //Lista os Cupons Fiscais. 
                    return $this->chamarApi(
                        "produtos/cupomfiscal/",
                        "ListarCupons",
                        $parametros
                    );
            }
                
    public function obterProximoLote(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/cupomfiscal/",
                        "ObterProximoLote",
                        $parametros
                    );
            }
                
    public function cuponsFiscais(array $parametros): array { 
                    //Listagem dos cupons fiscais. 
                    return $this->chamarApi(
                        "produtos/cupomfiscalconsultar/",
                        "CuponsFiscais",
                        $parametros
                    );
            }
                
    public function cuponsItens(array $parametros): array { 
                    //Listagem dos itens dos cupons fiscais 
                    return $this->chamarApi(
                        "produtos/cupomfiscalconsultar/",
                        "CuponsItens",
                        $parametros
                    );
            }
                
    public function cuponsPagamentos(array $parametros): array { 
                    //Listagem dos pagamentos dos cupons fiscais 
                    return $this->chamarApi(
                        "produtos/cupomfiscalconsultar/",
                        "CuponsPagamentos",
                        $parametros
                    );
            }
                
    public function importarNFCe(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/nfce/",
                        "ImportarNFCe",
                        $parametros
                    );
            }
                
    public function importarCfeSat(array $parametros): array { 
                    //Importa o XML de um CF-e SAT. 
                    return $this->chamarApi(
                        "produtos/sat/",
                        "ImportarCfeSat",
                        $parametros
                    );
            }
                
    public function alterarPrecoItem(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "AlterarPrecoItem",
                        $parametros
                    );
            }
                
    public function alterarTabelaPreco(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "AlterarTabelaPreco",
                        $parametros
                    );
            }
                
    public function ativarTabelaPreco(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "AtivarTabelaPreco",
                        $parametros
                    );
            }
                
    public function atualizarProdutos(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "AtualizarProdutos",
                        $parametros
                    );
            }
                
    public function consultarTabelaPreco(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "ConsultarTabelaPreco",
                        $parametros
                    );
            }
                
    public function excluirTabelaPreco(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "ExcluirTabelaPreco",
                        $parametros
                    );
            }
                
    public function incluirTabelaPreco(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "IncluirTabelaPreco",
                        $parametros
                    );
            }
                
    public function listarTabelaItens(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "ListarTabelaItens",
                        $parametros
                    );
            }
                
    public function listarTabelasPreco(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "ListarTabelasPreco",
                        $parametros
                    );
            }
                
    public function suspenderTabelaPreco(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/tabelaprecos/",
                        "SuspenderTabelaPreco",
                        $parametros
                    );
            }
                
    public function alterarCaracteristica(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/caracteristicas/",
                        "AlterarCaracteristica",
                        $parametros
                    );
            }
                
    public function consultarCaracteristica(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/caracteristicas/",
                        "ConsultarCaracteristica",
                        $parametros
                    );
            }
                
    public function excluirCaracteristica(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/caracteristicas/",
                        "ExcluirCaracteristica",
                        $parametros
                    );
            }
                
    public function incluirCaracteristica(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/caracteristicas/",
                        "IncluirCaracteristica",
                        $parametros
                    );
            }
                
    public function listarCaracteristicas(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/caracteristicas/",
                        "ListarCaracteristicas",
                        $parametros
                    );
            }
                
    public function listarEtapasFaturamento(array $parametros): array { 
                    //Lista as etapas do faturamento 
                    return $this->chamarApi(
                        "produtos/etapafat/",
                        "ListarEtapasFaturamento",
                        $parametros
                    );
            }
                
    public function listarMeiosPagamento(array $parametros): array { 
                    //Listagem de meios de pagamento 
                    return $this->chamarApi(
                        "geral/meiospagamento/",
                        "ListarMeiosPagamento",
                        $parametros
                    );
            }
                
    public function listarMotivosDevol(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "geral/motivodevolucao/",
                        "ListarMotivosDevol",
                        $parametros
                    );
            }
                
    public function listarNFSEs(array $parametros): array { 
                    //Lista de NFS-es. 
                    return $this->chamarApi(
                        "servicos/nfse/",
                        "ListarNFSEs",
                        $parametros
                    );
            }
                
    public function getUrlDanfe(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/notafiscalutil/",
                        "GetUrlDanfe",
                        $parametros
                    );
            }
                
    public function getUrlLogo(array $parametros): array { 
                    //Retorna a URL do Logotipo 
                    return $this->chamarApi(
                        "produtos/notafiscalutil/",
                        "GetUrlLogo",
                        $parametros
                    );
            }
                
    public function getUrlNotaFiscal(array $parametros): array { 
                    //Retorna a URL da Nota Fiscal 
                    return $this->chamarApi(
                        "produtos/notafiscalutil/",
                        "GetUrlNotaFiscal",
                        $parametros
                    );
            }
                
    public function excluirNFe(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/nfe/",
                        "ExcluirNFe",
                        $parametros
                    );
            }
                
    public function importarCancNFe(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/nfe/",
                        "ImportarCancNFe",
                        $parametros
                    );
            }
                
    public function importarNFe(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "produtos/nfe/",
                        "ImportarNFe",
                        $parametros
                    );
            }
                
    public function listarNFe(array $parametros): array { 
                    //Lista as NFes importadas. 
                    return $this->chamarApi(
                        "produtos/nfe/",
                        "ListarNFe",
                        $parametros
                    );
            }
                
    public function alterarCadastroServico(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/servico/",
                        "AlterarCadastroServico",
                        $parametros
                    );
            }
                
    public function associarCodIntServico(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/servico/",
                        "AssociarCodIntServico",
                        $parametros
                    );
            }
                
    public function consultarCadastroServico(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/servico/",
                        "ConsultarCadastroServico",
                        $parametros
                    );
            }
                
    public function excluirCadastroServico(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/servico/",
                        "ExcluirCadastroServico",
                        $parametros
                    );
            }
                
    public function incluirCadastroServico(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/servico/",
                        "IncluirCadastroServico",
                        $parametros
                    );
            }
                
    public function listarCadastroServico(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/servico/",
                        "ListarCadastroServico",
                        $parametros
                    );
            }
                
    public function upsertCadastroServico(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/servico/",
                        "UpsertCadastroServico",
                        $parametros
                    );
            }
                
    public function alterarOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/os/",
                        "AlterarOS",
                        $parametros
                    );
            }
                
    public function consultarOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/os/",
                        "ConsultarOS",
                        $parametros
                    );
            }
                
    public function excluirOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/os/",
                        "ExcluirOS",
                        $parametros
                    );
            }
                
    public function incluirOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/os/",
                        "IncluirOS",
                        $parametros
                    );
            }
                
    public function listarOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/os/",
                        "ListarOS",
                        $parametros
                    );
            }
                
    public function statusOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/os/",
                        "StatusOS",
                        $parametros
                    );
            }
                
    public function trocarEtapaOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/os/",
                        "TrocarEtapaOS",
                        $parametros
                    );
            }
                
    public function associarCodIntOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osp/",
                        "AssociarCodIntOS",
                        $parametros
                    );
            }
                
    public function cancelarOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osp/",
                        "CancelarOS",
                        $parametros
                    );
            }
                
    public function duplicarOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osp/",
                        "DuplicarOS",
                        $parametros
                    );
            }
                
    public function faturarOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osp/",
                        "FaturarOS",
                        $parametros
                    );
            }
                
    public function reenviarOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osp/",
                        "ReenviarOS",
                        $parametros
                    );
            }
                
    public function validarOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/osp/",
                        "ValidarOS",
                        $parametros
                    );
            }
                
    public function faturarLoteOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/oslote/",
                        "FaturarLoteOS",
                        $parametros
                    );
            }
                
    public function listarLoteNfse(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/oslote/",
                        "ListarLoteNfse",
                        $parametros
                    );
            }
                
    public function listarLotesOS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/oslote/",
                        "ListarLotesOS",
                        $parametros
                    );
            }
                
    public function statusLoteOS(array $parametros): array { 
                    //Status do lote faturado a partir do ID. 
                    return $this->chamarApi(
                        "servicos/oslote/",
                        "StatusLoteOS",
                        $parametros
                    );
            }
                
    public function alterarContrato(array $parametros): array { 
                    //Alterar um Contrato 
                    return $this->chamarApi(
                        "servicos/contrato/",
                        "AlterarContrato",
                        $parametros
                    );
            }
                
    public function consultarContrato(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/contrato/",
                        "ConsultarContrato",
                        $parametros
                    );
            }
                
    public function excluirItem(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/contrato/",
                        "ExcluirItem",
                        $parametros
                    );
            }
                
    public function incluirContrato(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/contrato/",
                        "IncluirContrato",
                        $parametros
                    );
            }
                
    public function listarContratos(array $parametros): array { 
                    //Lista os contratos cadastrados. 
                    return $this->chamarApi(
                        "servicos/contrato/",
                        "ListarContratos",
                        $parametros
                    );
            }
                
    public function upsertContrato(array $parametros): array { 
                    //Inclui / Altera um contrato 
                    return $this->chamarApi(
                        "servicos/contrato/",
                        "UpsertContrato",
                        $parametros
                    );
            }
                
    public function ativarContrato(array $parametros): array { 
                    //Ativa um contrato 
                    return $this->chamarApi(
                        "servicos/contratofat/",
                        "AtivarContrato",
                        $parametros
                    );
            }
                
    public function cancelarContrato(array $parametros): array { 
                    //Cancela contrato 
                    return $this->chamarApi(
                        "servicos/contratofat/",
                        "CancelarContrato",
                        $parametros
                    );
            }
                
    public function faturarContrato(array $parametros): array { 
                    //Fatura um contrato. 
                    return $this->chamarApi(
                        "servicos/contratofat/",
                        "FaturarContrato",
                        $parametros
                    );
            }
                
    public function obterContratos(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/contratofat/",
                        "ObterContratos",
                        $parametros
                    );
            }
                
    public function reativarContrato(array $parametros): array { 
                    //Reativar contrato 
                    return $this->chamarApi(
                        "servicos/contratofat/",
                        "ReativarContrato",
                        $parametros
                    );
            }
                
    public function suspenderContrato(array $parametros): array { 
                    //Suspende contrato 
                    return $this->chamarApi(
                        "servicos/contratofat/",
                        "SuspenderContrato",
                        $parametros
                    );
            }
                
    public function validarContrato(array $parametros): array { 
                    //Valida os dados de um contrato para faturamento. 
                    return $this->chamarApi(
                        "servicos/contratofat/",
                        "ValidarContrato",
                        $parametros
                    );
            }
                
    public function faturarLoteContrato(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/contratolote/",
                        "FaturarLoteContrato",
                        $parametros
                    );
            }
                
    public function listarLotesContrato(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/contratolote/",
                        "ListarLotesContrato",
                        $parametros
                    );
            }
                
    public function statusLoteContrato(array $parametros): array { 
                    //Status do lote faturado a partir do ID. 
                    return $this->chamarApi(
                        "servicos/contratolote/",
                        "StatusLoteContrato",
                        $parametros
                    );
            }
                
    public function listarServMunic(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/listaservico/",
                        "ListarServMunic",
                        $parametros
                    );
            }
                
    public function listarTiposTrib(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/tipotrib/",
                        "ListarTiposTrib",
                        $parametros
                    );
            }
                
    public function listarLC116(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/lc116/",
                        "ListarLC116",
                        $parametros
                    );
            }
                
    public function listarNBS(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/nbs/",
                        "ListarNBS",
                        $parametros
                    );
            }
                
    public function listarProdutosIBPT(array $parametros): array { 
                    //Lista os produtos da Tabela do IBPT. 
                    return $this->chamarApi(
                        "servicos/ibpt/",
                        "ListarProdutosIBPT",
                        $parametros
                    );
            }
                
    public function listarServicosIBPT(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/ibpt/",
                        "ListarServicosIBPT",
                        $parametros
                    );
            }
                
    public function listarTipoFatContrato(array $parametros): array { 
                    //Lista os tipos de faturamento de contrato. 
                    return $this->chamarApi(
                        "servicos/contratotpfat/",
                        "ListarTipoFatContrato",
                        $parametros
                    );
            }
                
    public function listarTipoUtilizacao(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/tipoutilizacao/",
                        "ListarTipoUtilizacao",
                        $parametros
                    );
            }
                
    public function listarClassificacaoServico(array $parametros): array { 
                    // 
                    return $this->chamarApi(
                        "servicos/classificacaoservico/",
                        "ListarClassificacaoServico",
                        $parametros
                    );
            }
                
    public function listarDocumentos(array $parametros): array { 
                    //Lista de XMLs de Documentos Fiscais. 
                    return $this->chamarApi(
                        "contador/xml/",
                        "ListarDocumentos",
                        $parametros
                    );
            }
                
}