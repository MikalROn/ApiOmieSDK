from ..core.omiebase import OmieBase


class Projeto(OmieBase):
    """ Todos os metodos relacionados a projetos """
    def alterar_projeto(
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

    def consultar_projeto(
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

    def excluir_projeto(
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

    def incluir_projeto(
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

    def listar_projetos(
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

    def upsert_projeto(
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