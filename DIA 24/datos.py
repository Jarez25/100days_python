def datos (*args, **kwargs):
    print(args)
    print(kwargs)
    
    
usuario = {'nombre':'javier', 'apellido':'gomez'}


datos (10,50,60, **usuario)