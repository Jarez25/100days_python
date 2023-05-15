from tkinter import *

root = Tk()
root.title("TABLERO DE AJEDREZ")

for blanco in range(8):
    for negro in range(8):
        marco = LabelFrame(root,
                           width=50,
                           height=50,
                           border=0,
                           borderwidth=2,
                           relief='solid'
                           )
        
        if (blanco + negro) % 2 == 0:
            marco.configure(background="white")
        else:
            marco.configure(background="black")
        
        marco.grid(row=blanco, column=negro)




root.mainloop()