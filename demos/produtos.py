import pandas as pd
import PySimpleGUI as sg
from pysimpleevent import EventSimpleGUI
from .omieapi import Omie


def janela_produtos(key: str, secreet: str):
    app = EventSimpleGUI()


    produtos = Omie(key, secreet)
    lista_de_produtos = produtos.listar_produtos(
        registros=100, filtrar_pdv=True, apenas_importado_api=False,
        pagina=1
    )['produto_servico_cadastro']
    data = pd.DataFrame(lista_de_produtos)


    headings = {'aliquota_cofins': False, 'aliquota_ibpt': False,
                'aliquota_icms': False, 'aliquota_pis': False,
                'altura': False, 'bloqueado': False,
                'bloquear_exclusao': False, 'cest': False,
                'cfop': False, 'codInt_familia': False,
                'codigo': False, 'codigo_beneficio': False,
                'codigo_familia': False, 'codigo_produto': False,
                'codigo_produto_integracao': False, 'csosn_icms': False,
                'cst_cofins': False, 'cst_icms': False, 'cst_pis': False,
                'dadosIbpt': False, 'descr_detalhada': False, 'descricao': True,
                'descricao_familia': False, 'dias_crossdocking': False,
                'dias_garantia': False, 'ean': False, 'estoque_minimo': False,
                'exibir_descricao_nfe': True, 'exibir_descricao_pedido': False,
                'importado_api': False, 'inativo': False, 'info': False,
                'largura': False, 'lead_time': False, 'marca': False,
                'modalidade_icms': False, 'modelo': False,
                'motivo_deson_icms': False, 'ncm': True, 'obs_internas': False,
                'origem_imposto': False, 'per_icms_fcp': False, 'peso_bruto': False,
                'peso_liq': False, 'profundidade': False, 'quantidade_estoque': False,
                'recomendacoes_fiscais': False,
                'red_base_cofins': False, 'red_base_icms': False,
                'red_base_pis': False, 'tipoItem': True,
                'unidade': True, 'valor_unitario': True}

    tabela = sg.Table([], headings=[x for x in headings.keys()],
                      visible_column_map=[x for x in headings.values()], expand_x=True,
                          expand_y=True,  k='Tabela')



    layout = [
        [sg.Input(k='PRODUTO', enable_events=True),
         sg.Button('Buscar'), sg.Text('--->'),
         sg.Button('Selecionar', expand_x=True)],
        [tabela]
    ]


    @app.event('Buscar')
    def event_buscar_produtos(event, values, window):
        tabela.update( data.values.tolist())


    win = sg.Window('Produtos', layout, resizable=True)
    return app.run_window(win, close_event='Selecionar')




































