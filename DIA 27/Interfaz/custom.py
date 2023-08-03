import tkinter
import customtkinter

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('green')

root = customtkinter.CTk()
root.geometry('400x240')

def funcion_boton():
    print('botones prsentes')

button = customtkinter.CTkButton(master=root, text="CTkbutton", command=funcion_boton)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root.mainloop()