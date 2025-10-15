class Persona:
    def __init__(self, nombre, edad, nacionalidad):
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


class Idioma:
    def __init__(self, idioma):
        self.idioma = idioma

    def mostrar_idioma(self):
        print(f'hablo {self.idioma}')

# class Empleado(Persona):
    # def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
     #   super().__init__(nombre, edad, nacionalidad)
      #  self.trabajo =  trabajo
       # self.salario = salario


class Empleado_artista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.trabajo = trabajo
        self.salario = salario

    def presentar(self):
        return f'{super().mostrar_habilidad()}'


class Traductor(Empleado_artista, Idioma):
    def __init__(self, nombre, edad, nacionalidad, habilidad, trabajo, salario, idioma):
        Empleado_artista.__init__(
            self, nombre, edad, nacionalidad, habilidad, trabajo, salario)
        Idioma.__init__(self, idioma)

    def presentar(self):
        return f'{self.nombre}, traductor en {self.idioma}, {super().mostrar_habilidad()}'


Pablos = Traductor('pablo', 23, 'colombia', 'cantar',
                   'desarrolador', 600, 'ingles')

robert = Empleado_artista("roberto", 34, 'nicaragua',
                          'cantar', 'programador', 500)

print(f' su nombre es {Pablos.nombre} y tiene {Pablos.edad} el vive en {Pablos.nacionalidad} y trabaja de {Pablos.trabajo} el sabe habla otro idioma {Pablos.idioma} donde gana la cifra de C${Pablos.salario}')
Pablos.presentar()

print(f' su nombre es {robert.nombre} y tiene {robert.edad} el vive en {robert.nacionalidad} y trabaja de {robert.trabajo} donde gana la cifra de C${robert.salario}')
robert.presentar()


herncia = issubclass(Empleado_artista, Artista)
istacias = isinstance(robert, Empleado_artista)
print(herncia)
print(istacias)
