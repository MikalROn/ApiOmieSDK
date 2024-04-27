package omie;

import org.json.JSONObject;
import java.io.IOException;
import java.net.URISyntaxException;

public class OmieAuto extends OmieObject {
    public OmieAuto(String appKey, String appSecreet) {
        super(appKey, appSecreet);
    }

    public JSONObject alterarCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera os dados do cliente

        return this.chamarApi(
                "geral/clientes/",
                "AlterarCliente",
                parametros
        );
    }

    public JSONObject associarCodIntCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/clientes/",
                "AssociarCodIntCliente",
                parametros
        );
    }

    public JSONObject consultarCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta os dados de um cliente

        return this.chamarApi(
                "geral/clientes/",
                "ConsultarCliente",
                parametros
        );
    }

    public JSONObject excluirCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui um cliente da base de dados.

        return this.chamarApi(
                "geral/clientes/",
                "ExcluirCliente",
                parametros
        );
    }

    public JSONObject incluirCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui o cliente no Omie

        return this.chamarApi(
                "geral/clientes/",
                "IncluirCliente",
                parametros
        );
    }

    public JSONObject incluirClientesPorLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //DEPRECATED

        return this.chamarApi(
                "geral/clientes/",
                "IncluirClientesPorLote",
                parametros
        );
    }

    public JSONObject listarClientes(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os clientes cadastrados

        return this.chamarApi(
                "geral/clientes/",
                "ListarClientes",
                parametros
        );
    }

    public JSONObject listarClientesResumido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Realiza pesquisa dos clientes

        return this.chamarApi(
                "geral/clientes/",
                "ListarClientesResumido",
                parametros
        );
    }

    public JSONObject upsertCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/clientes/",
                "UpsertCliente",
                parametros
        );
    }

    public JSONObject upsertClienteCpfCnpj(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/clientes/",
                "UpsertClienteCpfCnpj",
                parametros
        );
    }

    public JSONObject upsertClientesPorLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //DEPRECATED

        return this.chamarApi(
                "geral/clientes/",
                "UpsertClientesPorLote",
                parametros
        );
    }

    public JSONObject alterarCaractCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/clientescaract/",
                "AlterarCaractCliente",
                parametros
        );
    }

    public JSONObject consultarCaractCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/clientescaract/",
                "ConsultarCaractCliente",
                parametros
        );
    }

    public JSONObject excluirCaractCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/clientescaract/",
                "ExcluirCaractCliente",
                parametros
        );
    }

    public JSONObject excluirTodasCaractCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/clientescaract/",
                "ExcluirTodasCaractCliente",
                parametros
        );
    }

    public JSONObject incluirCaractCliente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/clientescaract/",
                "IncluirCaractCliente",
                parametros
        );
    }

    public JSONObject excluirTags(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Remove tags associadas a um cliente.

        return this.chamarApi(
                "geral/clientetag/",
                "ExcluirTags",
                parametros
        );
    }

    public JSONObject excluirTodas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Remove todas as tags associadas a um cliente.

        return this.chamarApi(
                "geral/clientetag/",
                "ExcluirTodas",
                parametros
        );
    }

    public JSONObject incluirTags(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Associa tags a um cliente.

        return this.chamarApi(
                "geral/clientetag/",
                "IncluirTags",
                parametros
        );
    }

    public JSONObject listarTags(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as tags de um determinado cliente.

        return this.chamarApi(
                "geral/clientetag/",
                "ListarTags",
                parametros
        );
    }

    public JSONObject alterarProjeto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera um projeto

        return this.chamarApi(
                "geral/projetos/",
                "AlterarProjeto",
                parametros
        );
    }

    public JSONObject consultarProjeto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta um projeto

        return this.chamarApi(
                "geral/projetos/",
                "ConsultarProjeto",
                parametros
        );
    }

    public JSONObject excluirProjeto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui um projeto

        return this.chamarApi(
                "geral/projetos/",
                "ExcluirProjeto",
                parametros
        );
    }

    public JSONObject incluirProjeto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui um novo projeto

        return this.chamarApi(
                "geral/projetos/",
                "IncluirProjeto",
                parametros
        );
    }

    public JSONObject listarProjetos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os projetos cadastrados

        return this.chamarApi(
                "geral/projetos/",
                "ListarProjetos",
                parametros
        );
    }

    public JSONObject upsertProjeto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui / Altera um projeto.

        return this.chamarApi(
                "geral/projetos/",
                "UpsertProjeto",
                parametros
        );
    }

    public JSONObject consultarEmpresa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Realiza a consulta de um registro especifico

        return this.chamarApi(
                "geral/empresas/",
                "ConsultarEmpresa",
                parametros
        );
    }

    public JSONObject listarEmpresas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as empresas cadastradas no Omie.

        return this.chamarApi(
                "geral/empresas/",
                "ListarEmpresas",
                parametros
        );
    }

    public JSONObject alterarDepartamento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/departamentos/",
                "AlterarDepartamento",
                parametros
        );
    }

    public JSONObject consultarDepartamento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/departamentos/",
                "ConsultarDepartamento",
                parametros
        );
    }

    public JSONObject excluirDepartamento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/departamentos/",
                "ExcluirDepartamento",
                parametros
        );
    }

    public JSONObject incluirDepartamento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/departamentos/",
                "IncluirDepartamento",
                parametros
        );
    }

    public JSONObject listarDepartamentos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/departamentos/",
                "ListarDepartamentos",
                parametros
        );
    }

    public JSONObject listarDepatartamentos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //DEPRECATED

        return this.chamarApi(
                "geral/departamentos/",
                "ListarDepatartamentos",
                parametros
        );
    }

    public JSONObject alterarCategoria(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/categorias/",
                "AlterarCategoria",
                parametros
        );
    }

    public JSONObject alterarGrupoCategoria(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/categorias/",
                "AlterarGrupoCategoria",
                parametros
        );
    }

    public JSONObject consultarCategoria(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta uma categoria

        return this.chamarApi(
                "geral/categorias/",
                "ConsultarCategoria",
                parametros
        );
    }

    public JSONObject incluirCategoria(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/categorias/",
                "IncluirCategoria",
                parametros
        );
    }

    public JSONObject incluirGrupoCategoria(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/categorias/",
                "IncluirGrupoCategoria",
                parametros
        );
    }

    public JSONObject listarCategorias(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as categorias cadastradas

        return this.chamarApi(
                "geral/categorias/",
                "ListarCategorias",
                parametros
        );
    }

    public JSONObject listarParcelas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista de Parcelas cadastradas.

        return this.chamarApi(
                "geral/parcelas/",
                "ListarParcelas",
                parametros
        );
    }

    public JSONObject listarTipoAtiv(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar Tipos de Atividade.

        return this.chamarApi(
                "geral/tpativ/",
                "ListarTipoAtiv",
                parametros
        );
    }

    public JSONObject listarCNAE(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar os CNAEs cadastrados

        return this.chamarApi(
                "produtos/cnae/",
                "ListarCNAE",
                parametros
        );
    }

    public JSONObject pesquisarCidades(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/cidades/",
                "PesquisarCidades",
                parametros
        );
    }

    public JSONObject listarPaises(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/paises/",
                "ListarPaises",
                parametros
        );
    }

    public JSONObject listarTiposAnexos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listagem de tipos de anexos.

        return this.chamarApi(
                "geral/tiposanexo/",
                "ListarTiposAnexos",
                parametros
        );
    }

    public JSONObject consultarAnexo(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/anexo/",
                "ConsultarAnexo",
                parametros
        );
    }

    public JSONObject excluirAnexo(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/anexo/",
                "ExcluirAnexo",
                parametros
        );
    }

    public JSONObject incluirAnexo(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui o anexo para um documento.

        return this.chamarApi(
                "geral/anexo/",
                "IncluirAnexo",
                parametros
        );
    }

    public JSONObject listarAnexo(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/anexo/",
                "ListarAnexo",
                parametros
        );
    }

    public JSONObject obterAnexo(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/anexo/",
                "ObterAnexo",
                parametros
        );
    }

    public JSONObject alterarTipoEntrega(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Alterar tipo de entrega

        return this.chamarApi(
                "geral/tiposentrega/",
                "AlterarTipoEntrega",
                parametros
        );
    }

    public JSONObject consultarTipoEntrega(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consultar tipo de entrega

        return this.chamarApi(
                "geral/tiposentrega/",
                "ConsultarTipoEntrega",
                parametros
        );
    }

    public JSONObject excluirTipoEntrega(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Excluir tipo de entrega

        return this.chamarApi(
                "geral/tiposentrega/",
                "ExcluirTipoEntrega",
                parametros
        );
    }

    public JSONObject incluirTipoEntrega(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Incluir tipo de entrega

        return this.chamarApi(
                "geral/tiposentrega/",
                "IncluirTipoEntrega",
                parametros
        );
    }

    public JSONObject listarTipoEntrega(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar tipo de entrega

        return this.chamarApi(
                "geral/tiposentrega/",
                "ListarTipoEntrega",
                parametros
        );
    }

    public JSONObject listarTipoAssinante(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os tipos de assinante

        return this.chamarApi(
                "geral/tipoassinante/",
                "ListarTipoAssinante",
                parametros
        );
    }

    public JSONObject alterarConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contas/",
                "AlterarConta",
                parametros
        );
    }

    public JSONObject consultarConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contas/",
                "ConsultarConta",
                parametros
        );
    }

    public JSONObject excluirConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contas/",
                "ExcluirConta",
                parametros
        );
    }

    public JSONObject incluirConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contas/",
                "IncluirConta",
                parametros
        );
    }

    public JSONObject listarContas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as contas do CRM.

        return this.chamarApi(
                "crm/contas/",
                "ListarContas",
                parametros
        );
    }

    public JSONObject upsertConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contas/",
                "UpsertConta",
                parametros
        );
    }

    public JSONObject verificarConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Verifica se uma conta foi criada a partir do nome e e-mail.

        return this.chamarApi(
                "crm/contas/",
                "VerificarConta",
                parametros
        );
    }

    public JSONObject alterarCaractConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contascaract/",
                "AlterarCaractConta",
                parametros
        );
    }

    public JSONObject consultarCaractConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contascaract/",
                "ConsultarCaractConta",
                parametros
        );
    }

    public JSONObject excluirCaractConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contascaract/",
                "ExcluirCaractConta",
                parametros
        );
    }

    public JSONObject excluirTodasCaractConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contascaract/",
                "ExcluirTodasCaractConta",
                parametros
        );
    }

    public JSONObject incluirCaractConta(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contascaract/",
                "IncluirCaractConta",
                parametros
        );
    }

    public JSONObject alterarContato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contatos/",
                "AlterarContato",
                parametros
        );
    }

    public JSONObject consultarContato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta o Contato

        return this.chamarApi(
                "crm/contatos/",
                "ConsultarContato",
                parametros
        );
    }

    public JSONObject excluirContato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contatos/",
                "ExcluirContato",
                parametros
        );
    }

    public JSONObject incluirContato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui um novo Contato

        return this.chamarApi(
                "crm/contatos/",
                "IncluirContato",
                parametros
        );
    }

    public JSONObject listarContatos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os contatos do CRM.

        return this.chamarApi(
                "crm/contatos/",
                "ListarContatos",
                parametros
        );
    }

    public JSONObject upsertContato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Upsert do contato

        return this.chamarApi(
                "crm/contatos/",
                "UpsertContato",
                parametros
        );
    }

    public JSONObject verificarContato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/contatos/",
                "VerificarContato",
                parametros
        );
    }

    public JSONObject alterarOportunidade(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/oportunidades/",
                "AlterarOportunidade",
                parametros
        );
    }

    public JSONObject consultarOportunidade(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta de oportunidade.

        return this.chamarApi(
                "crm/oportunidades/",
                "ConsultarOportunidade",
                parametros
        );
    }

    public JSONObject excluirOportunidade(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/oportunidades/",
                "ExcluirOportunidade",
                parametros
        );
    }

    public JSONObject incluirOportunidade(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Incluir uma oportunidade.

        return this.chamarApi(
                "crm/oportunidades/",
                "IncluirOportunidade",
                parametros
        );
    }

    public JSONObject listarOportunidades(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista de oportunidades.

        return this.chamarApi(
                "crm/oportunidades/",
                "ListarOportunidades",
                parametros
        );
    }

    public JSONObject upsertOportunidade(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Upsert de oportunidade.

        return this.chamarApi(
                "crm/oportunidades/",
                "UpsertOportunidade",
                parametros
        );
    }

    public JSONObject obterListaOp(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista de Oportunidades.

        return this.chamarApi(
                "crm/oportunidades-resumo/",
                "ObterListaOp",
                parametros
        );
    }

    public JSONObject obterResumoOp(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Resumo das oportunidades.

        return this.chamarApi(
                "crm/oportunidades-resumo/",
                "ObterResumoOp",
                parametros
        );
    }

    public JSONObject alterarTarefa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera uma tarefa.

        return this.chamarApi(
                "crm/tarefas/",
                "AlterarTarefa",
                parametros
        );
    }

    public JSONObject calendarioTarefas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/tarefas/",
                "CalendarioTarefas",
                parametros
        );
    }

    public JSONObject consultarTarefa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta uma tarefa da oportunidade.

        return this.chamarApi(
                "crm/tarefas/",
                "ConsultarTarefa",
                parametros
        );
    }

    public JSONObject excluirTarefa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui um tarefa.

        return this.chamarApi(
                "crm/tarefas/",
                "ExcluirTarefa",
                parametros
        );
    }

    public JSONObject incluirTarefa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui uma tarefa na oportunidade.

        return this.chamarApi(
                "crm/tarefas/",
                "IncluirTarefa",
                parametros
        );
    }

    public JSONObject listarEmailsTarefas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os  emails tarefas.

        return this.chamarApi(
                "crm/tarefas/",
                "ListarEmailsTarefas",
                parametros
        );
    }

    public JSONObject listarTarefas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Tarefas da oportunidade.

        return this.chamarApi(
                "crm/tarefas/",
                "ListarTarefas",
                parametros
        );
    }

    public JSONObject upsertTarefa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/tarefas/",
                "UpsertTarefa",
                parametros
        );
    }

    public JSONObject obterDetalhesTarefa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta os detalhes de uma tafera.

        return this.chamarApi(
                "crm/tarefas-resumo/",
                "ObterDetalhesTarefa",
                parametros
        );
    }

    public JSONObject obterListaTarefas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/tarefas-resumo/",
                "ObterListaTarefas",
                parametros
        );
    }

    public JSONObject obterResumoTarefas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Resumos das tarefas do CRM.

        return this.chamarApi(
                "crm/tarefas-resumo/",
                "ObterResumoTarefas",
                parametros
        );
    }

    public JSONObject listarSolucoes(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/solucoes/",
                "ListarSolucoes",
                parametros
        );
    }

    public JSONObject listarFases(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Fases da Oportunidade

        return this.chamarApi(
                "crm/fases/",
                "ListarFases",
                parametros
        );
    }

    public JSONObject listarUsuarios(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/usuarios/",
                "ListarUsuarios",
                parametros
        );
    }

    public JSONObject obterUsuarios(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "crm/usuarios/",
                "ObterUsuarios",
                parametros
        );
    }

    public JSONObject listarStatus(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Status da oportunidade.

        return this.chamarApi(
                "crm/status/",
                "ListarStatus",
                parametros
        );
    }

    public JSONObject listarMotivos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Motivos da oportunidade.

        return this.chamarApi(
                "crm/motivos/",
                "ListarMotivos",
                parametros
        );
    }

    public JSONObject listarTipos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Tipos de oportunidades.

        return this.chamarApi(
                "crm/tipos/",
                "ListarTipos",
                parametros
        );
    }

    public JSONObject listarParceiros(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Parceiros e equipes da oportunidade.

        return this.chamarApi(
                "crm/parceiros/",
                "ListarParceiros",
                parametros
        );
    }

    public JSONObject listarFinders(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Finders da oportunidade.

        return this.chamarApi(
                "crm/finders/",
                "ListarFinders",
                parametros
        );
    }

    public JSONObject listarOrigens(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Origens da oportunidade.

        return this.chamarApi(
                "crm/origens/",
                "ListarOrigens",
                parametros
        );
    }

    public JSONObject listarConcorrentes(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Concorrentes da oportunidade.

        return this.chamarApi(
                "crm/concorrentes/",
                "ListarConcorrentes",
                parametros
        );
    }

    public JSONObject listarVerticais(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as verticais cadastradas.

        return this.chamarApi(
                "crm/verticais/",
                "ListarVerticais",
                parametros
        );
    }

    public JSONObject alterarVendedor(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera os dados de um vendedor

        return this.chamarApi(
                "geral/vendedores/",
                "AlterarVendedor",
                parametros
        );
    }

    public JSONObject consultarVendedor(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta os dados de um vendedor

        return this.chamarApi(
                "geral/vendedores/",
                "ConsultarVendedor",
                parametros
        );
    }

    public JSONObject excluirVendedor(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui um vendedor

        return this.chamarApi(
                "geral/vendedores/",
                "ExcluirVendedor",
                parametros
        );
    }

    public JSONObject incluirVendedor(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui um vendedor

        return this.chamarApi(
                "geral/vendedores/",
                "IncluirVendedor",
                parametros
        );
    }

    public JSONObject listarVendedores(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listagem de Vendedores

        return this.chamarApi(
                "geral/vendedores/",
                "ListarVendedores",
                parametros
        );
    }

    public JSONObject upsertVendedor(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui / Altera um vendedor

        return this.chamarApi(
                "geral/vendedores/",
                "UpsertVendedor",
                parametros
        );
    }

    public JSONObject consultarTipoTarefa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta tipo de tarefa

        return this.chamarApi(
                "crm/tipostarefa/",
                "ConsultarTipoTarefa",
                parametros
        );
    }

    public JSONObject excluirTipoTarefa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Excluir tipo de tarefa

        return this.chamarApi(
                "crm/tipostarefa/",
                "ExcluirTipoTarefa",
                parametros
        );
    }

    public JSONObject listarTiposTarefa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista tipos de tarefa

        return this.chamarApi(
                "crm/tipostarefa/",
                "ListarTiposTarefa",
                parametros
        );
    }

    public JSONObject alterarContaCorrente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera a Conta Corrente

        return this.chamarApi(
                "geral/contacorrente/",
                "AlterarContaCorrente",
                parametros
        );
    }

    public JSONObject consultarContaCorrente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Realiza a consulta de uma conta corrente

        return this.chamarApi(
                "geral/contacorrente/",
                "ConsultarContaCorrente",
                parametros
        );
    }

    public JSONObject excluirContaCorrente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Excluir a Conta Corrente

        return this.chamarApi(
                "geral/contacorrente/",
                "ExcluirContaCorrente",
                parametros
        );
    }

    public JSONObject incluirContaCorrente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui uma conta corrente

        return this.chamarApi(
                "geral/contacorrente/",
                "IncluirContaCorrente",
                parametros
        );
    }

    public JSONObject listarContasCorrentes(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar Contas Correntes

        return this.chamarApi(
                "geral/contacorrente/",
                "ListarContasCorrentes",
                parametros
        );
    }

    public JSONObject listarResumoContasCorrentes(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar resumida de Contas correntes.

        return this.chamarApi(
                "geral/contacorrente/",
                "ListarResumoContasCorrentes",
                parametros
        );
    }

    public JSONObject pesquisarContaCorrente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //DEPRECATED

        return this.chamarApi(
                "geral/contacorrente/",
                "PesquisarContaCorrente",
                parametros
        );
    }

    public JSONObject upsertContaCorrente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Upsert da Conta Corrente

        return this.chamarApi(
                "geral/contacorrente/",
                "UpsertContaCorrente",
                parametros
        );
    }

    public JSONObject upsertContaCorrentePorLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Upsert por lote de Conta Corrente

        return this.chamarApi(
                "geral/contacorrente/",
                "UpsertContaCorrentePorLote",
                parametros
        );
    }

    public JSONObject alterarLancCC(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/contacorrentelancamentos/",
                "AlterarLancCC",
                parametros
        );
    }

    public JSONObject consultaLancCC(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/contacorrentelancamentos/",
                "ConsultaLancCC",
                parametros
        );
    }

    public JSONObject excluirLancCC(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/contacorrentelancamentos/",
                "ExcluirLancCC",
                parametros
        );
    }

    public JSONObject incluirLancCC(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/contacorrentelancamentos/",
                "IncluirLancCC",
                parametros
        );
    }

    public JSONObject listarLancCC(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/contacorrentelancamentos/",
                "ListarLancCC",
                parametros
        );
    }

    public JSONObject alterarContaPagar(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera uma conta a pagar

        return this.chamarApi(
                "financas/contapagar/",
                "AlterarContaPagar",
                parametros
        );
    }

    public JSONObject cancelarPagamento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancela um pagamento realizado no Contas a Pagar

        return this.chamarApi(
                "financas/contapagar/",
                "CancelarPagamento",
                parametros
        );
    }

    public JSONObject consultarContaPagar(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta uma conta a pagar

        return this.chamarApi(
                "financas/contapagar/",
                "ConsultarContaPagar",
                parametros
        );
    }

    public JSONObject excluirContaPagar(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui uma conta a pagar

        return this.chamarApi(
                "financas/contapagar/",
                "ExcluirContaPagar",
                parametros
        );
    }

    public JSONObject incluirContaPagar(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui uma conta a Pagar.

        return this.chamarApi(
                "financas/contapagar/",
                "IncluirContaPagar",
                parametros
        );
    }

    public JSONObject incluirContaPagarPorLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/contapagar/",
                "IncluirContaPagarPorLote",
                parametros
        );
    }

    public JSONObject lancarPagamento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Efetua a baixa de um pagamento do contas a pagar.

        return this.chamarApi(
                "financas/contapagar/",
                "LancarPagamento",
                parametros
        );
    }

    public JSONObject listarContasPagar(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar as Contas a Pagar

        return this.chamarApi(
                "financas/contapagar/",
                "ListarContasPagar",
                parametros
        );
    }

    public JSONObject upsertContaPagar(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Upsert do Contas a Pagar

        return this.chamarApi(
                "financas/contapagar/",
                "UpsertContaPagar",
                parametros
        );
    }

    public JSONObject upsertContaPagarPorLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Efetua o UPSERT do Contas a Pagar por Lote

        return this.chamarApi(
                "financas/contapagar/",
                "UpsertContaPagarPorLote",
                parametros
        );
    }

    public JSONObject alterarContaReceber(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera um conta a receber

        return this.chamarApi(
                "financas/contareceber/",
                "AlterarContaReceber",
                parametros
        );
    }

    public JSONObject cancelarContaReceber(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancelamento do boleto gerado de uma conta a receber

        return this.chamarApi(
                "financas/contareceber/",
                "CancelarContaReceber",
                parametros
        );
    }

    public JSONObject cancelarRecebimento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Efetua o cancelamento de um recebimento de Contas a Receber.

        return this.chamarApi(
                "financas/contareceber/",
                "CancelarRecebimento",
                parametros
        );
    }

    public JSONObject conciliarRecebimento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/contareceber/",
                "ConciliarRecebimento",
                parametros
        );
    }

    public JSONObject consultarContaReceber(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta uma Conta a Receber

        return this.chamarApi(
                "financas/contareceber/",
                "ConsultarContaReceber",
                parametros
        );
    }

    public JSONObject desconciliarRecebimento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Desconciliar o Recebimento

        return this.chamarApi(
                "financas/contareceber/",
                "DesconciliarRecebimento",
                parametros
        );
    }

    public JSONObject excluirContaReceber(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui uma conta a receber

        return this.chamarApi(
                "financas/contareceber/",
                "ExcluirContaReceber",
                parametros
        );
    }

    public JSONObject incluirContaReceber(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui uma conta a Receber

        return this.chamarApi(
                "financas/contareceber/",
                "IncluirContaReceber",
                parametros
        );
    }

    public JSONObject incluirContaReceberPorLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/contareceber/",
                "IncluirContaReceberPorLote",
                parametros
        );
    }

    public JSONObject lancarRecebimento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/contareceber/",
                "LancarRecebimento",
                parametros
        );
    }

    public JSONObject listarContasReceber(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as contas a receber cadastradas.

        return this.chamarApi(
                "financas/contareceber/",
                "ListarContasReceber",
                parametros
        );
    }

    public JSONObject upsertContaReceber(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Executa o Upsert do Contas a receber

        return this.chamarApi(
                "financas/contareceber/",
                "UpsertContaReceber",
                parametros
        );
    }

    public JSONObject upsertContaReceberPorLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Efetua o UPSERT do Contas a Receber por Lote.

        return this.chamarApi(
                "financas/contareceber/",
                "UpsertContaReceberPorLote",
                parametros
        );
    }

    public JSONObject cancelarBoleto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancela o Boleto.

        return this.chamarApi(
                "financas/contareceberboleto/",
                "CancelarBoleto",
                parametros
        );
    }

    public JSONObject gerarBoleto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Gera um Boleto referente a um Contas a Receber.

        return this.chamarApi(
                "financas/contareceberboleto/",
                "GerarBoleto",
                parametros
        );
    }

    public JSONObject obterBoleto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Disponibiliza o link de Download do Boleto.

        return this.chamarApi(
                "financas/contareceberboleto/",
                "ObterBoleto",
                parametros
        );
    }

    public JSONObject prorrogarBoleto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Prorroga o vencimento do Boleto.

        return this.chamarApi(
                "financas/contareceberboleto/",
                "ProrrogarBoleto",
                parametros
        );
    }

    public JSONObject cancelarPix(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Efetua o cancelamento de um PIX

        return this.chamarApi(
                "financas/pix/",
                "CancelarPix",
                parametros
        );
    }

    public JSONObject gerarPix(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Gera o QrCode de um PIX.

        return this.chamarApi(
                "financas/pix/",
                "GerarPix",
                parametros
        );
    }

    public JSONObject gerarQrCodePix(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/pix/",
                "GerarQrCodePix",
                parametros
        );
    }

    public JSONObject listarPix(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/pix/",
                "ListarPix",
                parametros
        );
    }

    public JSONObject listarStatusPix(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/pix/",
                "ListarStatusPix",
                parametros
        );
    }

    public JSONObject obterPix(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/pix/",
                "ObterPix",
                parametros
        );
    }

    public JSONObject obterStatusPix(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/pix/",
                "ObterStatusPix",
                parametros
        );
    }

    public JSONObject listarExtrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listagem do Extrato

        return this.chamarApi(
                "financas/extrato/",
                "ListarExtrato",
                parametros
        );
    }

    public JSONObject listarOrcamentos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/caixa/",
                "ListarOrcamentos",
                parametros
        );
    }

    public JSONObject obterURLBoleto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //DEPRECATED

        return this.chamarApi(
                "financas/pesquisartitulos/",
                "ObterURLBoleto",
                parametros
        );
    }

    public JSONObject pesquisarExcluidos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //DEPRECATED

        return this.chamarApi(
                "financas/pesquisartitulos/",
                "PesquisarExcluidos",
                parametros
        );
    }

    public JSONObject pesquisarLancamentos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "financas/pesquisartitulos/",
                "PesquisarLancamentos",
                parametros
        );
    }

    public JSONObject listarMovimentos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "estoque/movestoque/",
                "ListarMovimentos",
                parametros
        );
    }

    public JSONObject obterResumoContador(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Obtem o resumo do painel do contador.

        return this.chamarApi(
                "contador/resumo/",
                "ObterResumoContador",
                parametros
        );
    }

    public JSONObject consultarBanco(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/bancos/",
                "ConsultarBanco",
                parametros
        );
    }

    public JSONObject listarBancos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exibe uma lista com os banco cadastrados.

        return this.chamarApi(
                "geral/bancos/",
                "ListarBancos",
                parametros
        );
    }

    public JSONObject consultarTipoDocumento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/tiposdoc/",
                "ConsultarTipoDocumento",
                parametros
        );
    }

    public JSONObject pesquisarTipoDocumento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Pesquisa o tipo de documento

        return this.chamarApi(
                "geral/tiposdoc/",
                "PesquisarTipoDocumento",
                parametros
        );
    }

    public JSONObject listarTiposCC(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar os tipos de contas correntes.

        return this.chamarApi(
                "geral/tipocc/",
                "ListarTiposCC",
                parametros
        );
    }

    public JSONObject listarCadastroDRE(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as contas do DRE

        return this.chamarApi(
                "geral/dre/",
                "ListarCadastroDRE",
                parametros
        );
    }

    public JSONObject consultarFinalTransf(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/finaltransf/",
                "ConsultarFinalTransf",
                parametros
        );
    }

    public JSONObject listarFinalTransf(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/finaltransf/",
                "ListarFinalTransf",
                parametros
        );
    }

    public JSONObject listarOrigem(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista Origem de pedidos.

        return this.chamarApi(
                "geral/origempedido/",
                "ListarOrigem",
                parametros
        );
    }

    public JSONObject listarBandeiras(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/bandeiracartao/",
                "ListarBandeiras",
                parametros
        );
    }

    public JSONObject alterarProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/produtos/",
                "AlterarProduto",
                parametros
        );
    }

    public JSONObject associarCodIntProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/produtos/",
                "AssociarCodIntProduto",
                parametros
        );
    }

    public JSONObject consultarProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta um produto.

        return this.chamarApi(
                "geral/produtos/",
                "ConsultarProduto",
                parametros
        );
    }

    public JSONObject excluirProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui um produto

        return this.chamarApi(
                "geral/produtos/",
                "ExcluirProduto",
                parametros
        );
    }

    public JSONObject incluirProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Incluir um produto.

        return this.chamarApi(
                "geral/produtos/",
                "IncluirProduto",
                parametros
        );
    }

    public JSONObject incluirProdutosPorLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //DEPRECATED

        return this.chamarApi(
                "geral/produtos/",
                "IncluirProdutosPorLote",
                parametros
        );
    }

    public JSONObject listarProdutos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista completa do cadastro de produtos

        return this.chamarApi(
                "geral/produtos/",
                "ListarProdutos",
                parametros
        );
    }

    public JSONObject listarProdutosResumido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os produtos cadastrados

        return this.chamarApi(
                "geral/produtos/",
                "ListarProdutosResumido",
                parametros
        );
    }

    public JSONObject upsertProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/produtos/",
                "UpsertProduto",
                parametros
        );
    }

    public JSONObject upsertProdutosPorLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //DEPRECATED

        return this.chamarApi(
                "geral/produtos/",
                "UpsertProdutosPorLote",
                parametros
        );
    }

    public JSONObject alterarCaractProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/prodcaract/",
                "AlterarCaractProduto",
                parametros
        );
    }

    public JSONObject consultarCaractProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/prodcaract/",
                "ConsultarCaractProduto",
                parametros
        );
    }

    public JSONObject excluirCaractProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/prodcaract/",
                "ExcluirCaractProduto",
                parametros
        );
    }

    public JSONObject incluirCaractProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/prodcaract/",
                "IncluirCaractProduto",
                parametros
        );
    }

    public JSONObject listarCaractProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/prodcaract/",
                "ListarCaractProduto",
                parametros
        );
    }

    public JSONObject alterarEstrutura(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Alterar a estrutura de um produto.

        return this.chamarApi(
                "geral/malha/",
                "AlterarEstrutura",
                parametros
        );
    }

    public JSONObject consultarEstrutura(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta a estrutura do produto.

        return this.chamarApi(
                "geral/malha/",
                "ConsultarEstrutura",
                parametros
        );
    }

    public JSONObject excluirEstrutura(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Excluir item da estrutura de um produto.

        return this.chamarApi(
                "geral/malha/",
                "ExcluirEstrutura",
                parametros
        );
    }

    public JSONObject incluirEstrutura(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/malha/",
                "IncluirEstrutura",
                parametros
        );
    }

    public JSONObject listarEstruturas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as estruturas de produtos.

        return this.chamarApi(
                "geral/malha/",
                "ListarEstruturas",
                parametros
        );
    }

    public JSONObject alterarComponentesKit(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui/Altera/Exclui os componentes do KIT.

        return this.chamarApi(
                "geral/produtoskit/",
                "AlterarComponentesKit",
                parametros
        );
    }

    public JSONObject alterarReq(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/requisicaocompra/",
                "AlterarReq",
                parametros
        );
    }

    public JSONObject consultarReq(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/requisicaocompra/",
                "ConsultarReq",
                parametros
        );
    }

    public JSONObject excluirReq(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/requisicaocompra/",
                "ExcluirReq",
                parametros
        );
    }

    public JSONObject incluirReq(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/requisicaocompra/",
                "IncluirReq",
                parametros
        );
    }

    public JSONObject pesquisarReq(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/requisicaocompra/",
                "PesquisarReq",
                parametros
        );
    }

    public JSONObject upsertReq(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/requisicaocompra/",
                "UpsertReq",
                parametros
        );
    }

    public JSONObject alteraPedCompra(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/pedidocompra/",
                "AlteraPedCompra",
                parametros
        );
    }

    public JSONObject consultarPedCompra(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/pedidocompra/",
                "ConsultarPedCompra",
                parametros
        );
    }

    public JSONObject excluirPedCompra(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Excluir um Pedido de Compra

        return this.chamarApi(
                "produtos/pedidocompra/",
                "ExcluirPedCompra",
                parametros
        );
    }

    public JSONObject incluirPedCompra(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Incluir um Pedido de Compra

        return this.chamarApi(
                "produtos/pedidocompra/",
                "IncluirPedCompra",
                parametros
        );
    }

    public JSONObject pesquisarPedCompra(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/pedidocompra/",
                "PesquisarPedCompra",
                parametros
        );
    }

    public JSONObject upsertPedCompra(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/pedidocompra/",
                "UpsertPedCompra",
                parametros
        );
    }

    public JSONObject alterarOrdemProducao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/op/",
                "AlterarOrdemProducao",
                parametros
        );
    }

    public JSONObject concluirOrdemProducao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/op/",
                "ConcluirOrdemProducao",
                parametros
        );
    }

    public JSONObject consultarOrdemProducao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/op/",
                "ConsultarOrdemProducao",
                parametros
        );
    }

    public JSONObject excluirOrdemProducao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/op/",
                "ExcluirOrdemProducao",
                parametros
        );
    }

    public JSONObject incluirOrdemProducao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/op/",
                "IncluirOrdemProducao",
                parametros
        );
    }

    public JSONObject listarOrdemProducao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/op/",
                "ListarOrdemProducao",
                parametros
        );
    }

    public JSONObject reverterOrdemProducao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/op/",
                "ReverterOrdemProducao",
                parametros
        );
    }

    public JSONObject upsertOrdemProducao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/op/",
                "UpsertOrdemProducao",
                parametros
        );
    }

    public JSONObject alterarNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Alterar nota de entrada

        return this.chamarApi(
                "produtos/notaentrada/",
                "AlterarNotaEnt",
                parametros
        );
    }

    public JSONObject consultarNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consultar nota de entrada

        return this.chamarApi(
                "produtos/notaentrada/",
                "ConsultarNotaEnt",
                parametros
        );
    }

    public JSONObject excluirNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Excluir nota de entrada

        return this.chamarApi(
                "produtos/notaentrada/",
                "ExcluirNotaEnt",
                parametros
        );
    }

    public JSONObject incluirNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Incluir nota de entrada

        return this.chamarApi(
                "produtos/notaentrada/",
                "IncluirNotaEnt",
                parametros
        );
    }

    public JSONObject listarNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listagem de nota de entrada

        return this.chamarApi(
                "produtos/notaentrada/",
                "ListarNotaEnt",
                parametros
        );
    }

    public JSONObject statusNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Status de nota de entrada

        return this.chamarApi(
                "produtos/notaentrada/",
                "StatusNotaEnt",
                parametros
        );
    }

    public JSONObject cancelarNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancelar nota de entrada

        return this.chamarApi(
                "produtos/notaentradafat/",
                "CancelarNotaEnt",
                parametros
        );
    }

    public JSONObject concluirNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Concluir nota de entrada

        return this.chamarApi(
                "produtos/notaentradafat/",
                "ConcluirNotaEnt",
                parametros
        );
    }

    public JSONObject conferirNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Conferir nota de entrada

        return this.chamarApi(
                "produtos/notaentradafat/",
                "ConferirNotaEnt",
                parametros
        );
    }

    public JSONObject duplicarNotaEnt(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Duplicar nota de entrada

        return this.chamarApi(
                "produtos/notaentradafat/",
                "DuplicarNotaEnt",
                parametros
        );
    }

    public JSONObject alterarEtapaRecebimento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Alterar etapa recebimento NFe

        return this.chamarApi(
                "produtos/recebimentonfe/",
                "AlterarEtapaRecebimento",
                parametros
        );
    }

    public JSONObject alterarRecebimento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Alterar recebimento de NFe

        return this.chamarApi(
                "produtos/recebimentonfe/",
                "AlterarRecebimento",
                parametros
        );
    }

    public JSONObject concluirRecebimento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Concluir recebimento de NFe

        return this.chamarApi(
                "produtos/recebimentonfe/",
                "ConcluirRecebimento",
                parametros
        );
    }

    public JSONObject consultarRecebimento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consultar recebimento de NFe

        return this.chamarApi(
                "produtos/recebimentonfe/",
                "ConsultarRecebimento",
                parametros
        );
    }

    public JSONObject listarRecebimentos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar recebimento de NFe

        return this.chamarApi(
                "produtos/recebimentonfe/",
                "ListarRecebimentos",
                parametros
        );
    }

    public JSONObject reverterRecebimento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Reverter recebimento NFe

        return this.chamarApi(
                "produtos/recebimentonfe/",
                "ReverterRecebimento",
                parametros
        );
    }

    public JSONObject alterarFamilia(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera uma familia de produto

        return this.chamarApi(
                "geral/familias/",
                "AlterarFamilia",
                parametros
        );
    }

    public JSONObject consultarFamilia(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta uma familia de produto

        return this.chamarApi(
                "geral/familias/",
                "ConsultarFamilia",
                parametros
        );
    }

    public JSONObject excluirFamilia(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui uma familia de produto

        return this.chamarApi(
                "geral/familias/",
                "ExcluirFamilia",
                parametros
        );
    }

    public JSONObject incluirFamilia(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui uma familia de produto

        return this.chamarApi(
                "geral/familias/",
                "IncluirFamilia",
                parametros
        );
    }

    public JSONObject pesquisarFamilias(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listagem de familias cadastradas

        return this.chamarApi(
                "geral/familias/",
                "PesquisarFamilias",
                parametros
        );
    }

    public JSONObject upsertFamilia(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui / Altera uma familia de produto

        return this.chamarApi(
                "geral/familias/",
                "UpsertFamilia",
                parametros
        );
    }

    public JSONObject listarUnidades(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as unidades de medidas

        return this.chamarApi(
                "geral/unidade/",
                "ListarUnidades",
                parametros
        );
    }

    public JSONObject listarCompradores(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os compradores cadastrados.

        return this.chamarApi(
                "estoque/comprador/",
                "ListarCompradores",
                parametros
        );
    }

    public JSONObject listarProdutoFornecedor(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar os produtos por fornecedores.

        return this.chamarApi(
                "estoque/produtofornecedor/",
                "ListarProdutoFornecedor",
                parametros
        );
    }

    public JSONObject listarFormasPagVendas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as formas de pagmento de vendas.

        return this.chamarApi(
                "produtos/formaspagvendas/",
                "ListarFormasPagVendas",
                parametros
        );
    }

    public JSONObject consultarNCM(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta um NCM

        return this.chamarApi(
                "produtos/ncm/",
                "ConsultarNCM",
                parametros
        );
    }

    public JSONObject listarNCM(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os NCMs cadastrados.

        return this.chamarApi(
                "produtos/ncm/",
                "ListarNCM",
                parametros
        );
    }

    public JSONObject listarCenarios(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/cenarios/",
                "ListarCenarios",
                parametros
        );
    }

    public JSONObject listarImpostosCenario(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/cenarios/",
                "ListarImpostosCenario",
                parametros
        );
    }

    public JSONObject listarCFOP(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar as CFOPs

        return this.chamarApi(
                "produtos/cfop/",
                "ListarCFOP",
                parametros
        );
    }

    public JSONObject listarCST(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar os CSTs do ICMS

        return this.chamarApi(
                "produtos/icmscst/",
                "ListarCST",
                parametros
        );
    }

    public JSONObject listarCSOSN(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar os CSOSN do ICMS.

        return this.chamarApi(
                "produtos/icmscsosn/",
                "ListarCSOSN",
                parametros
        );
    }

    public JSONObject listarOrigMerc(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar a origem da mercadoria do ICMS.

        return this.chamarApi(
                "produtos/icmsorigem/",
                "ListarOrigMerc",
                parametros
        );
    }

    public JSONObject listarCstPis(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar o CST do PIS.

        return this.chamarApi(
                "produtos/piscst/",
                "ListarCstPis",
                parametros
        );
    }

    public JSONObject listarCstCofins(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar CST do COFINS.

        return this.chamarApi(
                "produtos/cofinscst/",
                "ListarCstCofins",
                parametros
        );
    }

    public JSONObject listarCstIpi(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar CST do IPI.

        return this.chamarApi(
                "produtos/ipicst/",
                "ListarCstIpi",
                parametros
        );
    }

    public JSONObject listarEnqIpi(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar Enquadramento do IPI.

        return this.chamarApi(
                "produtos/ipienq/",
                "ListarEnqIpi",
                parametros
        );
    }

    public JSONObject listarTpCalc(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tpcalc/",
                "ListarTpCalc",
                parametros
        );
    }

    public JSONObject listarCEST(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar CEST.

        return this.chamarApi(
                "produtos/cest/",
                "ListarCEST",
                parametros
        );
    }

    public JSONObject alterarEstoqueMinimo(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "estoque/ajuste/",
                "AlterarEstoqueMinimo",
                parametros
        );
    }

    public JSONObject excluirAjusteEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Excluir um Movimento de Ajuste de Estoque

        return this.chamarApi(
                "estoque/ajuste/",
                "ExcluirAjusteEstoque",
                parametros
        );
    }

    public JSONObject incluirAjusteEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Incluir um Ajuste de Estoque

        return this.chamarApi(
                "estoque/ajuste/",
                "IncluirAjusteEstoque",
                parametros
        );
    }

    public JSONObject listarAjusteEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar os ajuste de estoque.

        return this.chamarApi(
                "estoque/ajuste/",
                "ListarAjusteEstoque",
                parametros
        );
    }

    public JSONObject listarMovimentoEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "estoque/consulta/",
                "ListarMovimentoEstoque",
                parametros
        );
    }

    public JSONObject listarPosEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "estoque/consulta/",
                "ListarPosEstoque",
                parametros
        );
    }

    public JSONObject listarSaldoPendente(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista o saldo pendente de estoque.

        return this.chamarApi(
                "estoque/consulta/",
                "ListarSaldoPendente",
                parametros
        );
    }

    public JSONObject movimentoEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta do Movimento de Estoque

        return this.chamarApi(
                "estoque/consulta/",
                "MovimentoEstoque",
                parametros
        );
    }

    public JSONObject posicaoEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "estoque/consulta/",
                "PosicaoEstoque",
                parametros
        );
    }

    public JSONObject consultarPrevisao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "estoque/movestoque/",
                "ConsultarPrevisao",
                parametros
        );
    }

    public JSONObject alterarLocalEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Alterar local de Estoque

        return this.chamarApi(
                "estoque/local/",
                "AlterarLocalEstoque",
                parametros
        );
    }

    public JSONObject incluirLocalEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Adiciona um local de estoque

        return this.chamarApi(
                "estoque/local/",
                "IncluirLocalEstoque",
                parametros
        );
    }

    public JSONObject listarLocaisEstoque(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os Locais de Estoque encontrados.

        return this.chamarApi(
                "estoque/local/",
                "ListarLocaisEstoque",
                parametros
        );
    }

    public JSONObject obterEstoqueProduto(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "estoque/resumo/",
                "ObterEstoqueProduto",
                parametros
        );
    }

    public JSONObject adicionarPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/pedidovenda/",
                "AdicionarPedido",
                parametros
        );
    }

    public JSONObject alterarItemPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera um item no pedido de venda.

        return this.chamarApi(
                "produtos/pedidovenda/",
                "AlterarItemPedido",
                parametros
        );
    }

    public JSONObject excluirItemPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui um item no pedido de venda.

        return this.chamarApi(
                "produtos/pedidovenda/",
                "ExcluirItemPedido",
                parametros
        );
    }

    public JSONObject excluirItensPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui todos os itens do pedido de venda.

        return this.chamarApi(
                "produtos/pedidovenda/",
                "ExcluirItensPedido",
                parametros
        );
    }

    public JSONObject incluirItemPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui um item no pedido de venda.

        return this.chamarApi(
                "produtos/pedidovenda/",
                "IncluirItemPedido",
                parametros
        );
    }

    public JSONObject totalizarPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Recalcula os totais do pedido de venda.

        return this.chamarApi(
                "produtos/pedidovenda/",
                "TotalizarPedido",
                parametros
        );
    }

    public JSONObject alterarPedFaturado(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/pedido/",
                "AlterarPedFaturado",
                parametros
        );
    }

    public JSONObject alterarPedidoVenda(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/pedido/",
                "AlterarPedidoVenda",
                parametros
        );
    }

    public JSONObject consultarPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta de Pedido de Venda de Produto

        return this.chamarApi(
                "produtos/pedido/",
                "ConsultarPedido",
                parametros
        );
    }

    public JSONObject excluirPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Excluir pedido de venda de produto

        return this.chamarApi(
                "produtos/pedido/",
                "ExcluirPedido",
                parametros
        );
    }

    public JSONObject incluirPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui um pedido de venda de produto

        return this.chamarApi(
                "produtos/pedido/",
                "IncluirPedido",
                parametros
        );
    }

    public JSONObject listarPedidos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listar os pedidos de venda de produto

        return this.chamarApi(
                "produtos/pedido/",
                "ListarPedidos",
                parametros
        );
    }

    public JSONObject simularImpostos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Simula os impostos de um pedido de venda.

        return this.chamarApi(
                "produtos/pedido/",
                "SimularImpostos",
                parametros
        );
    }

    public JSONObject statusPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta do Status do Pedido

        return this.chamarApi(
                "produtos/pedido/",
                "StatusPedido",
                parametros
        );
    }

    public JSONObject trocarEtapaPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Troca etapa do pedido.

        return this.chamarApi(
                "produtos/pedido/",
                "TrocarEtapaPedido",
                parametros
        );
    }

    public JSONObject associarCodIntPedidoVenda(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/pedidovendafat/",
                "AssociarCodIntPedidoVenda",
                parametros
        );
    }

    public JSONObject cancelarPedidoVenda(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancela um pedido de venda de produto.

        return this.chamarApi(
                "produtos/pedidovendafat/",
                "CancelarPedidoVenda",
                parametros
        );
    }

    public JSONObject duplicarPedidoVenda(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Duplica um pedido de venda de produto.

        return this.chamarApi(
                "produtos/pedidovendafat/",
                "DuplicarPedidoVenda",
                parametros
        );
    }

    public JSONObject faturarPedidoVenda(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Fatura um pedido de venda de produto.

        return this.chamarApi(
                "produtos/pedidovendafat/",
                "FaturarPedidoVenda",
                parametros
        );
    }

    public JSONObject obterPedidosVenda(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Retorna a lista de pedidos de venda a serem faturados.

        return this.chamarApi(
                "produtos/pedidovendafat/",
                "ObterPedidosVenda",
                parametros
        );
    }

    public JSONObject validarPedidoVenda(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Valida um pedido de venda de produto para faturamento.

        return this.chamarApi(
                "produtos/pedidovendafat/",
                "ValidarPedidoVenda",
                parametros
        );
    }

    public JSONObject listarEtapasPedido(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as etapas do Pedido de Venda de Produtos.

        return this.chamarApi(
                "produtos/pedidoetapas/",
                "ListarEtapasPedido",
                parametros
        );
    }

    public JSONObject averbacaoCTe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/cte/",
                "AverbacaoCTe",
                parametros
        );
    }

    public JSONObject cancelarCTe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancela um CT-e.

        return this.chamarApi(
                "produtos/cte/",
                "CancelarCTe",
                parametros
        );
    }

    public JSONObject cartaCorrecaoCTe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/cte/",
                "CartaCorrecaoCTe",
                parametros
        );
    }

    public JSONObject excluirCTe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/cte/",
                "ExcluirCTe",
                parametros
        );
    }

    public JSONObject excluirFaturaCTe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui uma fatura de um grupo de CT-es.

        return this.chamarApi(
                "produtos/cte/",
                "ExcluirFaturaCTe",
                parametros
        );
    }

    public JSONObject faturarCTe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Gera uma fatura para um grupo de CT-es.

        return this.chamarApi(
                "produtos/cte/",
                "FaturarCTe",
                parametros
        );
    }

    public JSONObject faturarLoteCTe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Gera uma fatura por lote para um grupo de CT-es.

        return this.chamarApi(
                "produtos/cte/",
                "FaturarLoteCTe",
                parametros
        );
    }

    public JSONObject importarCTe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Importar o XML de um CT-e.

        return this.chamarApi(
                "produtos/cte/",
                "ImportarCTe",
                parametros
        );
    }

    public JSONObject listarNFeTransp(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/cte/",
                "ListarNFeTransp",
                parametros
        );
    }

    public JSONObject statusFatura(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Retorna o Status da Fatura inclusa.

        return this.chamarApi(
                "produtos/cte/",
                "StatusFatura",
                parametros
        );
    }

    public JSONObject alterarRemessa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Altera uma remessa

        return this.chamarApi(
                "produtos/remessa/",
                "AlterarRemessa",
                parametros
        );
    }

    public JSONObject consultarRemessa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Consulta uma remessa.

        return this.chamarApi(
                "produtos/remessa/",
                "ConsultarRemessa",
                parametros
        );
    }

    public JSONObject incluirRemessa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui uma nova remessa

        return this.chamarApi(
                "produtos/remessa/",
                "IncluirRemessa",
                parametros
        );
    }

    public JSONObject listarRemessas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as remessas cadastradas.

        return this.chamarApi(
                "produtos/remessa/",
                "ListarRemessas",
                parametros
        );
    }

    public JSONObject statusRemessa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Retorna o status da remessa

        return this.chamarApi(
                "produtos/remessa/",
                "StatusRemessa",
                parametros
        );
    }

    public JSONObject cancelarRemessa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancelar remessa de produto

        return this.chamarApi(
                "produtos/remessafat/",
                "CancelarRemessa",
                parametros
        );
    }

    public JSONObject concluirRemessa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Concluir remessa de produto

        return this.chamarApi(
                "produtos/remessafat/",
                "ConcluirRemessa",
                parametros
        );
    }

    public JSONObject conferirRemessa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Conferir remessa de produto

        return this.chamarApi(
                "produtos/remessafat/",
                "ConferirRemessa",
                parametros
        );
    }

    public JSONObject duplicarRemessa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Duplicar remessa de produto

        return this.chamarApi(
                "produtos/remessafat/",
                "DuplicarRemessa",
                parametros
        );
    }

    public JSONObject obterDemonst(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osdocs/",
                "ObterDemonst",
                parametros
        );
    }

    public JSONObject obterNFSe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osdocs/",
                "ObterNFSe",
                parametros
        );
    }

    public JSONObject obterOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osp/",
                "ObterOS",
                parametros
        );
    }

    public JSONObject obterRPS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osdocs/",
                "ObterRPS",
                parametros
        );
    }

    public JSONObject obterRecibo(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osdocs/",
                "ObterRecibo",
                parametros
        );
    }

    public JSONObject obterViaUnica(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osdocs/",
                "ObterViaUnica",
                parametros
        );
    }

    public JSONObject fecharCaixa(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Efetua o fechamento de um determinado caixa.

        return this.chamarApi(
                "produtos/cupomfiscalincluir/",
                "FecharCaixa",
                parametros
        );
    }

    public JSONObject incluirCfeSat(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Incluir Cupom Fiscal para SAT.

        return this.chamarApi(
                "produtos/cupomfiscalincluir/",
                "IncluirCfeSat",
                parametros
        );
    }

    public JSONObject incluirCupom(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Incluir Cupom Fiscal (ECF).

        return this.chamarApi(
                "produtos/cupomfiscalincluir/",
                "IncluirCupom",
                parametros
        );
    }

    public JSONObject incluirNfce(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/cupomfiscalincluir/",
                "IncluirNfce",
                parametros
        );
    }

    public JSONObject inutilizarNfce(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inutiliza um lote de NFC-e.

        return this.chamarApi(
                "produtos/cupomfiscalincluir/",
                "InutilizarNfce",
                parametros
        );
    }

    public JSONObject cancelarCupom(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancela um cupom Fiscal

        return this.chamarApi(
                "produtos/cupomfiscal/",
                "CancelarCupom",
                parametros
        );
    }

    public JSONObject cancelarNFCE(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancelar NFC-e.

        return this.chamarApi(
                "produtos/cupomfiscal/",
                "CancelarNFCE",
                parametros
        );
    }

    public JSONObject cancelarSAT(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancelar CF-e-SAT.

        return this.chamarApi(
                "produtos/cupomfiscal/",
                "CancelarSAT",
                parametros
        );
    }

    public JSONObject devolverCupom(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/cupomfiscal/",
                "DevolverCupom",
                parametros
        );
    }

    public JSONObject excluirCupom(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Exclui um Cupom Fiscal.

        return this.chamarApi(
                "produtos/cupomfiscal/",
                "ExcluirCupom",
                parametros
        );
    }

    public JSONObject excluirCuponsPorNumero(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/cupomfiscal/",
                "ExcluirCuponsPorNumero",
                parametros
        );
    }

    public JSONObject excluirLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Excluir o lote

        return this.chamarApi(
                "produtos/cupomfiscal/",
                "ExcluirLote",
                parametros
        );
    }

    public JSONObject listarCupons(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os Cupons Fiscais.

        return this.chamarApi(
                "produtos/cupomfiscal/",
                "ListarCupons",
                parametros
        );
    }

    public JSONObject obterProximoLote(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/cupomfiscal/",
                "ObterProximoLote",
                parametros
        );
    }

    public JSONObject cuponsFiscais(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listagem dos cupons fiscais.

        return this.chamarApi(
                "produtos/cupomfiscalconsultar/",
                "CuponsFiscais",
                parametros
        );
    }

    public JSONObject cuponsItens(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listagem dos itens dos cupons fiscais

        return this.chamarApi(
                "produtos/cupomfiscalconsultar/",
                "CuponsItens",
                parametros
        );
    }

    public JSONObject cuponsPagamentos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listagem dos pagamentos dos cupons fiscais

        return this.chamarApi(
                "produtos/cupomfiscalconsultar/",
                "CuponsPagamentos",
                parametros
        );
    }

    public JSONObject importarNFCe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/nfce/",
                "ImportarNFCe",
                parametros
        );
    }

    public JSONObject importarCfeSat(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Importa o XML de um CF-e SAT.

        return this.chamarApi(
                "produtos/sat/",
                "ImportarCfeSat",
                parametros
        );
    }

    public JSONObject alterarPrecoItem(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "AlterarPrecoItem",
                parametros
        );
    }

    public JSONObject alterarTabelaPreco(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "AlterarTabelaPreco",
                parametros
        );
    }

    public JSONObject ativarTabelaPreco(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "AtivarTabelaPreco",
                parametros
        );
    }

    public JSONObject atualizarProdutos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "AtualizarProdutos",
                parametros
        );
    }

    public JSONObject consultarTabelaPreco(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "ConsultarTabelaPreco",
                parametros
        );
    }

    public JSONObject excluirTabelaPreco(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "ExcluirTabelaPreco",
                parametros
        );
    }

    public JSONObject incluirTabelaPreco(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "IncluirTabelaPreco",
                parametros
        );
    }

    public JSONObject listarTabelaItens(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "ListarTabelaItens",
                parametros
        );
    }

    public JSONObject listarTabelasPreco(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "ListarTabelasPreco",
                parametros
        );
    }

    public JSONObject suspenderTabelaPreco(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/tabelaprecos/",
                "SuspenderTabelaPreco",
                parametros
        );
    }

    public JSONObject alterarCaracteristica(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/caracteristicas/",
                "AlterarCaracteristica",
                parametros
        );
    }

    public JSONObject consultarCaracteristica(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/caracteristicas/",
                "ConsultarCaracteristica",
                parametros
        );
    }

    public JSONObject excluirCaracteristica(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/caracteristicas/",
                "ExcluirCaracteristica",
                parametros
        );
    }

    public JSONObject incluirCaracteristica(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/caracteristicas/",
                "IncluirCaracteristica",
                parametros
        );
    }

    public JSONObject listarCaracteristicas(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/caracteristicas/",
                "ListarCaracteristicas",
                parametros
        );
    }

    public JSONObject listarEtapasFaturamento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as etapas do faturamento

        return this.chamarApi(
                "produtos/etapafat/",
                "ListarEtapasFaturamento",
                parametros
        );
    }

    public JSONObject listarMeiosPagamento(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Listagem de meios de pagamento

        return this.chamarApi(
                "geral/meiospagamento/",
                "ListarMeiosPagamento",
                parametros
        );
    }

    public JSONObject listarMotivosDevol(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "geral/motivodevolucao/",
                "ListarMotivosDevol",
                parametros
        );
    }

    public JSONObject listarNFSEs(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista de NFS-es.

        return this.chamarApi(
                "servicos/nfse/",
                "ListarNFSEs",
                parametros
        );
    }

    public JSONObject getUrlDanfe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/notafiscalutil/",
                "GetUrlDanfe",
                parametros
        );
    }

    public JSONObject getUrlLogo(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Retorna a URL do Logotipo

        return this.chamarApi(
                "produtos/notafiscalutil/",
                "GetUrlLogo",
                parametros
        );
    }

    public JSONObject getUrlNotaFiscal(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Retorna a URL da Nota Fiscal

        return this.chamarApi(
                "produtos/notafiscalutil/",
                "GetUrlNotaFiscal",
                parametros
        );
    }

    public JSONObject excluirNFe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/nfe/",
                "ExcluirNFe",
                parametros
        );
    }

    public JSONObject importarCancNFe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/nfe/",
                "ImportarCancNFe",
                parametros
        );
    }

    public JSONObject importarNFe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "produtos/nfe/",
                "ImportarNFe",
                parametros
        );
    }

    public JSONObject listarNFe(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista as NFes importadas.

        return this.chamarApi(
                "produtos/nfe/",
                "ListarNFe",
                parametros
        );
    }

    public JSONObject alterarCadastroServico(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/servico/",
                "AlterarCadastroServico",
                parametros
        );
    }

    public JSONObject associarCodIntServico(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/servico/",
                "AssociarCodIntServico",
                parametros
        );
    }

    public JSONObject consultarCadastroServico(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/servico/",
                "ConsultarCadastroServico",
                parametros
        );
    }

    public JSONObject excluirCadastroServico(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/servico/",
                "ExcluirCadastroServico",
                parametros
        );
    }

    public JSONObject incluirCadastroServico(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/servico/",
                "IncluirCadastroServico",
                parametros
        );
    }

    public JSONObject listarCadastroServico(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/servico/",
                "ListarCadastroServico",
                parametros
        );
    }

    public JSONObject upsertCadastroServico(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/servico/",
                "UpsertCadastroServico",
                parametros
        );
    }

    public JSONObject alterarOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/os/",
                "AlterarOS",
                parametros
        );
    }

    public JSONObject consultarOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/os/",
                "ConsultarOS",
                parametros
        );
    }

    public JSONObject excluirOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/os/",
                "ExcluirOS",
                parametros
        );
    }

    public JSONObject incluirOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/os/",
                "IncluirOS",
                parametros
        );
    }

    public JSONObject listarOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/os/",
                "ListarOS",
                parametros
        );
    }

    public JSONObject statusOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/os/",
                "StatusOS",
                parametros
        );
    }

    public JSONObject trocarEtapaOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/os/",
                "TrocarEtapaOS",
                parametros
        );
    }

    public JSONObject associarCodIntOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osp/",
                "AssociarCodIntOS",
                parametros
        );
    }

    public JSONObject cancelarOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osp/",
                "CancelarOS",
                parametros
        );
    }

    public JSONObject duplicarOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osp/",
                "DuplicarOS",
                parametros
        );
    }

    public JSONObject faturarOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osp/",
                "FaturarOS",
                parametros
        );
    }

    public JSONObject reenviarOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osp/",
                "ReenviarOS",
                parametros
        );
    }

    public JSONObject validarOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/osp/",
                "ValidarOS",
                parametros
        );
    }

    public JSONObject faturarLoteOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/oslote/",
                "FaturarLoteOS",
                parametros
        );
    }

    public JSONObject listarLoteNfse(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/oslote/",
                "ListarLoteNfse",
                parametros
        );
    }

    public JSONObject listarLotesOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/oslote/",
                "ListarLotesOS",
                parametros
        );
    }

    public JSONObject statusLoteOS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Status do lote faturado a partir do ID.

        return this.chamarApi(
                "servicos/oslote/",
                "StatusLoteOS",
                parametros
        );
    }

    public JSONObject alterarContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Alterar um Contrato

        return this.chamarApi(
                "servicos/contrato/",
                "AlterarContrato",
                parametros
        );
    }

    public JSONObject consultarContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/contrato/",
                "ConsultarContrato",
                parametros
        );
    }

    public JSONObject excluirItem(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/contrato/",
                "ExcluirItem",
                parametros
        );
    }

    public JSONObject incluirContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/contrato/",
                "IncluirContrato",
                parametros
        );
    }

    public JSONObject listarContratos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os contratos cadastrados.

        return this.chamarApi(
                "servicos/contrato/",
                "ListarContratos",
                parametros
        );
    }

    public JSONObject upsertContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Inclui / Altera um contrato

        return this.chamarApi(
                "servicos/contrato/",
                "UpsertContrato",
                parametros
        );
    }

    public JSONObject ativarContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Ativa um contrato

        return this.chamarApi(
                "servicos/contratofat/",
                "AtivarContrato",
                parametros
        );
    }

    public JSONObject cancelarContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Cancela contrato

        return this.chamarApi(
                "servicos/contratofat/",
                "CancelarContrato",
                parametros
        );
    }

    public JSONObject faturarContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Fatura um contrato.

        return this.chamarApi(
                "servicos/contratofat/",
                "FaturarContrato",
                parametros
        );
    }

    public JSONObject obterContratos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/contratofat/",
                "ObterContratos",
                parametros
        );
    }

    public JSONObject reativarContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Reativar contrato

        return this.chamarApi(
                "servicos/contratofat/",
                "ReativarContrato",
                parametros
        );
    }

    public JSONObject suspenderContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Suspende contrato

        return this.chamarApi(
                "servicos/contratofat/",
                "SuspenderContrato",
                parametros
        );
    }

    public JSONObject validarContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Valida os dados de um contrato para faturamento.

        return this.chamarApi(
                "servicos/contratofat/",
                "ValidarContrato",
                parametros
        );
    }

    public JSONObject faturarLoteContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/contratolote/",
                "FaturarLoteContrato",
                parametros
        );
    }

    public JSONObject listarLotesContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/contratolote/",
                "ListarLotesContrato",
                parametros
        );
    }

    public JSONObject statusLoteContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Status do lote faturado a partir do ID.

        return this.chamarApi(
                "servicos/contratolote/",
                "StatusLoteContrato",
                parametros
        );
    }

    public JSONObject listarServMunic(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/listaservico/",
                "ListarServMunic",
                parametros
        );
    }

    public JSONObject listarTiposTrib(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/tipotrib/",
                "ListarTiposTrib",
                parametros
        );
    }

    public JSONObject listarLC116(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/lc116/",
                "ListarLC116",
                parametros
        );
    }

    public JSONObject listarNBS(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/nbs/",
                "ListarNBS",
                parametros
        );
    }

    public JSONObject listarProdutosIBPT(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os produtos da Tabela do IBPT.

        return this.chamarApi(
                "servicos/ibpt/",
                "ListarProdutosIBPT",
                parametros
        );
    }

    public JSONObject listarServicosIBPT(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/ibpt/",
                "ListarServicosIBPT",
                parametros
        );
    }

    public JSONObject listarTipoFatContrato(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista os tipos de faturamento de contrato.

        return this.chamarApi(
                "servicos/contratotpfat/",
                "ListarTipoFatContrato",
                parametros
        );
    }

    public JSONObject listarTipoUtilizacao(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/tipoutilizacao/",
                "ListarTipoUtilizacao",
                parametros
        );
    }

    public JSONObject listarClassificacaoServico(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //

        return this.chamarApi(
                "servicos/classificacaoservico/",
                "ListarClassificacaoServico",
                parametros
        );
    }

    public JSONObject listarDocumentos(JSONArray parametros) throws URISyntaxException, IOException, InterruptedException {
        //Lista de XMLs de Documentos Fiscais.

        return this.chamarApi(
                "contador/xml/",
                "ListarDocumentos",
                parametros
        );
    }
}