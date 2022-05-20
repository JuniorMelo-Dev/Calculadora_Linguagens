from tkinter import *
from tkinter import ttk

#Cores
cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#37474F"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

#Criando janela principal
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x289")
janela.config(bg = cor1)

#Criando frames
frame_tela = Frame(janela, width = 300, height = 56, bg = cor3)
frame_tela.grid(row = 0, column = 0)

frame_cientifica = Frame(janela, width = 300, height = 86)
frame_cientifica.grid(row = 1, column = 0) 

frame_corpo = Frame(janela, width = 300, height = 340)
frame_corpo.grid(row = 2, column = 0)

#Configurando o frame_tela
label_tela = Label(janela, width = 16, height = 2, text = 'Teste', padx = 7, anchor = 'e', bd = 0, justify = RIGHT, font = ('Ivy 18'), bg = cor3, fg = cor2)
label_tela.place(x=0, y=0)


janela.mainloop()