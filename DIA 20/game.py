import random

def advina_el_numero(x):
    
    
    print("============================")
    print("====welcome to the games====")
    print("============================")
    print("adivina el numero o muere")
    
    
    numer_random = random.randint(1, x)
    predecir = 0
    intento = 0
    
    while predecir != numer_random:
        predecir = int(input(f"Adiviana un numero entre 1 y {x}: \n"))
        if predecir < numer_random:
            intento += 1
            print(f"este numero es menor puedes probar de nuevo este es el intento numero{intento}")
        elif predecir > numer_random:
            intento += 1
            print("este numero es muy grande puedes probar de nuevo")
    print(f"Feliciadades adivinaste el numero {numer_random} correctamente. te a tomado {intento} intentos")
    
advina_el_numero(10)