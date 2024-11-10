# -*- coding: utf-8 -*-

import requests as rs

if __name__ == '__main__':
    url = 'http://httpbin.org/cookies'
    galleta = {'my-cookie': 'true'}

    respuesta = rs.get(url, cookies=galleta)

    if respuesta.ok:
        galleta = respuesta.cookies.get_dict()
        print(galleta)

        print(respuesta.content)
