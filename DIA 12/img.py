from tkinter import *

root = Tk()
root.title('Spiderman')

my_frame = Frame(root, width=600, height=500)
my_frame.pack()
img = PhotoImage(file='DIA 12/python.png')
Label(my_frame, image=img).place(x=50, y=50)
Label(my_frame, text='ESTA ES LA IMAGEN DE TK', fg='blue', font=('Comic Sans MS', 22)).place(x=200, y=10)


root.mainloop()