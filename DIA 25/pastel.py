class pastel:
    def __init__(self, ingredientes) -> None:
        self.ingredientes = ingredientes
    
    def __repr__(self):
         return f'pastel({self.ingredientes !r})'
        
    @classmethod
    def Pastel_chovcoloate(cls):
        return cls(['harina','leche','chcolate'])#atributos del metodo
    
    @classmethod
    def Pastel_vainilla(cls):
        return cls(['harina', 'leche', 'vainilla'])
    
print(pastel.Pastel_chovcoloate())