for i in range(5): 
    print(f'el valor del bucle es {i}.')
print('final de primer bucle for')


for i in range(3, 9): 
    print(f'el valor del bucle es {i}.')
print('final de segundo bucle for')
    

for i in range(3, 12, 2): 
    print(f'el valor del bucle es {i}.')
print('final de tercero bucle for')

#for en negativos
    

for i in range(3, -12, -3): 
    print(f'el valor del bucle es {i}.')
print('final de tercero bucle for')


# lista de colores con for

colore = ['rojo', 'azul', 'morado']

for color in colore:
    print (color)
    
for color in colore:
    if color == 'azul' or color == 'verde':
        print('se a saltado este valor')
        continue
    print(f'el color es {color}')
    
for color in colore:
    if color == 'azul':
        print('se a roto la ejecicion')
        break
    print(f'el color es {color}')