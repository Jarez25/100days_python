lambda valor_uno , valor_dos : valor_uno +  valor_dos

suma = lambda numero_uno , numero_dos : numero_uno +  numero_dos

print(suma(10, 15))

resta = lambda numer, numer2 : numer - numer2
print(resta(10,5))


cuadro = lambda x : x ** 2
print(cuadro(5))

es_par = lambda x: x % 2 == 0
print(es_par(4))
print(es_par(7))

es_impar = lambda x: x % 2 == 1
print(es_impar(4))
print(es_impar(7))

longitud = lambda s: len(s)
print(longitud('hola mundo'))

maximo = lambda x, y : x if x > y else y
print(maximo(3,7))