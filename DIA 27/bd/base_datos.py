import mysql.connector

# Conexión
acceso_bd = {
    'host': 'localhost',
    'user': 'root',
    'password': '251115',
    'database': 'animales'
}

class BaseDatos:
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)
        
    def consulta(self, sql):
        cursor = self.conector.cursor()
        cursor.execute(sql)
        return cursor
