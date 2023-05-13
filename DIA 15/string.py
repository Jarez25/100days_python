mensaje = 'este es una cadena'
buscar = 'este'
buscar1 = 'hola'

for letras in mensaje:
    print(letras)
    
print(buscar in mensaje)

print(buscar1 in mensaje)

dicc = dict(enumerate(mensaje))
tupla = tuple(enumerate(mensaje))
lista = set(enumerate(mensaje))

print(dicc)
print(tupla)
print(lista)

cadena = input()


for l in cadena:
    print(l)
    
