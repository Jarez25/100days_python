import customtkinter as ctk
import os
from PIL import ImageTk, Image
from bd.base_datos import acceso_bd


carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "img")

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

class Login:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("BD")
        self.root.geometry("400x600")
        self.root.resizable(0,0)


        # Logo
        logo = ctk.CTkImage(
            light_image=(Image.open(os.path.join(carpeta_imagenes, "darklork.png"))),
            size=(250, 250)
        )
        
        #muestra la imagen
        tag = ctk.CTkLabel(master = self.root, image=logo, text = "")
        tag.pack(pady = 15)

       
        ctk.CTkLabel(self.root, text="Usuario").pack()  # Campos de texto
        self.usuario =ctk.CTkEntry(self.root)
        self.usuario.insert(0, "Jarez")
        self.usuario.bind("<Button-1>", lambda e: self.usuario.delete(0, 'end'))
        self.usuario.pack()

        
        ctk.CTkLabel(self.root, text="Contraseña").pack() # Contraseña
        self.contrasena = ctk.CTkEntry(self.root)
        self.contrasena.insert(0, "*******")
        self.contrasena.bind("<Button-1>", lambda e: self.contrasena.delete(0, 'end'))
        self.contrasena.pack()

        # Botón de envío
        ctk.CTkButton(self.root, text="Entrar", command=self.validar).pack()

        # Bucle de ejecución
        self.root.mainloop()
        #funcion para validar datos de acceso 
    def validar(self):
        obtener_usuario = self.usuario.get() # Obtenemos el nombre de usuario
        obtener_contrasena = self.contrasena.get() # Obtenemos la contraseña
        
        if obtener_usuario != acceso_bd["user"] or obtener_contrasena != acceso_bd["password"]:
            if hasattr(self, "info_login"):
                self.info_login.destroy()
            self.info_login = ctk.CTkLabel(self.root, text="Usuario o contraseña incorrectos.")
            self.info_login.pack()
        else:
            if hasattr(self, "info_login"):
                self.info_login.destroy()
            self. info_login = ctk.CTkLabel(self.root, text=f"Hola, {obtener_usuario}. Espere unos instantes...")
            self.info_login.pack()