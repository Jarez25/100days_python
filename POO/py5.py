class Calculadora:
    def __init__(self, numero_uno, numero_dos): 
        self.suam = numero_uno + numero_dos
        self.resta = numero_uno - numero_dos
        self.multi = numero_uno * numero_dos
        self.div = numero_uno / numero_dos
        
resultado = Calculadora(2,5)
print(resultado.suam)
print(resultado.resta)
print(resultado.multi)
print(resultado.div)