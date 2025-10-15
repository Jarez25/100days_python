class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre


jarez = Persona('Jairo', 26)
edad = jarez.edad
print(edad)
nombre = jarez.nombre
print(nombre)


jarez.nombre = 'Parrot'
nombre = jarez.nombre
print(nombre)
