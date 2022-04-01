from pytube import YouTube, streams
import os

#Variavel URL
url = input(str('Link para baixar: '))
video = YouTube(url)
stream = video.streams.get_highest_resolution()

#stream.download(output_path=os.path.join(os.path.expanduser("~"), "Downloads")

stream.download(output_path='C:/Users/jhonathan.sistema/Desktop')

#std_download_path = str(os.path.join(os.path.expanduser("~"), "Downloads"))

print('Download concluido com sucesso!')