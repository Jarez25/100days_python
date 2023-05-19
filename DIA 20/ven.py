from tkinter import *
from tkinter.messagebox import *

root = Tk()

root.title('esta es una ventana de clase')

root.resizable(0, 0) # funciona tambien con true y false
ancho = 500
alto = 400

#panatlla
an_pantalla = root.winfo_screenmmwidth()
al_pantalla = root.winfo_screenheight()

root.mainloop()