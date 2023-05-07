from tkinter import *

root = Tk()
root.title('esta es una ventana test')
root.geometry('600x450+50+75')

mensaje = Label(root, text='este es un mensaje')
mensaje2 = Label(root, text='este es un segundo mensaje')

mensaje.grid(row=0, column=0)
mensaje2.grid(row=0, column=1)



root.mainloop()