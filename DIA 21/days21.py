#pip install mysql-connector-python
#pip install mysql-connector
import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='251115'
)

cursor = conexion.cursor()

cursor.execute('SHOW DATABASES')

for bd in cursor: #con este ciclo for es para recore la base de datos 
    print(bd) 

conexion.close()
