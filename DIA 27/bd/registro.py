import base_datos as sqlbd

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)

registros = [
            [{"nombre": "Pedro", "apellidos": "García López", "telefono":"145645645", "direccion": "Calle del Sol #123"}],
            [{"nombre": "Ana", "apellidos": "Martínez Torres", "telefono": "547546775", "direccion": "Avenida del Mar #46"}],
            [{"nombre": "Mario", "apellidos": "Díaz González", "telefono": "654733534", "direccion": "Calle del Parque #20"}],
            [{"nombre": "Sofía", "apellidos": "Torres Fernández", "telefono": "534654645", "direccion": "Calle del Puerto #23"}],
            [{"nombre": "Enrique", "apellidos" : "Barros Fernández", "telefono" : "786959404", "direccion" : "Calle cualquiera #56"}]
            ]

for registro in registros:
    base_datos.insertar_registro("nueva", "usuarios", registro)