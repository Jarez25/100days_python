# dias de repaso

parrafo = 'este es un texto'
texto = 'este es un parrafo'
numero = 1
numero_dos = 2

print(f'hola {parrafo} y  {texto}')

print(' '.join([parrafo,texto]))
print(' '.join([parrafo,texto,parrafo,texto])) #
print('*'.join([parrafo,texto,parrafo,texto]))
#print('*'.join([parrafo,numero])) aqui ni se pueden mescalr int con str
#print('*'.join([numero, numero_dos])) al parecer join no admite int
print('%s %s' % (texto, parrafo))
print('%s %s' % (texto, numero))
print('%i %i' % (numero, numero_dos))
print('%i + %i' % (numero, numero_dos)) #no puedo sumar de esta manera

print('{}'.format(parrafo, texto))
print('{} {}'.format(parrafo, texto))
print('{}'.format(parrafo, texto))

mensaje = 'Aquí hay un ejemplo'
'de como cambiar el ancho'
'de una imagen al pasar sobre ella'

mensaje2 = ('Aquí hay un ejemplo'
'de como cambiar el ancho'
'de una imagen al pasar sobre ella')


print(mensaje)
print(mensaje2)
print((texto+' ')*3)

for letra in texto:
    print(letra)