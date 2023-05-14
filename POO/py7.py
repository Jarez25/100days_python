class Persona:
    edad = 27
    nombre = 'jarez'
    pais = 'nicaragua'
    
doctor = Persona()

print(f' la edad es {doctor.edad}')
print('su edad es: ', getattr(doctor, 'edad'))

print('el doctor tiene una edad?', hasattr(doctor, 'edad'))

print('antes era: ',doctor.nombre)
setattr(doctor, 'nombre', 'hector')
print('ahora se llama: ', doctor.nombre)

#delattr(Persona, 'pais')
print(doctor.pais)