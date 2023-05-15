import tkinter as tk



class TestApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.enabled_var = tk.IntVar(value=1)
        self.entry_text = tk.StringVar(value="Hola StackOverflow")

        self.entry = tk.Entry(self,
                              background="#ccff66",
                              foreground="#000000",
                              disabledbackground="#4d4d4d",
                              disabledforeground="#ffffff",
                              textvariable=self.entry_text 
                              )
        
        self.check_btn = tk.Checkbutton(self,
                                        text= "Enabled",
                                        variable=self.enabled_var,
                                        onvalue = 1,
                                        offvalue = 0,
                                        height=5,
                                        width=20,
                                        command=self.set_entry_state)
        
        self.entry.pack(side=tk.LEFT, expand=True, fill="x")
        self.check_btn.pack(side=tk.LEFT)


    def set_entry_state(self):
        if self.enabled_var.get():
            self.entry.configure(state=tk.NORMAL)
        else:
            self.entry.configure(state=tk.DISABLED)
               
        
        
        
if __name__ == "__main__":
    root = tk.Tk()
    TestApp(root).pack(side="top", fill="both", expand=True)
    root.mainloop()