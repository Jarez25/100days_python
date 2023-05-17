from tkinter import *
import os
from PIL import Image, ImageTk

root = Tk()
root.title('SELECIONA UN DECK')

select_deck = StringVar()
select_deck.set("Error")

imagen = os.path.dirname(__file__)
imagen_img = os.path.join(imagen, 'img')

root.config(background='blue')

mar_user = LabelFrame(root,
                      text="Selecciona tu deck:",
                      padx=10,
                      pady=10,
                      background='white',
                      border=0)
mar_user.pack(padx=10, pady=10)

user1 = ImageTk.PhotoImage(Image.open(os.path.join(imagen_img, 'aromage.jpg')).resize((200, 200)))
tag = Label(mar_user, image=user1)
tag.grid(row=0, column=0)

user2 = ImageTk.PhotoImage(Image.open(os.path.join(imagen_img, 'primer.webp')).resize((200, 200)))
tag2 = Label(mar_user, image=user2)
tag2.grid(row=2, column=0)

user3 = ImageTk.PhotoImage(Image.open(os.path.join(imagen_img, 'fantastruco.webp')).resize((200, 200)))
tag3 = Label(mar_user, image=user3)
tag3.grid(row=0, column=1)

user4 = ImageTk.PhotoImage(Image.open(os.path.join(imagen_img, 'labrislinto.webp')).resize((200, 200)))
tag4 = Label(mar_user, image=user4)
tag4.grid(row=2, column=1)


def update_radio():
    if select_deck.get() == 'Error':
        Label(root, text='Selecciona un deck, o de lo contrario irás al reino de las sombras',
              background='yellow',
              foreground='red').pack()
    else:
        Label(root, text=f'Toma tu deck {select_deck.get()}',
              background='red').pack()


Radiobutton(mar_user, text='AROMAGE',
            variable=select_deck, value='AROMAGE', background='green',
            command=update_radio).grid(row=1, column=0)
Radiobutton(mar_user, text='DARKLORD',
            variable=select_deck, value='DARKLORD', background='purple',
            command=update_radio).grid(row=3, column=0)
Radiobutton(mar_user, text='GHOSTRIC',
            variable=select_deck, value='GHOSTRIC', background='pink',
            command=update_radio).grid(row=1, column=1)
Radiobutton(mar_user, text='LABRYNTH',
            variable=select_deck, value='LABRYNTH', background='skyblue',
            command=update_radio).grid(row=3, column=1)




boton = Button(root, text='Enviar', command= update_radio)
boton.pack()

root.mainloop()
