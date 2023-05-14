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


comillas = '''este es  un mensade con "comillas" y uno de 'simples'. ''' #funciona igual si en vez de la simple agregamos 3 dobles


print(dicc)
print(tupla)
print(lista)