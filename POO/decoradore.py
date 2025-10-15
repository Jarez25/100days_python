def decorador(funcion_decoradora):
    def decorador_uno():
        print('esta es una funcion decoradora')
        funcion_decoradora()
        print('esto es la segunda duncion decoradora')
    return decorador_uno


def decorador_dos(funcion_test):
    def wrapper():
        print('Ingresa tu nombre completo')
        nombre = funcion_test()  # capturamos el valor retornado
        print(f'Hola {nombre}, te estoy saludando desde el decorador 🎉')
        print('Esto es la segunda función decoradora dos')
        return nombre  # opcional, si quieres que la función siga devolviendo el nombre
    return wrapper


@decorador_dos
def pedir_nombre():
    nombre = input('¿Cuál es tu nombre? ')
    return nombre


# Ejecutamos
pedir_nombre()


@decorador
def saluda():
    print('hola como estas ')

# saludo_decorador = (saluda)


# saludo_decorador()
# saluda()


# @decorerador_dos
# def despedida():
#     print('adios nos vemos luego')


# despedida_decorador = (despedida)
# despedida_decorador()
