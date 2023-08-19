import customtkinter as ctk
import os
from PIL import Image
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
            self.root.destroy()
            ventana_opciones = Ventana_opciones()

class FuncionesPrograma:
    def ventana_consultas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Consultas SQL")
        
    def ventana_mostrar_bases_datos(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Mostrar BD.")
        
    def ventana_eliminar_bases_datos(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Eliminar bases de datos")
        
    def ventana_crear_bases_datos(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Crear bases de datos")
        
    def ventana_crear_respaldos(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Crear respaldos")
        
    def ventana_crear_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Crear tablas")
    
    def ventana_eliminar_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Eliminar tablas")
        
    def ventana_mostrar_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Mostrar tablas")
        
    def ventana_mostrar_columnas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Mostrar columnas de una tabla")
        
    def ventana_insertar_registros(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Insertar registros")
        
    def ventana_eliminar_registros(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Eliminar registros")
        
    def ventana_vaciar_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Vaciar tablas")
    
    def ventana_actualizar_tablas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Actualizar tablas")
        
objeto_funciones = FuncionesPrograma()

class Ventana_opciones:
    # Diccionario para los botones
    botones = {'Consulta SQL': objeto_funciones.ventana_consultas, 
               'Mostrar Bases de Datos': objeto_funciones.ventana_mostrar_bases_datos,
               'Eliminar Bases de Datos': objeto_funciones.ventana_eliminar_bases_datos,
               'Crear Bases de Datos': objeto_funciones.ventana_crear_bases_datos, 
               'Crear Respaldos': objeto_funciones.ventana_crear_respaldos,
               'Crear Tablas': objeto_funciones.ventana_crear_tablas,
               'Eliminar Tablas': objeto_funciones.ventana_eliminar_tablas,
               'Mostrar Tablas': objeto_funciones.ventana_mostrar_tablas,
               'Mostrar Columnas': objeto_funciones.ventana_mostrar_columnas,
               'Insertar Registros': objeto_funciones.ventana_insertar_registros,
               'Eliminar Registros': objeto_funciones.ventana_eliminar_registros,
               'Vaciar Tablas': objeto_funciones.ventana_vaciar_tablas,
               'Actualizar Registros': objeto_funciones.ventana_actualizar_tablas
               }
    
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Opciones para trabajar con bases de datos.")

        #Contador para la posición de los botones
        contador = 0

        # Crea los botones y establece su texto
        for texto_boton in self.botones:
            button = ctk.CTkButton(
                master=self.root,
                text=texto_boton,
                height=25,
                width=200,
                command=self.botones[texto_boton]
            )
            button.grid(row=contador//3, column=contador%3, padx=5, pady=5)
        
            # Incrementa el contador
            contador += 1
            
        self.root.mainloop()