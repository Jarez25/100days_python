error = input('Ingrea un codigo de error \n')

match error:
    case '200':
        print('Todo ok')
    case '301':
        print('Todo ok')
    case '302':
        print('Todo ok')
    case '404':
        print('Todo ok')
    case '500':
        print('Todo ok')
    case '503':
        print('Todo ok')
    case _:
        print('Error no disponible')
        
# if para repeciociones complejas 
# match para repeticiones sencillas