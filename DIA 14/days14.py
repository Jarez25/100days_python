from tkinter import *


root = Tk()

entrada = Entry(root)
entrada.insert(0, 'ingresa tu nombre')
entrada.bind('<Button-1>', lambda e : entrada.delete(0, END)) #delete borra los elementos que hay en la entrada
entrada.pack()                                                 # el BackSpace solo es con el espacio y con el key es cualquier tecla

root.title("Please, Don't Touch Anything")

def pulsar():
    nombre = entrada.get()
    Label(root, text=f'{nombre}').pack()

b = Button(root, text='Enviar', command=pulsar).pack()

root.mainloop()