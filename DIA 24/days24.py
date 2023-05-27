def claves (**kwargs):
    numero  = 0
    for clave in kwargs.keys():
        numero +=1
        print(f'clave {numero}:{clave}.')

claves(nombre = 'jarez', apellido = 'medina', edad=25)

def key(**kwargs):
    print(kwargs)

key(nombre = 'jarez', apellido = 'medina', edad=25)