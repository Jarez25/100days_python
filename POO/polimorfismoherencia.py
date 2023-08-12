def reocorrer(elemento):
    for item in elemento:
        print(f'El elemento actual es: {item}')


lista = [1,2,3,4]
lista2 = ['numero', 'numer', 'nume', 'num', 'nu', 'n']
lista3 = 'numero'


reocorrer(lista)
reocorrer(lista2)
reocorrer(lista3)