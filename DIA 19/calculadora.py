from operaciones import suma, resta,division,modulo,exponente, multiplicacion

# Se da un título a la calculadora.
print("--- CALCULADORA MEJORADA DE NUEVO ---")

while True:
    # Se le pide al usuario que elija una opción y se evalúa
    print("Por favor, elija una opción:")
    print("1- Suma.")
    print("2- Resta.")
    print("3- Multiplicación.")
    print("4- División.")
    print("5- Módulo.")
    print("6- Exponente.")
    print("7- Salir.")

    # Se le pide al usuario un número de opción
    eleccion = int(input("Teclee un número y pulse ENTER:\n"))

    match eleccion:
        case 1:
            print('Ha elegido la opción "suma".')
        case 2:
            print('Ha elegido la opción "resta".')
        case 3:
            print('Ha elegido la opción "multiplicación".')
        case 4:
            print('Ha elegido la opción "división".')
        case 5:
            print('Ha elegido la opción "módulo".')
        case 6:
            print('Ha elegido la opción "exponente".')
        case 7:
            print('Saliendo de la calculadora...')
            break
        case _:
            print('Error, opción inválida. Especifique una opción del 1 al 7.')

    # Se solicitan los dos números para cualquier operación que elija.
    numero_1 = float(input("Especifique el primer operando:\n"))
    numero_2 = float(input("Especifique el segundo operando:\n"))
    
    match eleccion:
        case 1:
            resultado = round(suma(numero_1, numero_2), 2)
            print(f"El resultado de sumar {numero_1} + {numero_2} es: {resultado}.")
        case 2:
            resultado = round(resta(numero_1, numero_2), 2)
            print(f"El resultado de restar {numero_1} - {numero_2} es: {resultado}.")
        case 3:
            resultado = round(multiplicacion(numero_1, numero_2), 2)
            print(f"El resultado de multiplicar {numero_1} por {numero_2} es: {resultado}.")
        case 4:
            resultado = round(division(numero_1, numero_2), 2)
            print(f"El resultado de dividir {numero_1} entre {numero_2} es: {resultado}.")
        case 5:
            resultado = round(modulo(numero_1, numero_2), 2)
            print(f"El resto de la división de {numero_1} entre {numero_2} es: {resultado}.")
        case 6:
            resultado = round(exponente(numero_1, numero_2), 2)
            print(f"{numero_1} elevado a {numero_2} es: {resultado}.")