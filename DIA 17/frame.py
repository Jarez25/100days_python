from tkinter import *

root = Tk()

root.title('INTERFAZ2')

marco = LabelFrame(root,padx=20, pady=20 ,text='este es un FRAME')
marco.pack(padx=15, pady=15)

entrada = Entry(marco,
                background='yellow',
                border=5,
                foreground='red',
                width=30
                )

entrada.pack()
entrada.insert(0, "escribe tu nombre")
entrada.bind('<Button-1>', lambda v: entrada.delete(0, END))

def send():
    nombre = entrada.get()
    Label(root, text=f'hola {nombre}',
                background='skyblue',
                width=26,
                ).pack()
    
Button(marco, text='enviar', # si en vez de marco fuera root sale fuera del frame
                command=send,
                background='yellow',
                foreground='black',
                border=3,
                width=25
                ).pack()

root.mainloop()