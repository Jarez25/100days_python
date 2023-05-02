from days6 import saludar, hola #puedo importar una funciona a otro archivo 

hola('carlos', 45)
saludar()

# al llamar la funcion desde aqui se crea una carpeta llamada __pycache__

def suma( a, b): # las variable no se pueden utilizar fuera de la funcion solo dentro de ellas 
    print(a + b)

suma(5, 5)

def suma_v2 (x, y):
    return x + y 

resultado = suma_v2(99, 1)
resultado_v2 = suma_v2(98, 2)
resultado_total = resultado + resultado_v2

print(resultado)
print(resultado_v2)
print(resultado_total)

elementos = ['Tusgteno', 'oro', 'azufre']

def add_elemnto(elemento):
    elementos.insert(0, elemento)
    
add_elemnto(input('agrega una letra nueva \n'))

print(elementos)