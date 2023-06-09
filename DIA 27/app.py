import bd.base_datos as sqlbd

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)

base_datos.motrasr_datos()

base_datos.borrar_datos('prueba1')


#base_datos.crear_datos('prueba1')    


base_datos.copia_bd('world')