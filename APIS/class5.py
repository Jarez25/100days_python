import requests

if __name__ == '__main__':
    url = 'https://www.geekmi.news/__export/1686330720166/sites/debate/img/2023/06/05/axadir_un_txtulo_x14x.jpg_554688468.jpg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'
    }
    
    respuesta = requests.get(url, headers=headers, stream=True)
    if respuesta.status_code == 200:
        with open('image.jpg', 'wb') as file:
            for chunk in respuesta.iter_content(chunk_size=8192):
                file.write(chunk)
        print("Imagen descargada correctamente.")
    else:
        print("Error al descargar la imagen:", respuesta.status_code)
    respuesta.close()
