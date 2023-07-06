import bd.base_datos as sqlbd

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)

#base_datos.mostrar_bd()

#base_datos.crear_bd('nueva')

base_datos.mostrar_tablas('sakila')
#base_datos.eliminar_bd('nueva')

#base_datos.eliminar_bd('datos')

#base_datos.consulta('SHOW DATABASE') 

#base_datos.crear_tabla()
#base_datos.eliminar_tabla()



#base_datos.crear_datos('datos2')  


#base_datos.copia_bd('world')