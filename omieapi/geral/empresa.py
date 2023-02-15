from omieapi.omiebase import OmieBase


class Empresa(OmieBase):

    def consultar_empresa(
            self, codigo_empresa
    ) -> dict:
        """Realiza a consulta de um registro especifico"""
        return self._chamar_api(
            call='ConsultarEmpresa',
            endpoint='geral/empresas/',
            param={
                "codigo_empresa": codigo_empresa,

            }
        )

    def listar_empresas(
            self, pagina, registros_por_pagina, apenas_importado_api
    ) -> dict:
        """Lista as empresas cadastradas no Omie."""
        return self._chamar_api(
            call='ListarEmpresas',
            endpoint='geral/empresas/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina,
                "apenas_importado_api": apenas_importado_api
            }
        )

    def consultar_departamento(
            self, codigo
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ConsultarDepartamento',
            endpoint='geral/departamentos/',
            param={
                "codigo": codigo
            }
        )

    def listar_depatartamentos(
            self, pagina, registros_por_pagina
    ) -> dict:
        """DEPRECATED"""
        return self._chamar_api(
            call='ListarDepatartamentos',
            endpoint='geral/departamentos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

