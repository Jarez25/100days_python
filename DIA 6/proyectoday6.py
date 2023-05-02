print('**********************************')
print('======esta es un calculadora======')
print('**********************************')

def suma (numero_uno, numero_dos):
    return numero_uno + numero_dos 

def resta (numero_uno, numero_dos):
    return numero_uno - numero_dos 

def multiplicacion (numero_uno, numero_dos):
    return numero_uno * numero_dos 

def division (numero_uno, numero_dos):
    return numero_uno / numero_dos 

def exponente(numero_uno, numero_dos):
    return numero_uno ** numero_dos 

def resto (numero_uno, numero_dos):
    return numero_uno // numero_dos 

while True:
    print('Elige una opcion:')
    print('1-suma')
    print('2-resta')
    print('3-multiplicacion')
    print('4-division')
    print('5-exponente')
    print('6- resto')
    print('7 - salir')


    elecion = int(input('elige un numero el deseas \n'))

# suma = suma()
# resta = numero_uno -  numero_dos
# multiplicacion = numero_uno *  numero_dos
# division = numero_uno / numero_dos
# exponete = numero_uno ** numero_dos
# resto = numero_uno % numero_dos

    match elecion :
        case 1:
            print('a elegido sumar')
        case 2:
            print('a elegido restar')
        case 3:
            print('a elegido multiplicar')
        case 4:
            print('a elegido dividir')
        case 5:
            print('a elegido exponente')
        case 6:
            print(' a elegido resto')
        case 7:
            print('saliendo de la calculadora ....')
            break
        case _:
            print('opcion incorrecta')
    
    numero_uno = float(input('ingresa el primer valor \n'))
    numero_dos = float(input('ingresa el segundo valor \n'))
    
    match elecion:
        case 1:
            resultado = round(suma(numero_uno, numero_dos), 2)
            print(f'el valor de la suma es {resultado}.')
        case 2:
            resultado = round(resto(numero_uno, numero_dos), 2)
            print(f'el valor de la suma es {resultado}.')
        case 3:
            resultado = round(multiplicacion(numero_uno, numero_dos), 2)
            print(f'el valor de la suma es {resultado}.')
        case 4:
            resultado = round(division(numero_uno, numero_dos), 2)
            print(f'el valor de la suma es {resultado}.')
        case 5:
            resultado = round(exponente(numero_uno, numero_dos), 2)
            print(f'el valor de la suma es {resultado}.')
        case 6:
            resultado = round(resto(numero_uno, numero_dos), 2)
            print(f'el valor de la suma es {resultado}.')