from omieapi import OmieBase


class Produtos(OmieBase):
    """ Todos os metodos relacionados a produtos """
    def listar_produtos(
            self, registros: int, filtrar_pdv: bool, pagina: int,
            apenas_importado_api: bool
    ) -> dict:

        apenas_importado_api = self._bool_para_sn(apenas_importado_api)
        filtrar_pdv = self._bool_para_sn(filtrar_pdv)

        return self._chamar_api(
            call='ListarProdutos',
            endpoint='geral/produtos/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros,
                "apenas_importado_api": apenas_importado_api,
                "filtrar_apenas_omiepdv": filtrar_pdv
            }
        )