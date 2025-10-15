class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


robert = Empleado("roberto", 34, 'nicaragua', 'programador', 500)

print(f' su nombre es {robert.nombre} y tiene {robert.edad} el vive en {robert.nacionalidad} y trabaja de {robert.trabajo} donde gana la cifra de C${robert.salario}')
