import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='251115',
    database = 'Universidad'
)

cursor = conexion.cursor()


try:
    cursor.execute('CREATE TABLE clientes'
                  '(id INT NOT NULL AUTO_INCREMENT,'
                  'nombre VARCHAR (32) NOT NULL,'
                  'apellidos VARCHAR (64) NOT NULL,'
                  'telefono VARCHAR (9) NOT NULL,'
                  'direccion VARCHAR (256),'
                  'PRIMARY KEY (id));')
    print("Se creó correctamente la base de datos.")
    
except:
    print("Ocurrió un error al crear la base de datos. Inténtelo de nuevo.")