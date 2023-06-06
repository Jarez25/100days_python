def funcion_decoradora(funcion_a_decorar):
    def dentro(*args, **kwargs):
        print('Esta es la función que decora')
        funcion_a_decorar(*args, **kwargs) #agumentos de clave valor
        print('Esta es la segunda parte de la decoración')
    
    return dentro

@funcion_decoradora
def suma(num1, num2): #esta recibe parametros
    print(num1 + num2)
    
@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)
    
def potencia(base, exponete):
    print(pow(base, exponete))
    
    
suma(10, 20)
resta(30, 15)
potencia(base=5,exponete=3)