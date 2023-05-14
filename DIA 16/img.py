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
img = ImageTk.PhotoImage(Image.open(os.path.join(darklord, 'Eatos.png')).resize((350, 350)))
tag = Label(image=img)
tag.grid(row=0, column=0)

img2 = ImageTk.PhotoImage(Image.open(os.path.join(darklord, 'DarklordI.png')).resize((350, 350)))
tag = Label(image=img2)
tag.grid(row=1, column=0)

img3 = ImageTk.PhotoImage(Image.open(os.path.join(darklord, '21200905.jpg')).resize((350, 350)))
tag = Label(image=img3)
tag.grid(row=0, column=1)

img4 = ImageTk.PhotoImage(Image.open(os.path.join(darklord, 'Regreso.jpg')).resize((350, 350)))
tag = Label(image=img4)
tag.grid(row=1, column=1)

root.mainloop() 