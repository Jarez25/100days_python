from tkinter import *


windows = Tk()
windows.title('Dia 11 de python')
#windows.resizable(1,0) esta es para que la ventana pueda alteral(v1, v2) su dimenciones el primer valor de manera horizontal el segundo de manera vertical

windows.iconbitmap('DIA 11/Python.ico')
#windows.geometry('650x450')# no funciona con el * ni con la X mayuscula
windows.config(bg='red') #este cambia el color de fondo
windows.config(bd=50) # borde
windows.config(relief='ridge') #tipo de bordes
#Button(text = 'XD !').pack(side = TOP)
windows.config(cursor='hand2')

My_frame = Frame() # crear un Frame
My_frame.pack() #empaqueta 
My_frame.config(bg='blue')
My_frame.config(width='450', height='350')
My_frame.config(bd=20)
My_frame.config(relief='groove')
My_frame.config(cursor='hand1')
My_frame.pack(fill=BOTH, expand=True)

windows.mainloop()