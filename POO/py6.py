<<<<<<< HEAD
class Calculadora:
    def __init__(self, numero1, numero2):
        self.suma = numero1 + numero2
        self.resta = numero1 - numero2
        self.multi = numero1 * numero2
        self.dici = numero1 / numero2
        

resul = Calculadora(5,20)

print(resul.suma)
=======
class Persona:
    edad = 25
    nombre = 'Jarez'
    pais = 'Nicaragua'
    
programador = Persona()
print('la edad es: ', programador.edad)
print('la edad es:' ,getattr(programador,'edad'))
print('el  doctor tiene una edad', hasattr(programador, 'edad'))
print('el  doctor tiene una edad', hasattr(programador, 'apellido'))
print(programador.nombre)
setattr(programador, 'nombre', 'Jairo')
print(programador.nombre)
# delattr(programador.pais)
print(programador.pais)
>>>>>>> adf6100ec24d70dc5451ba09c52b60b3b607ec75
