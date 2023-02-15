from omiebase import OmieBase


class Tags(OmieBase):
    """ Todos os metodos relacionados a tags """

    def excluir_tags(self, nCodCliente, cCodIntCliente, tags) -> dict:
        """ Remove tags associadas a um cliente. """
        return self._chamar_api(
            call='ExcluirTags',
            endpoint='geral/clientetag/',
            param={
                "nCodCliente": nCodCliente,
                "cCodIntCliente": cCodIntCliente,
                "tags": tags
            }
        )

    def excluir_todas(self, nCodCliente, cCodIntCliente) -> dict:
        """ Remove todas as tags associadas a um cliente. """
        return self._chamar_api(
            call='ExcluirTodas',
            endpoint='geral/clientetag/',
            param={
                "nCodCliente": nCodCliente,
                "cCodIntCliente": cCodIntCliente
            }
        )

    def incluir_tags(self, nCodCliente, cCodIntCliente, tags) -> dict:
        """ Associa tags a um cliente. """
        return self._chamar_api(
            call='IncluirTags',
            endpoint='geral/clientetag/',
            param={
                "nCodCliente": nCodCliente,
                "cCodIntCliente": cCodIntCliente,
                "tags": tags
            }
        )

    def listar_tags(self, nCodCliente, cCodIntCliente) -> dict:
        """ Lista as tags de um determinado cliente. """
        return self._chamar_api(
            call='ListarTags',
            endpoint='geral/clientetag/',
            param={
                "nCodCliente": nCodCliente,
                "cCodIntCliente": cCodIntCliente
            }
        )