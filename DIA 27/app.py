import bd.base_datos as sqlbd
import bd.tablas as tbl

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)

base_datos.mostrar_bd()

#base_datos.borrar_datos('datos1')

base_datos.crear_tabla()



#base_datos.crear_datos('datos2')  


#base_datos.copia_bd('world')