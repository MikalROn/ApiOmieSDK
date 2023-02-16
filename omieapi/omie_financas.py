from omieapi.omiebase import OmieBase
from financas import *


class Financas(OmieBase):
    """ Classe que carrega todos os metodo relacionados a financias """
    def Conta(self) -> Conta:
        return Conta(self._appkey, self._appsecret)

    def CupomFiscal(self) -> CupomFiscal:
        return CupomFiscal(self._appkey, self._appsecret)