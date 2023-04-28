var = 'automaticamente'
var2 = len(var)
print(var2)
#print(var2[5]) me da error
print(var[5])
eleva = 10 ** 5

print(eleva)
sin = 10 * 10 * 10 * 10 * 10
print(sin)

#estados de datos boleanos
True
False

#mostrar tipo de dato
numero_1 = 675.87
print(type(numero_1))

#usar len para contar un numero
numero_dos = 78763843
numero_tres = str(numero_dos)
print(len(numero_tres))
print(len(str(numero_dos))) # otra manera mas corta

#convertir datos en interger


numero_cuatro = "14.527"
numero_cinco = "560.92"

numeroa = float(numero_cuatro)
numerob = float(numero_cinco)

print(int(numeroa))
print(int(numerob))

# redonderar numero
uno = 10.41564561458451 # 3 decimales
dos = 7674.7886 # 2 decimales
tres = 68754.78 # 1 decimal

print(round(uno, 3))
print(round(dos, 2))
print(round(tres, 1))

#valor de decremento o imcremento
cuatro = 10 # +60
cinco = 24 # -100
seis = 65.67 # +4.33

cuatro += 60
cinco -= 100
seis += 4.33
print(cuatro)
print(cinco)
print(seis)

# usar fstring

siete = 4
ocho = 769.97
texto = 'am I a string'
decision = True

print(f' el valor {siete} es bastante mas grande que el valor { ocho}. {texto} the asbwer is {decision}')