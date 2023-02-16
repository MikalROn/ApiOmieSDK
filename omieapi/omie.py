from omiebase import OmieBase
from omie_geral import Geral


class Omie(OmieBase):
    """
    Classe que carrega todos os metodos da api
    :param omie_app_key:              Chave api da omie
    :param omie_app_secret:           APi Secret da omie
    """
    def Geral(self) -> Geral:
        return Geral(self._appkey, self._appsecret)