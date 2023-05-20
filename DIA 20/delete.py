import os 

ruta = os.path.dirname(__file__)
delete = os.path.join(ruta, 'delete')
print(delete) #este es para borrar la carpeta delete del directorio

os.rmdir(delete)