from tkinter import *
caixinha = Tk()
caixinha.title("Maior de idade")
caixinha.geometry("400x400")

def mostrar_idade():
    idade = 2023 - int(ano_input.get())
    if idade <= 18:
        resultado.configure(text="Resultado: Maior de idade")
    else:
        resultado.configure(text="Resultado: Menor de idade")

idade= Label(text="Digite o ano de nascimento")
idade.pack()
ano_input= Entry()
ano_input.pack()

botao = Button(caixinha, text="Enviar", command=mostrar_idade)
botao.pack()

resultado = Label(text="Resposta: ")
resultado.pack()
caixinha.mainloop()