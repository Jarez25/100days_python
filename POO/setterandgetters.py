class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, new_nombre):
        self.nombre = new_nombre


jarez = Persona('Jairo', 26)

nombre = jarez.get_nombre()
print(nombre)

jarez.set_nombre('Parrot')

nombre = jarez.get_nombre()
print(nombre)