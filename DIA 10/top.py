from tkinter import *

root = Tk()
root.title('ventana primaria')
Label1 = Label(root, text='esta es mi ventana primarial')

top1 = Toplevel(root)
top1.title('esta es la ventana secundaria')
label2 = Label(top1, text='Esta es mi ventana principla')

Button(root, text='hola a todos').pack()
Button(root, text='este es un boton').pack()
Label(root, text='esta es una intefaz con tkinter').pack()
label2.pack()


top2 = Toplevel(root)
top2.title('tansitoria')
label3 = Label(top2, text='esta es una ventana de tranciosionde la principal')
top2.transient()


top3 = Toplevel(root)
label4 = Label(top3, text='una tercera ventana')
label4.pack()
top3.overrideredirect(1)
top3.geometry('100x70+0+150')

root.mainloop()