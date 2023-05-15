from tkinter import *

root = Tk()

root.title('INTERFAZ')


marco = LabelFrame(root, text='frame vacio', width=300, height=300 )
marco.pack(padx=25, pady=10, side='bottom')

color1 = LabelFrame(marco,
                    width=200,
                    height=400,
                    border=0,
                    background='red')
color1.grid(row=0, column=0)

color2 = LabelFrame(marco,
                    width=200,
                    height=400,
                    border=0,
                    background='blue')
color2.grid(row=0, column=1)

root.mainloop()