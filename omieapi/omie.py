from omieapi.scripts.cod_automatico import CodigoAutogerado


class Omie(CodigoAutogerado):
        """
        :param omie_app_key:              Chave api da omie
        :param omie_app_secret:           APi Secret da omie
        """
        

CREDENCIAIS_PARA_HOMOLOGACAO_E_TESTE =  (
        OMIE_APP_KEY  := "1560731700",
        OMIE_APP_SECRET := "226dcf372489bb45ceede61bfd98f0f1"
)

OmieHomologacao: Omie = Omie(*CREDENCIAIS_PARA_HOMOLOGACAO_E_TESTE) 
OmieHomologacaoSession: Omie = Omie(*CREDENCIAIS_PARA_HOMOLOGACAO_E_TESTE, session=True)