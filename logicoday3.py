color = 'rojo'
forma = 'circulo'
tamaño = 'grande'


if color == 'rojo' and forma == 'circulo' and tamaño == 'pequeño':
    print('esto es un circulo rojo')
else:
    print('esto no es un circulo')

# and  
# True + True = True
# True + False = False 
# False + True = False
# False + False = False

if color == 'rojo' or forma == 'circulo' or tamaño == 'pequeño':
    print('esto es un circulo rojo')
else:
    print('esto no es un circulo')
    
# and  
# True + True = True
# True + False = True 
# False + True = True
# False + False = False

if not color == 'rojo':
    print('esto es un circulo rojo')
else:
    print('esto no es un circulo')