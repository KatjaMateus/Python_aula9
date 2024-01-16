from tkinter import *

janela = Tk()
janela.title("Conversor")
janela.geometry("250x250")

def calcular_metro():
    metro = float(entrycm.get())/100
    resultado.configure(text=f"{entrycm.get()} cm = {metro:.1f} metros", bg="#780000", fg="white")

label = Label(text="Digite a medida em centimetros")
label.pack()

entrycm = Entry(width=8)
entrycm.pack()

botao = Button(janela, text="Converter", command=calcular_metro)
botao.pack()

resultado = Label(text="", )
resultado.pack()

janela.mainloop()