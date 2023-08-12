import requests
import json

if __name__ ==  '__main__':
    url = 'https://www.geekmi.news/__export/1686330720166/sites/debate/img/2023/06/05/axadir_un_txtulo_x14x.jpg_554688468.jpg'

    respuesta = requests.get(url, stream=True)
    with open ('image.jpg', 'wb') as file:
        for chunk in respuesta.iter_content():
            file.write(chunk)
            
    respuesta.close()