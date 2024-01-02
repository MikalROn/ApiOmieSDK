from PySimpleGUI import Window, Text, Input, Button, Multiline, Push, Column, popup_error
from pysimpleevent import EventSimpleGUI
from omieapi import Omie
import ast

eventos = EventSimpleGUI()


layout = [
    [Column([
        [Text('Endpoint')],
        [Input(k='-ENDPOINT-', expand_x=True)],
        [Text('Nome'), Push(), Text('Valor'), Push(), Push()],
        [Text('OMIE_APP_KEY', s=(20, 0), expand_x=True), Push(), Input(k='-OMIE_APP_KEY-', expand_x=True)],
        [Text('OMIE_APP_SECRET', s=(20, 0), expand_x=True), Push(), Input(k='-OMIE_APP_SECRET-', expand_x=True)],
        [Text('OMIE_CALL', s=(20, 0), expand_x=True), Push(), Input(k='-OMIE_CALL-', expand_x=True)],

        [Text('Conteúdo')],
        [Multiline(k='-CONTEUDO-', expand_x=True, size=(10, 25))],
        [Push(), Button('Executar', button_color='green')]
    ]),
    Column([
        [Multiline(k='RESPOSTA', size=(50, 25), expand_y=True)]
    ], expand_x=True, expand_y=True)
    ]
]


@eventos.event('Executar')
def event_buscar(event, values, window: Window):
    try:
        omie = Omie(
            values['-OMIE_APP_KEY-'],
            values['-OMIE_APP_SECRET-']
        )
        r = omie.conectar_api(
            values['-OMIE_CALL-'],
            values['-ENDPOINT-'].replace('https://app.omie.com.br/api/v1/', ''),
            ast.literal_eval(values['-CONTEUDO-'])
        )
        window.find_element('RESPOSTA').update(r)
    except Exception as erro:
        popup_error(erro)


janela = Window('Teste metodos API', layout)
eventos.run_window(janela)