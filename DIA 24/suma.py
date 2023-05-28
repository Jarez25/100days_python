def sumar(*args):
    print(args[0] +  args[1] + args[2])
    
sumar(10, 7, 40)



def sumar1(x,y, *args):
    print(args[0] +  args[1] + args[2] + x + y)
    
sumar1(10, 7, 40, 40 ,80)

def muestra_datos(**kwargs):
    claves = tuple(kwargs.keys())
    valores = tuple(kwargs.values())
    print(f"El {claves[0]} es {valores[0]}, sus {claves[1]} son {valores[1]} y tiene {valores[2]} años de {claves[2]}." )
    
usuario1 = {"nombre":"Javier", "apellidos":"Gómez de la barca", "edad":"27"}

usuario2 = {"nombre":"Andrea", "apellidos":"Pedraza Peña", "edad":"31"}

muestra_datos(**usuario1)
muestra_datos(**usuario2)