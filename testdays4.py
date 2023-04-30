lista_numero = [10, 45, 55, 76]
lista_colore = ["rojo", 'azul', 'verde', 'amarillo']

print(lista_numero[3])

print(f"el valor mas pqueño de la lista es {lista_numero[0]}. y el mas pequeño es {lista_numero[3]}")

print(lista_colore[1][2])

paises = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia & Herzegovina""Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan",
"Turks & Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]

print(len(paises)) #esta te cuanta los 74 caracteres pero inicia del 1 y pasa sar los otro valores restale 1 para asi pensar que iniciate del 0
print(paises[72])
print(paises[73])
print(paises[-1])
print(paises[-2])

#adañir otro colaores
lista_colore.insert(0, 'gris')
lista_colore.append('rosa')
lista_colore.insert(3, 'naranja')
print(lista_colore)
#eliminar colores
lista_colore.pop(1)
print(lista_colore)
lista_colore.pop(3)
print(lista_colore)
lista_colore.pop(3)
print(lista_colore)
#duplica lista
new_list = lista_colore.copy()
print(new_list)

lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
print(lista_numeros.count(10))
print(paises.index("Brunei"))
lista_numeros.sort()
print(lista_numeros)
lista_numeros.reverse()
print(lista_numeros)

print(len(paises))