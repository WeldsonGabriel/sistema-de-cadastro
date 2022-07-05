#criar interface 
from PySimpleGUI import PySimpleGUI as sg
#layout (tema SystemDefault1).
sg.theme ('SystemDefault')
layout = [
    [sg.Text('usuario')],
    [sg.Input(Key='usuario')],
    [sg.Text('senha')],
    [sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('salvar o login ?')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('tela de login', layout)
#eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar' : 
        if valores['usuario'] == 'Gabriel' and valores['senha'] == '123456':
            print('')
