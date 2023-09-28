from bd.base_datos import BaseDatos
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from tkinter.font import BOLD
import os
from PIL import Image
import bd.base_datos as sqlbd

carpeta_principal = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_principal, "img")

ctk.set_appearance_mode('System')
ctk.set_default_color_theme('blue')

    #fuentes  
fuente = ('Releway', 16, BOLD)

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
        
        if obtener_usuario != sqlbd.acceso_bd["user"] or obtener_contrasena != sqlbd.acceso_bd["password"]:
            if hasattr(self, "info_login"):
                self.info_login.destroy()
            self.info_login = ctk.CTkLabel(self.root, text="Usuario o contraseña incorrectos.")
            self.info_login.pack()
        else:
            if hasattr(self, "info_login"):
                self.info_login = ctk.CTkLabel(self.root, text="Usuario o contraseña incorrectos.")
            else:
                self. info_login = ctk.CTkLabel(self.root, text=f"Hola, {obtener_usuario}. Espere unos instantes...")
                self.info_login.pack()
                self.root.destroy()
                
                ventana_opciones = Ventana_opciones()

class FuncionesPrograma:
    def ventana_consultas(self):
        ventana = ctk.CTkToplevel()
        ventana.title("Consultas SQL")
        ventana.grab_set()

            #frame
        marco = ctk.CTkFrame(ventana)
        marco.pack(padx=10, pady=10)

        #entry para las consiltas
        self.entrada = ctk.CTkEntry(marco, width=300)
        self.entrada.configure(font = fuente)
        self.entrada.grid(row=0, column=0)

        #obtener logica del metodo de consultar base de datos

        def procesar_datos():
            try:
                self.texto.delete('1.0', 'end')
                # obtiene el contenido del entry
                datos = self.entrada.get()
                # llama al método base_datos.consulta() con los datos como argumento
                resultado = BaseDatos.consulta(datos)
                for registro in resultado:
                    self.texto.insert('end', registro)
                    self.texto.insert('end', '\n')
                # Actualiza el contador de registros devueltos
                numero_registros = len(resultado)
                self.contador_registros.configure(text=f"Registros devueltos: {numero_registros}")
            except AttributeError:
                self.contador_registros.configure(text=f"Hay un error en tu consulta SQL. Por favor, revísela.")
                CTkMessagebox(title="Error", message="¡Hay un error en tu consulta SQL! Por favor, revísela.", icon="cancel")
        #boton de enviar

        boton_enviar = ctk.CTkButton(marco, text="Enviar", command=lambda :  procesar_datos)
        boton_enviar.grid(row=0, column = 1)

        #boton Limpiar
        boton_borrar = ctk.CTkButton(marco, text="Borrar", command=self.limpiar_texto)
        boton_borrar.grid(row=0, column=2)

        self.texto = ctk.CTkTextbox(marco, width=600, height=300)
        self.texto.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.contador_registro = ctk.CTkLabel(marco, text="Esperando una intruccion")
        self.contador_registro.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def limpiar_texto(self):
        self.texto.delete('1.0', 'end')
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
