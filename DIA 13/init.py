class Vehiculo():
    
    pais_de_origen = 'Alemania' # este es un atributo de clase 
    
    def __init__(self, color, metros, ruedas):# self es el opbjeto istansiado en la clase esto aun se me hace complicado
        self.color = color  # estos son atributos de istancia
        self.metro = metros
        self.ruedas = ruedas
    
    def arrancar(self):
        print('el vehiculo se a encendido')
    
    def detener(self):
        print('el vehiculo se a detenido')
        
    def mostar_info(self):
        print(f'el color del vehiculo es {self.color}. con una longitud de {self.metro} y tiene {self.ruedas} ruedas \n el pais de origen es {self.pais_de_origen}')   
    
Vehiculo1 = Vehiculo('rojo', 4, 4)
Vehiculo2 = Vehiculo('negro', 8, 16)

print(Vehiculo1.pais_de_origen)

#Vehiculo2.material_aleron = 'Fibra de carbono'

Vehiculo1.arrancar()
Vehiculo1.mostar_info()
Vehiculo2.mostar_info()
#print(Vehiculo2.material_aleron) #crea un nuevo atribuno que solo existe en el vehiculo 2

class vacia():
    pass #con este pass la clase se puede dejar vacia y sin inicalozar para crear intancias sin tener codigo
        # el pas se puede usar con los condicionales con los ciclos for y while y con las funciones 
        # a pesar que se usa con las funciones no se puede usar con las lambda
if True:
    pass

for i in range(0):
    pass

def funcion():
    pass

while True:
    pass

