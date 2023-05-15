from tkinter import *

root = Tk()

root.title('INTERFAZ')

entrada = Entry(root, background='green', border=5, foreground='blue', width=30)
entrada.pack()

def send():
    Label(root, text='se a pulsado un boton',
                background='skyblue',
                width=26).pack()

    
b = Button(root, text='enviar', 
                command=send,
                background='yellow',
                foreground='black',
                border=3,
                width=25
                ).pack()


root.mainloop()