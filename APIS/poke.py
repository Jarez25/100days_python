import requests as rs

respuesta = rs.get("https://pokeapi.co/api/v2/pokemon?limit=151")


for name in respuesta:
    print(f'{name}\n')

#print(respuesta)
#print(respuesta.json())
#print(respuesta.json())