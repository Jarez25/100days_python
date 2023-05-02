def saludar():
    nombre = input('ingresa tu nombre \n')
    print(f'hola como estas {nombre}')

saludar()

def hola(name, age):
    print(f'hola como estas {name}')
    print(f'tu edad es de {age}')
    
hola('Jairo' , 25)
hola(name = 'jarez', age = 25) 

# argumetos posicionales  van por orden de posicion en la declaracion de los parametros
# argumentos de clave van en cualquier orden, ya que se indica en el propio argumento , el parametro es como la clave