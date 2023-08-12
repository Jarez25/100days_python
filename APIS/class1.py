import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/get?nombre=jarez&curso=python'
    args = {'nombre' : 'Jairo', 'curso' : 'Java', 'nivel' : 'intermedio'}

    respuesta = requests.get(url, params=args)
    print(respuesta.url)


    if respuesta.status_code == 200:
        contenido =  respuesta.content
        print(contenido)


