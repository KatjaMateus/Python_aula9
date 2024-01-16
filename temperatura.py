from tkinter import *
janela = Tk()
janela.title("Conversor de temperatura")
janela.geometry("350x350")

def calcular_celsius():
    fahrenheit = float(entryF.get())
    celsius = (fahrenheit-32)/1.8
    resultadoF.configure(text=f"A temperatura em Celsius é {celsius:.1f}")
    # print(f"A temperatura em Celsius é {celsius:.1f}.")
    

def calcular_fahrenheit():
    celsius = float(entryC.get())
    fahrenheit = celsius*1.8+32
    resultadoC.configure(text=f"A temperatura em Fahrenheit é {fahrenheit:.1f}")
    # print(f"A temperatura em Fahrenheit é {fahrenheit:.1f}.")

labelF = Label(text="Fahrenheits")
labelF.pack()
entryF = Entry()
entryF.pack()

botaoF = Button(janela, text="Converter", command=calcular_celsius)
botaoF.pack()

resultadoF = Label(text="")
resultadoF.pack()

labelC = Label(text="Celsius")
labelC.pack()
entryC = Entry()
entryC.pack()

botaoC = Button(janela, text="Converter", command=calcular_fahrenheit)
botaoC.pack()

resultadoC = Label(text="")
resultadoC.pack()
janela.mainloop()
