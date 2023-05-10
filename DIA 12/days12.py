from tkinter import *

root = Tk()
root.title('Frames')


for relieve in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
    frame = Frame(root, borderwidth=10, relief=relieve)
    frame.pack(side=LEFT, padx=5, pady=5)
    Label(frame, text=relieve, width=10).pack()
    Button(frame,text=relieve, width=10).pack()
    
for colors in ['blue', 'red', 'green', 'yellow']:
    frame =  Frame(root, borderwidth=5, relief=SOLID)
    frame.pack(side=RIGHT, padx=5, pady=5)
    Button(frame, text=colors, width=5).pack()

root.mainloop()