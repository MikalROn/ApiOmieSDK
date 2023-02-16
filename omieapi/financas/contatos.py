from ..core.omiebase import OmieBase


class Contatos(OmieBase):
    """ Classe com metodos relacionados a contatos """
    def consultar_contato(self, nCod, cCodInt) -> dict:
        """Consulta o Contato"""
        return self._chamar_api(
            call='ConsultarContato',
            endpoint='crm/contatos/',
            param={
                "nCod": nCod,
                "cCodInt": cCodInt
            }
        )

    def incluir_contato(self, identificacao, endereco, telefone_email) -> dict:
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

    def listar_contatos(self, pagina, registros_por_pagina) -> dict:
        """Lista os contatos do CRM."""
        return self._chamar_api(
            call='ListarContatos',
            endpoint='crm/contatos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def upsert_contato(self, identificacao, endereco, telefone_email) -> dict:
        """Upsert do contato"""
        return self._chamar_api(
            call='UpsertContato',
            endpoint='crm/contatos/',
            param={
                "identificacao": identificacao,
                "endereco": endereco,
                "telefone_email": telefone_email
            }
        )

    def verificar_contato(self, cNome, cEmail) -> dict:
        """"""
        return self._chamar_api(
            call='VerificarContato',
            endpoint='crm/contatos/',
            param={
                "cNome": cNome,
                "cEmail": cEmail
            }
        )