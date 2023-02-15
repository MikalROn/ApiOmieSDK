from omieapi.omiebase import OmieBase


class Categorias(OmieBase):
    """"""

    def consultar_categoria(
            self, codigo
    ) -> dict:
        """ Consulta uma categoria """
        return self._chamar_api(
            call='ConsultarCategoria',
            endpoint='geral/categorias/',
            param={
                "codigo": codigo
            }
        )

    def listar_categorias(
            self, pagina, registros_por_pagina
    ) -> dict:
        """ Lista as categorias cadastradas """
        return self._chamar_api(
            call='ListarCategorias',
            endpoint='geral/categorias/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )