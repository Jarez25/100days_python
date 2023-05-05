import random

def adivina_el_número(x):

    print('*****************************')
    print('  ¡Bienvenido(a) al Juego!   ')
    print('*****************************')
    
    print('==========================================================')
    print('Tu meta es adivinar el número generado por la computadora.')
    print('==========================================================')


    número_aleatorio = random.randint(1, x) # seleciona un numero aleatorio entre 1 y numero de la funcion en este caso seria 100

    predicción = 0

 
    while predicción != número_aleatorio: #si la variable predicion es diferente  continua con el ciclo
        predicción = int(input(f'Adivina un número entre 1 y {x}: \n')) #cambia el valor de predicion de 0  a un input y en este caso combiete en input en int
        if predicción < número_aleatorio: 
            print('=============================================')
            print('Intenta otra vez. Este número es muy pequeño.')
            print('=============================================')

        elif predicción > número_aleatorio:
            print('===========================================')
            print('Intenta otra vez. Este número es muy grande.')
            print('===========================================')

    print(f'¡Felicitaciones! Adivinaste el número {número_aleatorio} correctamente.')

adivina_el_número(100)