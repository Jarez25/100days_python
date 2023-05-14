class Calculadora:
    def __init__(self, numero1, numero2):
        self.suma = numero1 + numero2
        self.resta = numero1 - numero2
        self.multi = numero1 * numero2
        self.dici = numero1 / numero2
        

resul = Calculadora(5,20)

print(resul.suma)