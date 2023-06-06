import bd.base_datos as sqlbd

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)

consulta_1 = base_datos.consulta('SHOW DATABASES')

for bd in consulta_1:
    print(bd)
