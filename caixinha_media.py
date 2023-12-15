from tkinter import *
caixinha = Tk()
caixinha.title("Média de notas")
caixinha.geometry("400x400")

def calcular_media():
    primeira_nota = float(nota1_input.get())
    segunda_nota = float(nota2_input.get())
    media = (primeira_nota + segunda_nota)/2
    if media >=7:
        resultado.configure(text="Aprovado", bg = "green")
    else:
        resultado.configure(text="Reprovado", bg = "red")



nota1_label= Label(text="Digite a primeira nota")
nota1_label.pack()
nota1_input= Entry()
nota1_input.pack()

nota2_label= Label(text="Digite a segunda nota")
nota2_label.pack()
nota2_input= Entry()
nota2_input.pack()

botao = Button(caixinha, text="Calcular a média", command=calcular_media)
botao.pack()


resultado = Label(text="")
resultado.pack()

caixinha.mainloop()