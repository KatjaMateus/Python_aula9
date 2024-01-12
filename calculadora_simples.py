from tkinter import *

caixa = Tk()
caixa.title("Calculadora")
caixa.geometry("300x350")

nome_label=Label(text="0", bg="blue", fg="black", width=43, height=3)
nome_label.grid(row=0, column=0, rowspan=2, columnspan=4)

botaoC = Button(caixa, text="C", width=10, height=3)
botaoC.grid(row=3, column=0, rowspan=2)

botaoerro = Button(caixa, text="⌫", width=10, height=3)
botaoerro.grid(row=3, column=1, rowspan=2)

botao_result = Button(caixa, text="=", bg="blue", width=22, height=3)
botao_result.grid(row=3, column=2, rowspan=2, columnspan = 2)

botao1 = Button(caixa, text="1", bg = "yellow", width=10, height=3)
botao1.grid(row=5, column = 0, rowspan = 2)

botao2 = Button(caixa, text="2", bg = "yellow", width=10, height=3)
botao2.grid(row=5, column=1, rowspan = 2)

botao3 = Button(caixa, text="3", bg = "yellow", width=10, height=3)
botao3.grid(row=5, column = 2, rowspan = 2)

botaoplus = Button(caixa, text="+", bg = "yellow", width=10, height=3)
botaoplus.grid(row=5, column=3, rowspan = 2)

botao4 = Button(caixa, text="4", bg = "yellow", width=10, height=3)
botao4.grid(row=7, column=0, rowspan = 2)

botao5 = Button(caixa, text="5", bg = "yellow", width=10, height=3)
botao5.grid(row=7, column=1, rowspan = 2)

botao6 = Button(caixa, text="6", bg = "yellow", width=10, height=3)
botao6.grid(row=7, column=2, rowspan = 2)

botaominus = Button(caixa, text="-", bg = "yellow", width=10, height=3)
botaominus.grid(row=7, column=3, rowspan = 2)

botao7 = Button(caixa, text="7", bg = "yellow", width=10, height=3)
botao7.grid(row=9, column=0, rowspan = 2)

botao8 = Button(caixa, text="8", bg = "yellow", width=10, height=3)
botao8.grid(row=9, column=1, rowspan = 2)

botao9 = Button(caixa, text="9", bg = "yellow", width=10, height=3)
botao9.grid(row=9, column=2, rowspan = 2)

botaomultiply = Button(caixa, text="*", bg = "yellow", width=10, height=3)
botaomultiply.grid(row=9, column=3, rowspan = 2)

botaoempty = Button(caixa, text="", bg = "yellow", width=10, height=3)
botaoempty.grid(row=11, column=0, rowspan = 2)

botao0 = Button(caixa, text="0", bg = "yellow", width=10, height=3)
botao0.grid(row=11, column=1, rowspan = 2)

botaocomma = Button(caixa, text=",", bg = "yellow", width=10, height=3)
botaocomma.grid(row=11, column=2, rowspan = 2)

botaodivide = Button(caixa, text="/", bg = "yellow", width=10, height=3)
botaodivide.grid(row=11, column=3, rowspan = 2)
caixa.mainloop()