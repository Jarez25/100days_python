import mysql.connector
import os
import subprocess
import datetime

# conexión con la base de datos
acceso_bd = {"host": "localhost",
             "user": "root",
             "password": "251115",
             }

# Rutas

# Obtenemos la raíz de la carpeta del proyecto
carpeta_principal = os.path.dirname(__file__)

carpeta_respaldo = os.path.join(carpeta_principal, "respaldo")


class BaseDatos:
    # Conexión y cursor
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)
        self.cursor = self.conector.cursor()
        self.contrasena = kwargs["password"]

    # Decoradora para el reporte de bases de datos en el servidor
    def reporte_bd(funcion_parametro):
        def interno(self, nombre_db):
            funcion_parametro(self, nombre_db)
            print("Estas son las bases de datos que tiene el servidor:")
            BaseDatos.mostrar_bd(self)

        return interno

    # Consultas SQL
    def consulta(self, sql):
        self.cursor.execute(sql)
        return self.cursor

    # Mostrar bases de datos
    def mostrar_bd(self):
        self.cursor.execute("SHOW DATABASES")
        for bd in self.cursor:
            print(bd)

    # Eliminar bases de datos
    @reporte_bd
    def eliminar_bd(self, nombre_bd):
        try:
            self.cursor.execute(f"DROP DATABASE {nombre_bd}")
            print(f"Se eliminó la base de datos {nombre_bd} correctamente.")
        except:
            print(f"Base de datos '{nombre_bd}' no encontrada.")

    # Crear bases de datos
    @reporte_bd
    def crear_bd(self, nombre_bd):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_bd}")
            print(f"Se creó la base de datos {nombre_bd} o ya estaba creada.")
        except:
            print(f"Ocurrió un error al intentar crear la base de datos {nombre_bd}.")

    # Crear backups de bases de datos
    def copiar_bd(self, nombre_bd):
        # Obtiene la hora y fecha actuales
        self.fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        # Se crea la copia de seguridad
        with open(f'{carpeta_respaldo}/{nombre_bd}_{self.fecha_hora}.sql', 'w') as out:
            subprocess.Popen(
                f'"C:/Program Files/MySQL/MySQL Workbench 8.0/"mysqldump --user=root --	password={self.contrasena} --databases {nombre_bd}',
                shell=True, stdout=out)

    def crear_tabla(self, nombre_bd, nombre_tabla, columnas):
        # String para guardar el string con las columnas y tipos de datos
        columnas_string = ""
        for columna in columnas:
            # Formamos el string con nombre, tipo y longitud
            columnas_string += f"{columna['name']} {columna['type']}({columna['length']})"
            if columna['primary_key']:
                columnas_string += " PRIMARY KEY"
            if columna['auto_increment']:
                columnas_string += " AUTO_INCREMENT"
            if columna['not_null']:
                columnas_string += " NOT NULL"
            columnas_string += ",\n"
        columnas_string = columnas_string[:-2]
        self.cursor.execute(f"USE {nombre_bd}")
        sql = f"CREATE TABLE {nombre_tabla} ({columnas_string})"
        self.cursor.execute(sql)
        self.conector.commit()


bd = BaseDatos(**acceso_bd)

# Definir el nombre de la base de datos y el nombre de la tabla
nombre_bd = "datos"
nombre_tabla = "usuario"

# Definir la estructura de las columnas
columnas = [
    {
        "name": "id",
        "type": "INT",
        "length": 11,
        "primary_key": True,
        "auto_increment": True,
        "not_null": True
    },
    {
        "name": "nombre",
        "type": "VARCHAR",
        "length": 50,
        "primary_key": False,
        "auto_increment": False,
        "not_null": True
    },
    {
        "name": "edad",
        "type": "INT",
        "length": 3,
        "primary_key": False,
        "auto_increment": False,
        "not_null": True
    }
]

# Llamar a la función crear_tabla
bd.crear_tabla(nombre_bd, nombre_tabla, columnas)
