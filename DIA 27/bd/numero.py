import bd.base_datos as sqlbd

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)

registro = [{"nombre": "Enrique",
 "apellidos" : "Barros Fernández",
 "telefono" : "786959404",
 "direccion" : "C/cualquiera"}]

base_datos.insertar_registro("pruebas", "usuarios", registro)