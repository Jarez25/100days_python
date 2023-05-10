(lambda numero_uno, numero_dos : print(numero_uno * numero_dos))(5,5)

radio = int(input('ingrese el radio del circulo'))

PI = 3.1416

area = lambda radios_cm: PI * radios_cm * radios_cm

area_c = round(area(radio), 2)
print(area_c)

(lambda texto : print(f'hola {texto}'))('jairo')

colores = ['rojo', 'azul', 'verde', 'amarillo']

(lambda color : print(f'el color de este valor es {colores.index(color)} de la lista'))('azul')