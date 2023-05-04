numero_one = 5
numero_two = 1
numero_Three = '2'


try:
    if numero_two == int:
        print('no hay errores')
    else: 
        print('salta el codigo')
except:
    print('no es un entero')
    

try:
    print(numero_one +  numero_Three)
except:
    print('no es un entero')
else: #opcional
    print('la ejecucion puede continuar')
finally: # opcional
    print('la ejecciom continua')
    
try:
    print(numero_one + numero_Three)
except ValueError: # except (RuntimeError, TypeError, NameError)
    print('este es un error')