import tkinter
import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('400x240')

def funcion_boton():
    root.destroy()
    ventana2 = customtkinter.CTk()
    ventana2.title("Segunda ventana")
    ventana2.geometry("300x100")
    ventana2.mainloop()  


def funcion_boton2():
    root.destroy()  
    ventana2 = customtkinter.CTk()
    ventana2.title("tercera")
    ventana2.geometry("300x100")
    ventana2.mainloop() 

button1 = customtkinter.CTkButton(master=root, text="Sventana", command=funcion_boton)
button1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button2 = customtkinter.CTkButton(master=root, text="Tventana", command=funcion_boton2)
button2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

root.mainloop()