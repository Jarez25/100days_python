from tkinter import *

root = Tk()
root.title('programa de python')
root.geometry('800x600+560+240')
mensaje = Label(root, text='este es un msj con variable')
mensaje2 = Label(root, text='esta es otra variable')
mensaje_grid = Label(root, text='este es un grid')
columna_fantasma = Label(root, text='esta es una columna de prueba')
#Label(root, text='Mi primer label').pack()
#mensaje.pack() esta me dan error por ocupar el gometria del grid o seso fue lo que entendi
mensaje.grid(row=1, column=0) #row es fila y column por logica es columnda
mensaje2.grid(row=0, column=1)
mensaje_grid.grid(row=0, column=0)
columna_fantasma.grid(row=1, column=10) #podria decir que no es que ella sea la fantasma las fantasmas serian las demas columnas que no muestras
                                        #las columnas asi toman la posicion de la columna siguente en este caso ella seria la columna 2 auque.
                                        #en el grid sea la columna 10

total = Label(root, text='esta es otra manera de usar grid').grid(row=2, column=3)


root.mainloop()