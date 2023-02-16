from omieapi.core.omiebase import OmieBase
from omieapi.geral import Cliente, Categorias, Empresa, Projeto, Tags


class Geral(OmieBase):
    """ Classe que possiu metodos listados na aba geral """
    def Categorias(self) -> Categorias:
        return Categorias(self._appkey, self._appsecret)

    def Cliente(self) -> Cliente:
        return Cliente(self._appkey, self._appsecret)

    def Empresa(self) -> Empresa:
        return Empresa(self._appkey, self._appsecret)

    def Projetos(self) -> Projeto:
        return Projeto(self._appkey, self._appsecret)

    def Tags(self) -> Tags:
        return Tags(self._appkey, self._appsecret)