my_set  = set()
print(type(my_set))

lenguajes = {'python', 'kothin', 'java', 'javascript', 'cobol', 'lisp', 'python'}
desarollor = {'junior', 'semi-senior', 'senior'}
lenguajes_lista = ['pyton', 'kothin', 'java', 'javascript', 'cobol', 'lisp', 'python']

print(lenguajes) #los imprime en un orden diferenente de forma aleatoria
print(lenguajes)
print(lenguajes) # el orden no varia durante la ejecucion 
print('     ESTA ES LA LINEA DE SEPARACION    ')

print(lenguajes) #en los set no puede haber valores duplicados o este te los quito(no admite valores repetidos)
print(lenguajes_lista)

print(len(lenguajes))
lenguajes.add('PHP') #agrega un valor al set

print(lenguajes)
print('PHP' in lenguajes) #si un elemento existe en el set
print('ruby' in lenguajes)

lenguajes.remove('cobol') #elimina el 1 valor del set en este caso "cobol"
print(lenguajes)

print(lenguajes.union(desarollor))

lenguajes.clear() # elimina todos los valores del set
print(lenguajes)
