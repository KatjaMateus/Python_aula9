from tkinter import *

caixinha = Tk()
caixinha.title("Aula 1 TKinter")
caixinha.geometry("400x400")

def mostrar_nome():
    print(nome_input.get())

nome = Label(text="Digite seu nome", background="#f4acb7", foreground="#9d8189") #paleta de cores css, Coolors
nome.pack()         #.pack faz o nome aparecer

nome_input = Entry()        #cria caixinha para preencher 
nome_input.pack()

botao = Button(caixinha, text="Enviar", command=mostrar_nome)
botao.pack()
caixinha.mainloop()