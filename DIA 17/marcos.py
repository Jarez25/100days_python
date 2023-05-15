from tkinter import *

root = Tk()

root.title('INTERFAZ2')

marco1 = LabelFrame(root,padx=20, pady=20 ,text='este es un FRAME')
marco1.pack(padx=15, pady=15) #grid(row=0, column=0,padx=15, pady=15)

marco2 = LabelFrame(root,padx=20, pady=20 ,text='este es un FRAME')
marco2.pack(padx=15, pady=15) #grid(row=1, column=0, padx=5, pady=15)

marco3 = LabelFrame(root,padx=20, pady=20 ,text='este es un FRAME')
marco3.pack(padx=15, pady=15) #grid(row=0, column=1, padx=5, pady=15)

entrada = Entry(marco1,
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
    Label(marco3, text=f'hola {nombre}',
                background='skyblue',
                width=26,
                ).pack()
    
Button(marco2, text='enviar', # si en vez de marco fuera root sale fuera del frame
                command=send,
                background='yellow',
                foreground='black',
                border=3,
                width=25
                ).pack()

root.mainloop()