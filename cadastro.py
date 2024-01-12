from tkinter import *
janela = Tk()

janela.title("Cadastro de alunos")
janela.geometry("400x400")

def mostrar_cadastro():
    print(f"Nome:{nome_entry.get()}")
    print(f"Idade: {idade_entry.get()}")
    print(f"Nota: {nota_entry.get()}")

nome_label=Label(text="Nome")
nome_label.pack()
nome_entry=Entry()
nome_entry.pack()

idade_label=Label(text="Idade")
idade_label.pack()
idade_entry=Entry()
idade_entry.pack()

nota_label=Label(text="Nota")
nota_label.pack()
nota_entry=Entry()
nota_entry.pack()

botao=Button(janela, text="Cadastrar", command=mostrar_cadastro)
botao.pack()

janela.mainloop()
