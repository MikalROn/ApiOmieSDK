from omieapi.omiebase import OmieBase
from compras_estoque_producao import Produtos


class Estoque(OmieBase):
    """ Classe que carrega todos os metodos ligados ao estoque """
    def Produtos(self) -> Produtos:
        return Produtos(self._appkey, self._appsecret)
