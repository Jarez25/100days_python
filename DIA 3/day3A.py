edad = int(input('Ingresa tu edad \n'))

respuesta = 0


if edad >= 18:
    print('puedes conprar licor cual deseas compar \n')
    respuesta = input('1- rom. \n 2- whisky, \n 3-ginebra.\n ')
    
    if respuesta =='1':
        print('vas a tomar ron')
    elif respuesta == '2':
        print('vas a tomar whisky')
    elif respuesta == '3':
        print('vas a tomar ginebra')
    else:
        print('opcion invalioda')
else:
    print('Eres menor de edad no puede consumir nada')