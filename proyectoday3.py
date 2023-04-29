print('**********************************')
print('======esta es un calculadora======')
print('**********************************')

numero_uno = int(input('ingresa el valor numero uno \n'))

numero_dos = int(input('ingresa el valor numero uno \n'))

print('Elige una opcion:')
print('1-suma')
print('2-resta')
print('3-multiplicacion')
print('4-division')
print('5-exponente')
print('6- resto')

elecion = int(input('elige un numero el deseas \n'))

suma = numero_uno + numero_dos
resta = numero_uno -  numero_dos
multiplicacion = numero_uno *  numero_dos
division = numero_uno / numero_dos
exponete = numero_uno ** numero_dos
resto = numero_uno % numero_dos

match elecion :
    case 1:
        print(suma)
    case 2:
        print(resta)
    case 3:
        print(multiplicacion)
    case 4:
        print(division)
    case 5:
        print(exponete)
    case 6:
        print(resto)
    case _:
        print('eligue una opcion correcta')
    
    
    
