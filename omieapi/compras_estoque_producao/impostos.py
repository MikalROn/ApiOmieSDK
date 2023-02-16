from ..core.omiebase import OmieBase


class Impostos(OmieBase):
    """ Classe que carrega metodos de impostos """

    def listar_cfop(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar as CFOPs"""
        return self._chamar_api(
            call='ListarCFOP',
            endpoint='produtos/cfop/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_cst(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar os CSTs do ICMS"""
        return self._chamar_api(
            call='ListarCST',
            endpoint='produtos/icmscst/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_csosn(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar os CSOSN do ICMS."""
        return self._chamar_api(
            call='ListarCSOSN',
            endpoint='produtos/icmscsosn/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_orig_merc(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar a origem da mercadoria do ICMS."""
        return self._chamar_api(
            call='ListarOrigMerc',
            endpoint='produtos/icmsorigem/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_cst_pis(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar o CST do PIS."""
        return self._chamar_api(
            call='ListarCstPis',
            endpoint='produtos/piscst/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_cst_cofins(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar CST do COFINS."""
        return self._chamar_api(
            call='ListarCstCofins',
            endpoint='produtos/cofinscst/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_cst_ipi(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar CST do IPI."""
        return self._chamar_api(
            call='ListarCstIpi',
            endpoint='produtos/ipicst/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_enq_ipi(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar Enquadramento do IPI."""
        return self._chamar_api(
            call='ListarEnqIpi',
            endpoint='produtos/ipienq/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_tp_calc(
            self, pagina, registros_por_pagina
    ) -> dict:
        """"""
        return self._chamar_api(
            call='ListarTpCalc',
            endpoint='produtos/tpcalc/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )

    def listar_cest(
            self, pagina, registros_por_pagina
    ) -> dict:
        """Listar CEST."""
        return self._chamar_api(
            call='ListarCEST',
            endpoint='produtos/cest/',
            param={
                "pagina": pagina,
                "registros_por_pagina": registros_por_pagina
            }
        )