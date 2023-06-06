import math

def a(b):
    def c(*args):
        print(f"Empieza el cálculo...")
        b(*args)
        print("Operación realizada con éxito.")
    return c

@a
def area_rectangulo(base, altura): 
    print(f"El área del rectángulo es: {base * altura}.")
@a
def area_triangulo(base, altura):
    print(f"El área del rectángulo es: {base * altura / 2}")
@a
def area_circulo(radio):
    print(f"El área del círculo es {math.pi * radio ** 2}")
    
area_rectangulo(10,40)