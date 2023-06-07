import mysql.connector

# Conexión
acceso_bd = {
    'host': 'localhost',
    'user': 'root',
    'password': '251115',
}

class BaseDatos:
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)
        self.cursor = self.conector.cursor()
        
    def consulta(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
    def motrasr_datos(self):
        self.cursor.execute('SHOW DATABASES')
        for bd in self.cursor:
            print(bd)
            
    def borrar_datos(self, nombre_bd):
        try:
            self.cursor.execute(f'DROP DATABASE {nombre_bd}')
            print(f'se elimino la base de datos{nombre_bd}. se elimino la base de datos correctamente')
        except:
            print(f'Base de datos {nombre_bd} no encontrada')
            print('esta son las base de datos que se encuentran')
            self.motrasr_datos()
            
    def crear_datos(self, nombre_bd):
        try:
            self.cursor.execute(f'CREATE DATABASE {nombre_bd}')
            print(f'se creo la base de datos{nombre_bd}. exitosamente')
        except:
            print(f'Ya existe una base de datos con este nombre : {nombre_bd} ')
            print('esta son las base de datos que se encuentran')
            self.motrasr_datos()