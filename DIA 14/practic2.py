from tkinter import *

root = Tk()
entrada = Entry(root)
entrada.insert(0, 'ingresa tu nombre')

mombre = Label(root, text="Nombre: ").grid(column=0, row=0)
entrada = Entry(root)
entrada.grid(column=1, row=0)


edad = Label(root, text="Edad: ").grid(column=0, row=1)
entrada_E = Entry(root)
entrada_E.grid(column=1, row=1)

def pulsar():
    nombre = entrada.get()
    edad = entrada_E.get()
    Label(root, text=f"Mi nombre es {nombre}. Tengo {edad} años.").grid(column=1, row=3)
    
Button(root, text="Enviar", command=pulsar).grid(column=1, row=2)

root.mainloop()