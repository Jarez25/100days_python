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
delattr(programador.pais)
print(programador.pais)
