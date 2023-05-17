from tkinter import *

root = Tk()

root.title('dia 18 de python')
opcion = IntVar()
opcion.set(2)

def update_radio(valor):
    Label(root, text=valor).pack()
    
    
Radiobutton(root, text='ROJO',variable=opcion, value=1).pack()
Radiobutton(root, text='AZUL',variable=opcion, value=2).pack()
Radiobutton(root, text='VERDE',variable=opcion, value=3).pack()
Radiobutton(root, text='AMARILLO',variable=opcion, value=4).pack()


Button_send = Button(root, text='enviar', command=lambda: update_radio(opcion.get())).pack()
  
#Label(root, text=f'{opcion.get()}').pack()

root.mainloop()

