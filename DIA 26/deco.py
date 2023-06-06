def funcion_decoradora(funcion_a_decorar):
    def dentro():
        print('Esta es la función que decora')
        funcion_a_decorar()
        print('Esta es la segunda parte de la decoración')
    
    return dentro

@funcion_decoradora
def suma(): #esta no recibe parametros
    print(15+20)
    
@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()