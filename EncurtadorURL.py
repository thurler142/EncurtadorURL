import pyshorteners
from PySimpleGUI import PySimpleGUI as sg


""" url_encurtada = pyshorteners.Shortener()

url_encurtada.tinyurl.short(url) """

sg.theme('Reddit')
layout = [
    [sg.Text('URL', auto_size_text=True), ],
    [sg.InputText(key = 'url')],
    [sg.Button('Gerar', auto_size_button = True, key='gerar')],
    [sg.InputText('', size=(45, 1), key='resultado')]
]   
window = sg.Window('Minha Janela', layout)

def Encurtar ():
    event, values = window.read()
    url = values['url']
    url_encurtada = pyshorteners.Shortener()
    url_encurtada_resultado = url_encurtada.tinyurl.short(url)
    """ sg.popup(f'URL encurtada: {url_encurtada_resultado}') """
    window['resultado'].update(url_encurtada_resultado)
Encurtar()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'gerar':
        Encurtar()
        
    
window.close()