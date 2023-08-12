import requests

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon?limit=151'
    respuesta = requests.get(url)


    if respuesta.status_code == 200:
        contenido =  respuesta.content
        file = open('pokemon.json', 'wb')
        file.write(contenido)
        file.close()

    # if respuesta.status_code == 200:
    #     print(respuesta.content)


