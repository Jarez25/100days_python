from tkinter import *
from tkinter.messagebox import *

root = Tk()

root.title('esta es una ventana de clase')

def error():
    showerror('esta es una alerta', 'hola')

b = Button(root, text='Enviar', width=75, command=error).pack()

root.mainloop()