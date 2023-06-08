import mysql.connector

# Conexión
acceso_bd = {
    'host': 'localhost',
    'user': 'root',
    'password': '251115',
}
#La clase para hacer la conexion ala base de datos
class BaseDatos:
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)
        self.cursor = self.conector.cursor()

# decorador de base de datos       
    def repor_datos(fparametro):
        def inter(self, nombre_bd):
            fparametro(self, nombre_bd)
            print('esta son las base de datos que se encuentran')
            BaseDatos.motrasr_datos(self)
        return inter
    
# consultas        
    def consulta(self, sql):
        self.cursor.execute(sql)
        return self.cursor
    
 # muestra los datos    
    def motrasr_datos(self):
        self.cursor.execute('SHOW DATABASES')
        for bd in self.cursor:
            print(bd)
            
#elimina los datos
    @repor_datos                
    def borrar_datos(self, nombre_bd):
        try:
            self.cursor.execute(f'DROP DATABASE {nombre_bd}')
            print(f'se elimino la base de datos{nombre_bd}. se elimino la base de datos correctamente')
        except:
            print(f'Base de datos {nombre_bd} no encontrada')
            
#crea los datos de la base de datos  
    @repor_datos          
    def crear_datos(self, nombre_bd):
        try:
            self.cursor.execute(f'CREATE DATABASE IF NO EXISTS {nombre_bd}')
            print(f'se creo la base de datos{nombre_bd}. exitosamente')
        except:
            print(f'Ya existe una base de datos con este nombre : {nombre_bd} ')
