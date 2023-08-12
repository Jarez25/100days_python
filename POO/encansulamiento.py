class Miclase:
    def __init__(self):
        self.__atributos_privados = 'valor'

    def __hablar(self):
        print('hola como estas')


objeto = Miclase()
print(objeto.__hablar())