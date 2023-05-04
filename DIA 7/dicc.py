paquete_office = {
    'word' : 'es un procesador de texto.',
    'excel' :  'es una hoja de calculo.',
    'power': 'es una hoja de presentaciones.'
}

my_person = {
    'nombre' : 'jairo',
    'alias' : 'jarez',
    'apellido' : 'Medina',
    'edad' : 25,
    'L_aprendiendo' : {'html', 'css', 'python'}
}

for key in paquete_office:
    print(f'->{key.capitalize()}')
    
for key in paquete_office:
    print(f'->{key.capitalize()} : {paquete_office[key]}')  
    
  #pacticas  
colores = {
    1 :  'rojo',
    2 : 'azul',
    3 : 'verde',
    4 : 'amarrillo'
}

colores['5'] = ' morado'

for color in colores:
    print(f'->{color} - {colores[color].capitalize()}')
    
print(my_person)
print('rojo' in colores )
print(1 in colores )
    

    