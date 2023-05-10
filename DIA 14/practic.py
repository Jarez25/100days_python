from tkinter import *

root = Tk()

def crear(numero):
    Label(root, text=f'Boton {numero} pulsado').pack()

"""

def pulsar():
        Label(root, text=f'se a pulado el boton 1').pack()
        
def pulsar1():
        Label(root, text=f'se a pulado el boton 2').pack()

def pulsar2():
        Label(root, text=f'se a pulado el boton 3').pack()

def pulsar3():
        Label(root, text=f'se a pulado el boton 4').pack() 
        
"""


Button(root, text='preciona este boton 1', command=lambda: crear(1)).pack()
Button(root, text='preciona este boton 2', command=lambda: crear(2)).pack()
Button(root, text='preciona este boton 3', command=lambda: crear(3)).pack()
Button(root, text='preciona este boton 4', command=lambda: crear(4)).pack()
#Button(root, text='preciona este boton').grid(row=5, column=5)
#Button(root, text='preciona este boton').grid(row= 6, column=6)



root.mainloop()