def decorador(funcion_decoradora):
    def decorador_uno():
        print('esta es una funcion decoradora')
        funcion_decoradora()
        print('esto es la segunda duncion decoradora')
    return decorador_uno



#@decorador
def saluda():
    print('hola como estas ')

saludo_decorador = decorador(saluda)


saludo_decorador()
#saluda()