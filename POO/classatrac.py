from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentar(self):
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años.')


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Estoy estudiando {self.actividad}')


class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Estoy trabajando como {self.actividad}')


class Desempleado(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f'Actualmente no tengo empleo, mi actividad es {self.actividad}')


nombre = Estudiante('Jairo', 26, 'masculino', 'aprendiz de programador')
jairo = Trabajador('Jarez', 27, 'masculino', 'programador junior')
luis = Desempleado('luis', 30, 'masculino', 'ninguna')

nombre.hacer_actividad()
nombre.presentar()
jairo.hacer_actividad()
jairo.presentar()
luis.hacer_actividad()
luis.presentar()
