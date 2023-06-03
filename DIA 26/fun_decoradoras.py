def a(b):
    def c():
        print('resultado de la operacion es ')
        b()
        print('Operacion realizada con exito')
    return c

@a
def sumar():
    print(10 + 10)
    
@a
def restar():
    print(10 - 20)
@a    
def multiplicar():
    print(45 * 2)
@a
def dividir():
    print(4 / 87)
    
sumar()

restar()