from tkinter import *
import os

root = Tk()

carpeta = os.path.dirname(__file__)

img = os.path.join(carpeta, 'img')
print(img)

root.iconbitmap(os.path.join(img, 'darklork'))

#print(carpeta)

root.title('este es el dia 16')

root.mainloop()