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


frase = ["esta", "es", "una", "frase"]

print('  '.join(frase))

colore = ['azul', 'verde', 'rojo']
GUIN ='-'
PUNTO = '.'

for color in colore:
    print('{}{}{}'.format(GUIN,color.capitalize(),PUNTO))
    
numerouno = 15
numerodos = 34.55

resultado = numerouno *  numerodos

print('la multiplicacion de %i * %f da como resultado: %f.'%(numerouno,numerodos, resultado))


texto = 'Ya que la elección del directorio dónde vivirá el intérprete es una opción del proceso de instalación, puede estar en otros lugares; consulta a tu gurú de Python local o administrador de sistemas'

letra = input('cual es la letra \n')

contador = 0


for i in texto:
    if letra in i :
        contador += 1
print(f'se econtro {contador} veces esa letra')