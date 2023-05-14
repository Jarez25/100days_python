from tkinter import *
import os
from PIL import ImageTk, Image
import getpass

user_create = tuple()

while True:
    new_user = input('registra tu nuevo usuario \n')
    new_password = getpass.getpass('registra tu contrase;a \n')

    confir_user = input('confierma el valor de tu usuario \n')
    confir_pass = getpass.getpass('confirma tu contrase;a \n')
    
    if new_user != confir_user or new_password != confir_pass:
        print('los datos no conciden')
        
    else:
        user_create = (new_user, new_password)
    
    break


root = Tk()

root.title('YUGIOH GAMES')

imagen = os.path.dirname(__file__)
imagen_img = os.path.join(imagen, 'imagenes')
ruta = os.path.join(imagen_img, 'darklord')

img = ImageTk.PhotoImage(Image.open(os.path.join(ruta, 'yugioh.jpg')).resize((250, 100)))
tag = Label(image=img)
tag.pack()


Label(root, text='USER').pack()
user = Entry()
user.insert(0, 'username')
user.bind('<Button-1>', lambda v: user.delete(0, END) )
user.pack()

Label(root, text='PASSWORD').pack()
password = Entry()
password.insert(0, '***********')
password.bind('<Button-1>', lambda v: password.delete(0, END) )
password.pack()

def validar():
    obtener_usuario = user.get()
    obtener_contrasena = password.get()
    if obtener_usuario != user_create[0] or obtener_contrasena != user_create[1]:
        Label(text="Usuario o contraseña incorrectos.").pack()
    else:
        Label(text=f"Espera un momento, {user_create[0]}. El juego esta cargando...").pack()

Button(root, text='Entra', command=validar).pack()

root.mainloop()