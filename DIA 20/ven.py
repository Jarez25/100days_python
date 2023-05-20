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

cordenada_x = int((an_pantalla/2)-(ancho/2))
cordenada_y = int((al_pantalla/2)-(alto/2))-37

root.geometry('{}x{}+{}+{}'.format(ancho,alto,cordenada_x, cordenada_y))

Label(text=f'pantalla ancho: {an_pantalla} pixeles').pack()
Label(text=f'pantalla ancho: {al_pantalla} pixeles').pack()

root.state('zoomed')# amplia la pantalla normal =  defaul, withdrawn = oculta la ventana se muesta con deiconify


root.mainloop() 