class Gato():
    def sonido(self):
        return 'Miua'
    
class Perro():
    def sonido(self):
        return 'Guau'

def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()

perro = Perro()

hacer_sonido(gato)

#print(perro.sonido())