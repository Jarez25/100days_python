# -*- coding: utf-8 -*-
import requests as rs


def get_card(url="https://db.ygoprodeck.com/api/v7/cardinfo.php", offset=0):
    # los paramentros de soolicitud se definen como num para dar el numero limitado de recursos en este caso 2
    params = {"num": 20, "offset": offset}
    # lo campos son num para definir una lista de usuario enumerad y el offset es uno de lo parametros de respuesta

    try:
        respuesta = rs.get(url, params=params)

        if respuesta.status_code == 200:
            payload = respuesta.json()
            resultado = payload.get("data", [])

            if resultado:
                for card in resultado:
                    name = card.get("name")
                    if name:
                        print(name)

                next_step = input("¿Continuar Listado? [Y/N]: ").lower()
                if next_step == "y":
                    get_card(offset=offset + 20)
                else:
                    print("Listado detenido.")
            else:
                print("No hay más cartas para mostrar.")
        else:
            print("Error en la solicitud:", respuesta.status_code)
    except Exception as e:
        print("Error en la conexión:", e)


if __name__ == '__main__':
    get_card()
