class Vehiculo():
    color = None
    metros = None
    ruedas = 4
    
    def arrancar(self):
        print('el vehiculo se a encendido')
    
    def detener(self):
        print('el vehiculo se a detenido')
    
Vehiculo1 = Vehiculo()
Vehiculo2 = Vehiculo()

Vehiculo2.material_aleron = 'Fibra de carbono'

Vehiculo1.arrancar()
print(Vehiculo2.material_aleron) #crea un nuevo atribuno que solo existe en el vehiculo 2