class Usuario:
    def __init__(self, celular, nombre ='defaul', apellido='defaul', edad='defaul') -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.celular = celular
        
        
    def decribe(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Edad: {self.edad}')
        print(f'Celular: {self.celular}')

user1 = Usuario('85738074','Jarez')

user1.decribe()