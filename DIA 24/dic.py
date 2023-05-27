def imprime_dic(*args, **kwargs):
    for elemento in kwargs.items():
        print(elemento)
        

user1 = {"nombre":"Javier", "apellidos":"Gómez de la barca", "edad":"27"}

imprime_dic(**user1) 


def mul(x,y, *args):
    return(x * y *args[0] *args[1])

print(mul(10,4,50,6))