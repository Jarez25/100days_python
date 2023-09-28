import bd.base_datos as sqlbd
import Interfaz.interfaz as gui

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)


ventana = gui.Login()

base_datos.consulta('SHOW DATABASE;')
