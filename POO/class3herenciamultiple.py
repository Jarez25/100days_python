class Persona:
    def __init__(self, nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print('hola como te llamas')

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad  

    def mostrar_habilidad(self):
        print(f'mi habilidad es {self.habilidad}')     

#class Empleado(Persona):
    #def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
     #   super().__init__(nombre, edad, nacionalidad)
      #  self.trabajo =  trabajo
       # self.salario = salario


class Empleado_artista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.trabajo = trabajo
        self.salario = salario

    def presentar(self):
        return f'{super().mostrar_habilidad()}'


robert = Empleado_artista("roberto", 34, 'nicaragua', 'cantar' ,'programador', 500)

print(f' su nombre es {robert.nombre} y tiene {robert.edad} el vive en {robert.nacionalidad} y trabaja de {robert.trabajo} donde gana la cifra de C${robert.salario}')

robert.presentar()


herncia = issubclass(Empleado_artista,Artista)
istacias = isinstance(robert,Empleado_artista)
print(herncia)
print(istacias)