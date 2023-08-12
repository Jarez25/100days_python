class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre


jarez = Persona('Jairo', 26)

nombre = jarez.nombre

print(nombre)

jarez.nombre = 'Parrrot'

nombre = jarez.nombre

print(nombre)