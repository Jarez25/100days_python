import mysql.connector
import os
import subprocess
import datetime

# conexión con la base de datos
acceso_bd = {
    "host": "localhost",
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
        self.host = kwargs['host']
        self.usuario = kwargs['user']
        self.contrasena = kwargs["password"]
        self.conexion_cerrada = False

    # Decoradora para el reporte de bases de datos en el servidor
    def reporte_bd(funcion_parametro):
        def interno(self, nombre_db):
            funcion_parametro(self, nombre_db)
            print("Estas son las bases de datos que tiene el servidor:")
            BaseDatos.mostrar_bd(self)

        return interno
    
    @reporte_bd
    def eliminar_bd(self, nombre_bd):
        try:
            self.cursor.execute(f"DROP DATABASE {nombre_bd}")
            print(f"Se eliminó la base de datos {nombre_bd} correctamente.")
        except:
            print(f"Base de datos '{nombre_bd}' no encontrada.")
        finally:
            # Cierra el cursor y la conexión
            self.cursor.close()
            self.conector.close()
            
    def conexion(funcion_parametro):
        def interno(self, *args, **kwargs):
            try:
                if self.conexion_cerrada:
                    self.conector = mysql.connector.connect(
                        host = self.host,
                        user = self.usuario,
                        password = self.contrasena
                    )
                # Se llama a la función externa
                funcion_parametro(self, *args, **kwargs)
            except:
              	# Se informa de un error en la llamada
                print("Ocurrió un error.")
            finally:
                if self.conexion_cerrada == True:
                    pass
                else:
                    self.cursor.close()
                    self.conector.close()
                    print("Se cerró la conexión con el servidor.")
                    self.conexion_cerrada = True
        return interno

    # Consultas SQL
    def consulta(self, sql):
        try:
            self.cursor.execute(sql)
            print('esta es la salida de la intrucions')
            print(self.cursor.fetchmany(10))
        except:
            print('Ocurrio un error. Revisa la intruccion SQL.')
            
    # Mostrar bases de datos
    @conexion
    def mostrar_bd(self):
        try:
            # Se informa de que se están obteniendo las bases de datos
            print("Aquí tienes el listado de las bases de datos del servidor:")
            # Realiza la consulta para mostrar las bases de datos
            self.cursor.execute("SHOW DATABASES")
            resultado = self.cursor.fetchall()
            # Recorre los resultados y los muestra por pantalla
            for bd in resultado:
                print(bd)
        except:
            # Si ocurre una excepción, se avisa en la consola
            print("No se pudieron obtener las bases de datos. Comprueba la conexión con el servidor.")

    # Eliminar bases de datos
    @conexion
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

    # Crear tabla
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

    # Eliminar tabla
    def eliminar_tabla(self, nombre_bd, nombre_tabla):
        try:
            self.cursor.execute(f"USE {nombre_bd}")
            self.cursor.execute(f"DROP TABLE {nombre_tabla}")
            print(
                f"Se eliminó la tabla {nombre_tabla} de la base de datos {nombre_bd} correctamente."
            )
        except:
            print(
                f"Ocurrió un error al intentar eliminar la tabla {nombre_tabla} de la base de datos {nombre_bd}."
            )

    @conexion
    def mostrar_tablas(self, nombre_bd):
        sql = f"SHOW DATABASES LIKE '{nombre_bd}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        if not resultado:
            print(f'La base de datos {nombre_bd} no existe.')
            return
        self.cursor.execute(f"USE {nombre_bd};")
        try:
            self.cursor.execute("SHOW TABLES")
            resultado = self.cursor.fetchall()
            
            print(f'esta es una lista de las tablas {nombre_tabla}')
            for tabla in resultado:
                null = 'no admite valores nulos' if columnas[2] == 'NO' else "Admite valores nulos"
                primeryKey = 'es una clave primaria' if columnas[3] == 'PRI' else ''
                foreingKey = 'es una clave foranea' if columnas[3] == 'MUL'  else ''
                print(f'-{columnas[0]} ({columnas[1]}) {null} {primeryKey} {foreingKey}')
        except:
            print('Ocurrio un error, comprueba el nombre de la tabla')

bd = BaseDatos(**acceso_bd)

nombre_bd = "datos"
nombre_tabla = "user"

# Definir la estructura de las columnas
columnas = [
    {
        "name": "id",
        "type": "INT",
        "length": 11,
        "primary_key": True,
        "auto_increment": True,
        "not_null": True,
    },
    {
        "name": "nombre",
        "type": "VARCHAR",
        "length": 50,
        "primary_key": False,
        "auto_increment": False,
        "not_null": True,
    },
    {
        "name": "edad",
        "type": "INT",
        "length": 3,
        "primary_key": False,
        "auto_increment": False,
        "not_null": True,
    },
]

# Llamar a la función crear_tabla
#bd.crear_tabla(nombre_bd, nombre_tabla, columnas)


