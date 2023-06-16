import tkinter as tk
from tkinter import messagebox

def validar():
    if entrada_one.get()=='jarez':
        new_ventana()
    else:
        messagebox.showwarning('Advertencia', 'Contraseña Incorrecta')
        
def new_ventana():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('380x300+1000+200')
    win.configure(background='red')
    tag=tk.Label(win, text='Welcome ala segunda ventana', bg='pink', fg='white')
    tag.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    b = tk.Button(win,text='OK', command=win.destroy)
    b.pack(side=tk.TOP)
    
def close():
    ventana.destroy()
    
ventana = tk.Tk()
ventana.title('este es un segundo plano')
ventana.geometry('380x300')
ventana.configure(background='blue')

e= tk.Label(ventana,text='Password', bg='pink', fg='white')
e.pack(padx=5, pady=5, ipadx=5,ipady=5)
entrada_one = tk.Entry(ventana)
entrada_one.pack(fill=tk.X,padx=5, pady=5, ipadx=5,ipady=5)
boton=tk.Button(ventana,text='Nueva Ventana', fg='blue', command=new_ventana)
boton.pack(side=tk.TOP)
boton3=tk.Button(ventana, text='Validar Password', fg='Blue', command=validar)
boton3.pack(side=tk.TOP)

ventana.mainloop()