import tkinter as tk
import os
from PIL import ImageTk, Image


carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "img")
print(carpeta_imagenes)

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BD")
        self.root.geometry("500x650")


        # Logo
        logo = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_imagenes, "darklork.png")))
        tk.Label(self.root, image=logo).pack()

       
        tk.Label(self.root, text="Usuario").pack()  # Campos de texto
        self.usuario = tk.Entry(self.root)
        self.usuario.insert(0, "Jarez")
        self.usuario.bind("<Button-1>", lambda e: self.usuario.delete(0, tk.END))
        self.usuario.pack()

        
        tk.Label(self.root, text="Contraseña").pack() # Contraseña
        self.contrasena = tk.Entry(self.root)
        self.contrasena.insert(0, "*******")
        self.contrasena.bind("<Button-1>", lambda e: self.contrasena.delete(0, tk.END))
        self.contrasena.pack()

        # Botón de envío
        tk.Button(self.root, text="Entrar").pack()

        # Bucle de ejecución
        self.root.mainloop()