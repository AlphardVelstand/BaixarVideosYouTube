from tkinter import *
from tkinter import messagebox, filedialog

import pytube
from pytube import *
from tkinter import filedialog as dlg

#Definindo uma variavel global
video = str(YouTube)
#video = ''

# Função para baixar o video
def BaixarLinkYouT():
    global video
    if  video !='':
        video = YouTube(str(texto_input.get()))

        local = dlg.askdirectory()  # chamando metodo que abre a janela para selecionar aonde o video sera salvo
        stream = video.streams.get_highest_resolution()

        # Mensagem de iniciando o download
        messagebox.showinfo("Baixador YouTube", "Iniciando o Download")
        stream.download(local)

        text = f'''Download concluido com sucesso!'''

        texto_DownConcluido["text"] = text

        # Mensagem de download concluido
        messagebox.showinfo("CONCLUIDO", "ARQUIVO BAIXADO E SALVO NA PASTA: \n " + local)

    else:
            messagebox.showinfo("ERRO", "Campo URL nao pode estar vazio")


# messagebox.showinfo("ERRO", "CAMPO URL DO VIDEO EM BRANCO!)
# Função para fechar o programa quando clicar no botao sair
def fechar_janela():
    janela.destroy()


# Validando se o campo video nao esta vazio
def ValidarCampoVideo():
    if video != '':
        BaixarLinkYouT()
    else:
        messagebox.showinfo("ERRO", "Campo URL nao pode estar vazio")


# Criando a janela TK
janela = Tk()
# Titulo
janela.title("Baixador YouTube")
janela.geometry("250x300")
# Label1
texto_orientacao1 = Label(janela, text="Insira a URL do video que deseja baixar")
# texto_orientacao1.place(relx = 0.5, rely = 0.5, anchor = 'sw')
texto_orientacao1.grid(column=0, row=0, padx=10, pady=10)

# Inserindo a URL do Video
texto_input = Entry(janela)
texto_input.grid(column=0, row=2, padx=10, pady=10)
texto_input["width"] = 30

# Label 2
texto_DownConcluido = Label(janela, text="", foreground='blue')
texto_DownConcluido.grid(column=0, row=3, padx=10, pady=10)

texto_orientacao3 = Label(janela, text="Clique no botão para baixar")
texto_orientacao3.grid(column=0, row=6, padx=10, pady=10)

# Texto copyright
textoCopyright = Label(janela, text="Desenvolvido por Alphard")
textoCopyright.place(relx=0.0, rely=1.0, anchor='sw')

# Botao que chama a função e baixa o video
# botao = Button(janela, text="Baixar Video", command=ValidarCampoVideo)
botao = Button(janela, text="Baixar Video", command=BaixarLinkYouT)
botao.grid(column=0, row=7, padx=10, pady=10)
botao["width"] = 20

# Botao SAIR
botaoSair = Button(janela, text="Sair", command=fechar_janela)
botaoSair.grid(column=0, row=8, padx=10, pady=10)
botaoSair["width"] = 20

# print("Baixando...")

# Mantendo jannela aberta
janela.mainloop()
