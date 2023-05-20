from tkinter import *
import tkinter.messagebox as msb
import random

#Mensaje de inicio del juego
msb.showinfo("Adivina el número.", "Introduzca un número del 0 al 1000. ¿Cuántos intentos necesitará para conseguir acertar el número secreto?")

root = Tk()
root.title("")
root.resizable(False, False)
root.attributes("-topmost", True)
ancho_ventana = 400
alto_ventana = 100

#Pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

coordenadas_x = int((ancho_pantalla/2) - (ancho_ventana/2))#copiado y pegado del ejercicio ven
coordenadas_y = int((alto_pantalla/2) - (alto_ventana/2))- 37

root.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, coordenadas_x, coordenadas_y))#copiado y pegado del ejercicio ven

#Entrada de datos
entrada = Entry(root)
entrada.insert(0,"Escriba un número...")
entrada.bind("<Button-1>", lambda d : entrada.delete(0, END))
entrada.pack()

aleatorio = random.randint(0, 1000)
intentos = 1
print(aleatorio)

#Evento para el botón
def pulsar_boton():
    global intentos
    #Se obtiene el valor del Entry
    try:
        numero = int(entrada.get())

        if numero < aleatorio:
            msb.showinfo("¡Fallaste!", f"El número es mayor. Introduce un número mayor que {numero}.")
            intentos += 1
        elif numero > aleatorio:
            msb.showinfo("¡Fallaste!", f"El número es menor. Introduce un número menor que {numero}.")
            intentos += 1
        else:
            msb.showinfo("¡Excelente!", f"Lo has adivinado. Necesitaste {intentos} intento/s.")
    
    except:
        msb.showerror("¡Error!", "Valor no válido.")
        intentos += 1

#Botón
Button(root, text="Enviar", command=pulsar_boton).pack()
#Bucle de ejecución
root.mainloop()