from omieapi.core.omiebase import OmieBase
from omieapi.financas import Conta, CupomFiscal


class Financas(OmieBase):
    """ Classe que carrega todos os metodo relacionados a financias """
    def Conta(self) -> Conta:
        return Conta(self._appkey, self._appsecret)

    def CupomFiscal(self) -> CupomFiscal:
        return CupomFiscal(self._appkey, self._appsecret)