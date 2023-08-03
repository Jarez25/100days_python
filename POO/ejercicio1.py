class Estudiante:
    def __init__(self, nombre, edad, grado) :
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f'el estudiante {self.nombre} esta estudiando')

nombre = input('ingresa tu nombre \n')
edad = input('ingresa tu edad \n')
grado = input('ingresa tu grado \n') 

estdiante = Estudiante(nombre, edad, grado)

print(f'este es el nombre {estdiante.nombre} y su edad es {estdiante.edad} y su grado es {estdiante.grado}')


while True:
    estudiar = input()
    if (estudiar.lower() == 'estudiar'):
        estdiante.estudiar()
    elif(estudiar.lower() == 'salir'):
        print('saliendo del programa')
        break
