class Animal:
    def comer(self):
        print('el animal esta comiendo')

class Ave(Animal):
    def volar(self):
        print('el animal esta volando')


class Mamifer(Animal):
    def amamantar(self):
        print('el animal esta amamantando')


class Muercielago(Ave, Mamifer):
    pass

muercielago = Muercielago()


muercielago.amamantar()
muercielago.comer()
muercielago.volar()

print(Muercielago.mro())
