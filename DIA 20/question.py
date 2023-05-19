from tkinter import *
from tkinter.messagebox import *

root = Tk()

root.title('esta es una ventana de clase')

'''def pregunta(): esta da una ventana de si o no
    askquestion('aceptas el virus', 'hola')
'''    
def pregunta():
    askokcancel('aceptas el virus', 'hola')    
    
'''def pregunta(): es igual que es askquestion
    askyesno('aceptas el virus', 'hola')
'''
b = Button(root, text='Enviar', width=75, command=pregunta).pack()

root.mainloop()