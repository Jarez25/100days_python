
from tkinter import *


root = Tk()

root.title("Tablero de ajedrez")


marco_1 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="Black",
                    border=0)
marco_1.grid(row=0, column=0)

marco_2 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="white",
                    border=0)
marco_2.grid(row=0, column=1)

#Marco 3
marco_3 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="Black",
                    border=0)
marco_3.grid(row=0, column=2)

#Marco 4
marco_4 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="white",
                    border=0)
marco_4.grid(row=1, column=0)

#Marco 5
marco_5 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="Black",
                    border=0)
marco_5.grid(row=1, column=1)

#Marco 6
marco_6 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="white",
                    border=0)
marco_6.grid(row=1, column=2)

#Marco 7
marco_7 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="Black",
                    border=0)
marco_7.grid(row=2, column=0)

#Marco 8
marco_8 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="white",
                    border=0)
marco_8.grid(row=2, column=1)

#Marco 9
marco_9 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="Black",
                    border=0)
marco_9.grid(row=2, column=2)


marco_10 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="Black",
                    border=0)
marco_10.grid(row=3, column=0)

#Marco 8
marco_11 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="white",
                    border=0)
marco_11.grid(row=3, column=0)

#Marco 9
marco_12 = LabelFrame(root,
                    width=50,
                    height=50,
                    background="Black",
                    border=0)
marco_12.grid(row=3, column=1)


#Bucle de ejecución
root.mainloop()