class nombre:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'persona("{self.nombre}",{self.edad})'
    
    def __repr__(self) -> str:
        pass