from PySimpleGUI import Window, Text, Input, Button, Multiline, Push, Column, popup_error
from pysimpleevent import EventSimpleGUI
from produtos import janela_produtos

eventos = EventSimpleGUI()


layout = [
    [Column([
        [Text('Nome'), Push(), Text('Valor'), Push(), Push()],
        [Text('OMIE_APP_KEY', s=(20, 0), expand_x=True), Push(), Input(k='-OMIE_APP_KEY-', expand_x=True)],
        [Text('OMIE_APP_SECRET', s=(20, 0), expand_x=True), Push(), Input(k='-OMIE_APP_SECRET-', expand_x=True)],

        [Push(), Button('Executar', button_color='Blue')]
    ])
    ]
]


@eventos.event('Executar')
def event_buscar(event, values, window: Window):
    """ Evento de Executar , abre janela de produtos """
    try:
        janela_produtos(
        values['-OMIE_APP_KEY-'],
        values['-OMIE_APP_SECRET-']
        )
    except Exception as erro:
        popup_error(erro)


# iniciar janela
janela = Window('Teste metodos API', layout)


if __name__ == '__main__':
    eventos.run_window(janela)
