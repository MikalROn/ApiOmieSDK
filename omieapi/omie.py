from omieapi.scripts.cod_automatico import CodigoAutogerado


class Omie(CodigoAutogerado):
        """
        :param omie_app_key:              Chave api da omie
        :param omie_app_secret:           APi Secret da omie
        """
        

CREDENCIAIS_PARA_HOMOLOGACAO_E_TESTE =  (
        OMIE_APP_KEY  := "38333295000",
        OMIE_APP_SECRET := "fed2163e2e8dccb53ff914ce9e2f1258"
)

OmieHomologacao: Omie = Omie(*CREDENCIAIS_PARA_HOMOLOGACAO_E_TESTE) 
OmieHomologacaoSession: Omie = Omie(*CREDENCIAIS_PARA_HOMOLOGACAO_E_TESTE, session=True)