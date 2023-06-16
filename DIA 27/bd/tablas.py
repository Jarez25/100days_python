import mysql.connector

acceso_bd = {"host" : "localhost",
             "user" : "root",
             "password" : "251115",
             }

class BaseDatos:
    #Conexión y cursor
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)
        self.cursor = self.conector.cursor()
        self.contrasena = kwargs["password"]

base_datos = BaseDatos(**acceso_bd)

columnas = [
    {
        'name': 'id',
        'type': 'INT',
        'length': 10,
        'primary_key': True,
        'auto_increment': True,
        'not_null': True
    },
    {
        'name': 'nombre',
        'type': 'VARCHAR',
        'length': 32,
        'primary_key': False,
        'auto_increment': False,
        'not_null': True
    },
    {
        'name': 'apellidos',
        'type': 'VARCHAR',
        'length': 64,
        'primary_key': False,
        'auto_increment': False,
        'not_null': True
    },
    {
        'name': 'telefono',
        'type': 'VARCHAR',
        'length': 9,
        'primary_key': False,
        'auto_increment': False,
        'not_null': False
    },
    {
        'name': 'direccion',
        'type': 'VARCHAR',
        'length': 128,
        'primary_key': False,
        'auto_increment': False,
        'not_null': False
    }
]

base_datos.crear_tabla('base_datos_cualquiera', 'nombre_tabla', columnas)