import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='251115'
)

cursor = conexion.cursor()


try:
    cursor.execute('DROP DATABASE Universidad2;')
    print("la base de datos se borro con exito.")
    
except:
    print("La base de datos ya no existe.")