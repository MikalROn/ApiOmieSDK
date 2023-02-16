from omieapi.omiebase import OmieBase
from geral import *

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