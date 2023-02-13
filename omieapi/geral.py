from omieapi.omie import Omie


class Geral(Omie):
    """ Classe que possiu metodos listados na aba geral """
    def consulta_empresa(self, codigo_empresa: int) -> dict:
        """
        :param codigo_empresa:  integer	Código da Empresa
        """
        return self._chamar_api(
            call='ConsultarEmpresa',
            endpoint='geral/empresas/',
            param={
                "codigo_empresa": codigo_empresa
            }
        )

    def listar_empresa(self, pagina: int, registros_por_pagina: int, apenas_importado_api: bool) -> dict:
        """
           :param pagina:                              integer	Número da página que será listada.
           :param registros_por_pagina:                integer	Número de registros retornados
           :param apenas_importado_api:                bool	Exibir apenas os registros gerados pela API.
           """
        apenas_importado_api = self._bool_para_sn(apenas_importado_api)
        return self._chamar_api(
            call='ListarEmpresas',
            endpoint='geral/empresas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api
            }
        )