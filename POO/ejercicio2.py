class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f'Su nombre es: {self.nombre}')
        print(f'Su edad es: {self.edad}')

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f'su grado es: {self.grado}')


estudiante = Estudiante("Jarez", 25, "7mo")

estudiante.datos()
estudiante.mostrar_grado()