def datos(*argumentos, **arguemntos_clave):
    print(argumentos)
    print(arguemntos_clave)
    
usuario1 = {'nombre':'javier', 'apellido':'gomez'}

datos(10,50,60, usuario1)