import tkinter as tk
root = tk.Tk()

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, bg="red")
entry.pack()

text= tk.Text(root, height=5, width=30, bg="yellow")
text.pack(padx=5, pady=10)
text.insert(tk.END, "Este é um exemplo")

frame=tk.Frame(root, relief=tk.RAISED, borderwidth=10)
frame.pack()

canvas= tk.Canvas(root, width=200, height=100)
canvas.pack(side="left", padx=10)

canvas.create_rectangle(10, 10, 100, 60, fill="blue")

check_var= tk.BooleanVar()
checkbutton=tk.Checkbutton(root, text="Aceitar termos", variable=check_var)
checkbutton.pack()

radio_var= tk.StringVar()

radio1=tk.Radiobutton(root, text="Opção 1", variable=radio_var, value="opcao1")
radio2=tk.Radiobutton(root, text="Opção 2", variable=radio_var, value="opcao2")
radio1.pack()
radio2.pack()

scale_var=tk.DoubleVar()
scale=tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, variable=scale_var)
scale.pack(side="right")

menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)
menu.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="Abrir")
file_menu.add_command(label="Salvar")
file_menu.add_separator()
file_menu.add_command(label="Sair")
root.mainloop()