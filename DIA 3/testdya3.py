numero = 10

if numero >= 7: 
    print('verdadero.')

 
if numero != 5:
    print('otra vez verdadero')
    

if numero == 10:
    print('son iguales')
    

color = 'morado'
forma = 'cuadrado'
tamaño = 'grande'

if color == 'morado' and forma == 'cuadrado':
    print('es verdadero')
else:
    print('falso')
   
    
if color == 'morado' and forma == 'cuadrado' or tamaño == 'grande':
    print('esto es real')
else: # el bloque else no lleva exprecion depende del bloque if y elif 
    print('falso')