numero = 1
menos = 0
paises = ["Afghanistan","Albania","Algeria","Andorra","Angola","Anguilla","Antigua and Barbuda","Argentina","Armenia","Aruba","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bermuda","Bhutan","Bolivia","Bosnia & Herzegovina""Botswana","Brazil","British Virgin Islands","Brunei","Bulgaria","Burkina Faso","Burundi","Cambodia","Cameroon","Cape Verde","Cayman Islands","Chad","Chile","China","Colombia","Congo","Cook Islands","Costa Rica","Cote D Ivoire","Croatia","Cruise Ship","Cuba","Cyprus","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor L'Este","Togo","Tonga","Trinidad & Tobago","Tunisia","Turkey","Turkmenistan",
"Turks & Caicos","Uganda","Ukraine","United Arab Emirates","United Kingdom","Uruguay","Uzbekistan","Venezuela","Vietnam","Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]

lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]

for i in range (7, 15):
    print(f' los numero son {i}')
    

while numero <= 14:
    print(f'estos numeros son {numero}')
    numero += 1
    

for i in range (0, -5001, -500):
    print(f'valor de los de 500 {i}')
    
while menos >= -5000:
    print(f'el valor de informatica {menos}' )
    menos -= 500
    
for pais  in paises:
    print(f'--{pais}--')
    
lista_numeros.sort()

for numero in lista_numeros:
    if numero == 10:
        continue
    elif numero == 356:
        break
    else:
        print(f'el valor del elemento es {numero}')