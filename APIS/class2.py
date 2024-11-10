import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = {'nombre': 'Jairo', 'curso': 'Java', 'nivel': 'intermedio'}

    respuesta = requests.get(url, params=args)
    print(respuesta.url)

    if respuesta.status_code == 200:
        # respuesta_json = respuesta.json()
        # origin = respuesta_json['origin']
        # print(origin)
        respuesta_json = json.loads(respuesta.text)
        origin = respuesta_json['origin']
        print(origin)
