import tkinter as tk

root = tk.Tk()

root.title('Esta es una ventana de clase')

root.eval('tk::PlaceWindow . center')  # Centrar la ventana utilizando eval

l = tk.Label(root, text='')
l.pack()

b = tk.Button(root, text='Enviar', width=75)
b.pack()

root.mainloop()