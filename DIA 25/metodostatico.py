import math

class Pastel:
    def __init__(self, ingredientes, talla):
        self.ingredientes = ingredientes
        self.talla = talla
        
    def __repr__(self) -> str:
        return(f'Pastel({self.ingredientes}, 'f'{self.talla})') 
    
    def area(self):
        return self.talla_area(self.talla)
    
    @staticmethod
    def talla_area(A):
        return A ** 2  * math.pi
    
nuevo = Pastel(['harina', 'azucar', 'crema', 'leche'], 4)

print(nuevo.ingredientes)
print(nuevo.talla_area(12))