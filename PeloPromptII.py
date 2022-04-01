from pytube import YouTube, streams
from PySimpleGUI import PySimpleGUI as sg

#Função Baixar
def BaixarLinkYouT():
    #url = input('Link para baixar: ')
    #local = input('Digite aonde deseja salvar o video: ')
    video = YouTube(url)

    stream = video.streams.get_highest_resolution()
    stream.download(local)

    print('Download concluido com sucesso!')

#Layout
    sg.theme('Reddit')
    layout = [
        [sg.Text('YouTube Baixador')],
        [sg.Text('Link para baixar: '), sg.Input(key='LinkBaixar')],
        [sg.Button('Download'), sg.Input(key='BaixarLinkYouT')]
    ]
#janela
    janela = sg.Window('Tela de Download', layout)
#Ler Eventos
    while True:
        linkDown = janela.read()
        if janela == sg.WIN_CLOSED:
            break

import os

