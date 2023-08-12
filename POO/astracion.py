class Auto():
    def __init__(self):
        self._estado = 'apagado'

    def encender(self):
        self._estado = 'encendido'
        print('el auto esta encendido')


    def conducir(self):
        if self._estado == 'apagado':
            self.encender
            print('El auto se esta conduciendo')


Mycar = Auto()

Mycar.conducir()