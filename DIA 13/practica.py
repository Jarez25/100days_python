class Motocicleta():
    
    estado = 'nueva'
    motor = False
    
    
    def __init__(self, color , matricula, combustibles_litros, numero_ruedas, marca, modelo, fecha_de_fabricacion, velocidad_punta, peso, precio, combustibles_maximo):
        self.color = color
        self.matricula = matricula
        self.combustibles_litros = combustibles_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_de_fabricacion = fecha_de_fabricacion
        self.velocidad_punta =velocidad_punta
        self.peso = peso
        self.precio = precio
        self.combustibles_maximo = combustibles_maximo
        
    def arrancar(self):
        if self.motor:
            print("Se escucha un molesto sonido al girar la llave. El motor ya estaba arrancado.")
        else:
            print("Se ha arrancado el motor. Ruge como un león.")
    
    def detener(self):
        if self.motor:
            print("Se detiene el motor.")
        else:
            print("No puedes parar el motor, porque ya está apagado. ¿No lo oyes?")
            
    def consultar_precio(self):
        print(f'el precio de la moto es {moto.precio}')
        
        
    def comprobar_deposito(self):
        print(f"--->REPORTE DE DEPÓSITO DE {self.marca} {self.modelo}<---")
        print(f"El depósito tiene {self.combustibles_litros} litros.")
        print(f"La capacidad máxima del tanque de combustible es de {self.combustibles_maximo}.")
        print(f"Faltan {self.combustibles_maximo - self.combustibles_litros} litros para llenar el depósito.")
        print(f"--->FIN DEL REPORTE<---\n")    
    
    
moto = Motocicleta('negro', 85983, 10, 2, 'TOYOTA', 'dragon', '12/04/22', 180, 75, 17, 18)

moto.detener()

moto.precio = 27000

moto.consultar_precio()

moto.comprobar_deposito()