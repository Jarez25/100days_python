from tkinter import *
import os
from PIL import ImageTk, ImageColor, Image

root = Tk()


#ruta de las carpetas donde estas las imagenes
imagen = os.path.dirname(__file__)
imagen_img = os.path.join(imagen, 'imagenes')
darklord = os.path.join(imagen_img, 'darklord')

#HEAD de interfaz esta el logo como el titulo de la ventana
root.title('este es el dia 6')
root.iconbitmap(os.path.join(imagen_img, 'the_first.ico'))

#carga la imagen
img = ImageTk.PhotoImage(Image.open(os.path.join(darklord, 'darklord.jpg')).resize((1000, 650)))

tag = Label(image=img)
tag.pack()



root.mainloop() 