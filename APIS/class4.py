import requests
import json

if __name__ == '__main__':
    # url = 'http://httpbin.org/post/put'
    url = 'http://httpbin.org/post/delete'
    payload = {'nombre': 'Jairo', 'curso': 'Java', 'nivel': 'intermedio'}
    headers = {'Conten-Type':  'application/json', 'access-token':  '12345'}

    respuesta = requests.delete(url, data=json.dumps(payload), headers=headers)

    # get :  obtiene los recursos
    # post : para crear los recursos
    # put : para actualizarlos
    # delete : para eliminar

    # json post se encarga de seralizar los parametros
    # data nosotros serealizamos los parametros
    print(respuesta.url)

    if respuesta.status_code == 200:
        # print(respuesta.content)
        headers_res = respuesta.headers
        # print(headers_res)
        server = headers_res['server']
