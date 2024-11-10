import requests
import json
import urllib.parse

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'nombre' : 'Jairo', 'curso' : 'Java', 'nivel' : 'intermedio'}
    headers = {'Conten-Type' :  'application/json', 'access-token' :  '12345'}

    respuesta = requests.post(url, data = json.dumps(payload), headers = headers) 

    #json post se encarga de seralizar los parametros
    #data nosotros serealizamos los parametros 
    print(respuesta.url)


    if respuesta.status_code == 200:
        print(respuesta.content)
        headers_res = respuesta.headers
        #print(headers_res)
        server = headers_res['server']
        print(server)

