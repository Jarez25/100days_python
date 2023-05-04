paquete_office = {  #los diccionaros se traajan con clave valor Ej 'word(esta es la clave)' : 'es  un procesador de texto(este es el valor)' 
    'word' : 'es un procesador de texto.',
    'excel' :  'es una hoja de calculo.',
    'power': 'es una hoja de presentaciones.'
}

paquete_office['access'] = ' es la base de datos' #para agregar un nuevo valor al diccionario
paquete_office['word'] = 'es el procesador de texto de office 365' # funciona igual que agregar un valor solo que en este caso lo edita simpre  y    cuando se le agrege el nombre de la llave correcta

diccionario_numero = {
    1 : 'valor1',
    2 : 'valor2',
    3 : 'valor3'
}
diccionario_vacio = {}
print(diccionario_vacio)

print(paquete_office['word']) # para llamar el valor de un diccioario es con la clave
print(paquete_office['access'])
#print(paquete_office['outlook'])
# este da un error de clave o un keyError ya que la clave no se encuentra

print(diccionario_numero[3])

inventario_game = {
    1 : 'Claymore',
    2 : 'Svalinn',
    3 : 'eternal health rune'
}
print(inventario_game)

inventario_game = {}

print(inventario_game)