lista_colore = ['rojo', 'azul', 'verde', 'amariilo']
#lista_colore_v2 = list('rojo', 'azul', 'verde', 'amariilo') (esta de error)
lista_colore_v2 = list(('rojo', 'azul', 'verde', 'amariilo'))
lista_colore_v3 =  ['rojo', 'azul', 'verde', 'amariilo']

otra = list(lista_colore_v2)
otra = lista_colore
lista_colore_v3.append('rosa') #append agrega un nuevo elemento ala lista pero al final 
lista_colore_v3.insert(0, 'morado') #insert agrega un elemnto nuevo en la lista el numero indica la posicion y luego ingresa el elemento
new_lista = lista_colore.copy()

print(type(lista_colore))
print(lista_colore[0])
print(type(otra))
#print(otra[1])
print(type(lista_colore_v2))
print(lista_colore_v2[2])
print(f'El segundo color de la lista es {lista_colore[1]}')
print(lista_colore[2])
print(lista_colore[3][3])
print(lista_colore[-4])

print(lista_colore)
lista_colore[1] = 'naranja'
print(lista_colore)
print(lista_colore_v3)
lista_colore_v3.pop(2) # se puede utilizar remove pero en este caso se ingresa el nombre del elemto EJ: lista_colore_v3.remove('azul')
print(lista_colore_v3)
lista_colore_v3.clear()
print(lista_colore_v3)
print(new_lista)
print(lista_colore_v2.count('rojo')) #cuentas cuantos calor
print(lista_colore_v2.index('rojo')) #cuenta en que posicion se encuentra el elemento
print(lista_colore_v2)
lista_colore_v2.reverse() # se le puede agrgar un True para que el orden alfabetico sea desentende tambien funciona con numero
print(lista_colore_v2)
lista_colore_v2.sort()#orden alfabetico
print(lista_colore_v2)
print(lista_colore_v2.reverse()) #esto da None
lista_colore.extend(lista_colore_v2) # al agregar un elemento con extend EJ lista_colores.extend('rojos'): el elemento se separa 
print(lista_colore)