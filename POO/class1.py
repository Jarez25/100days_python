class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def encender(self):
        print(f'encendiste el celular {self.marca}')

    def apagar(self):
        print(f'apagaste tu celular {self.marca}')

celular1 = Celular('LG', "k10", "10 Mp")

print(celular1.camara)

celular1.encender()