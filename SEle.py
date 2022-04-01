
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def OpenFileTk ():
    Tk().withdraw() # Isto torna oculto a janela principal
    filename = askopenfilename() # Isto te permite selecionar um arquivo
    print(filename) # printa o arquivo selecionado

from tkinter import filedialog as dlg
path = dlg.askopenfilename()