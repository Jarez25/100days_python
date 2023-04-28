color = 'azul'
numero = 100
numero_uno = 400
numero_s = "100"
numero_uno_s = "400"
operaciones_1 = 10 + 56 * 89 - 3 / 2
operaciones_2 = 10 +56 * (89 - 3) / 2
valor_uno = 4_897_567_800_678_543_558 # el numero sadra sin los guiones bajo
decision = True
decision_1 = False
numero_dos = 4
numero_tres = 756.54
texto = 'soy un string'
numero_cinco = 560
letra_numero = '10.23'
letra_numero_v2 = '50.23'
##suma_valores = int(letra_numero) + int(letra_numero_v2)
suma_valores_flot = float(letra_numero) +  float(letra_numero_v2)

valor_numero = str(numero_cinco)
numero_f = 10.2
numero_f_v2 = 10.5
suma_f = numero_f + numero_f_v2
multiplicar = 7.56 * 6.94
division_r = 10 // 3
division_resto = (10 % 3)
resultado = numero +  numero_uno
division = numero / numero_uno
numero_10 = 10
numero_10 += 10
numero -= 10
suma_terminal = 90 + 500

#suma numero + numero_uno
#resta numero - numero_uno
#multiplicacion numero * numero_uno
#division numero / numero_uno
#exponete  ** 
#  // resultado de divion con entero
# % devuelve el resto
# =+ ingrementa el valor de la variable


print(len('Amarillo'))
print(len(color))
print(color[0])

print(numero +  numero_uno)
print(numero_s + numero_uno_s)
print(resultado)
print(division)
print(2**10)
print(operaciones_1)
print(operaciones_2)
print(valor_uno)

print(type(numero_dos))
print(type(numero_tres))
print(type(texto))
print(type(decision))
print(len(valor_numero))

#print(suma_valores)
print(suma_valores_flot)
print(suma_f)


one = 10.563
two = 10.34

suma = int(one + two)

print(suma)
print(multiplicar)
print(round(multiplicar))
print(round(multiplicar, 2))
print(division_r)
print(division_resto)
print(numero_10)
print(numero)
#print('el valor de la suma es ' + suma_terminal) da error
print('el valor de la suma es ' + str(suma_terminal)) #creo que es mejor usar una fstring
print(f'el resultado de la suma es {suma_terminal}')