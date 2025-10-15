# -*- coding: utf-8 -*-
import requests as rs
from woocommerce import API

# Configuración de WooCommerce API
wcapi = API(
    url="http://telegran.test",  # Cambia esto a tu URL local de WordPress
    consumer_key="ck_16e6900c7bb7eae06702a478c8b3e455a00623a1",
    consumer_secret="cs_950614640a36fceb309c61141a16106db9afe11b",
    version="wc/v3"
)


def get_card(url="https://db.ygoprodeck.com/api/v7/cardinfo.php", offset=0):
    # Parámetros de solicitud
    params = {"num": 20, "offset": offset}

    try:
        respuesta = rs.get(url, params=params)

        if respuesta.status_code == 200:
            payload = respuesta.json()
            resultado = payload.get("data", [])

            if resultado:
                for card in resultado:
                    card_id = card.get("id")
                    name = card.get("name")
                    description = card.get("desc", "Sin descripción")
                    human_readable_card_type = card.get(
                        "humanReadableCardType", "Sin categoría")
                    archetype = card.get("archetype", "Sin arquetipo")
                    price = card.get("card_prices", [{}])[
                        0].get("tcgplayer_price", "1.99")
                    image_url = card.get("card_images", [{}])[
                        0].get("image_url")

                    # Crear el producto en WooCommerce
                    create_product_in_woocommerce(
                        card_id=card_id,
                        name=name,
                        description=description,
                        price=price,
                        category=human_readable_card_type,
                        tags=[archetype],
                        image_url=image_url
                    )
                    print(f"Producto '{name}' creado en WooCommerce.")

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


def create_product_in_woocommerce(card_id, name, description, price, category, tags, image_url):
    # Obtener o crear categoría en WooCommerce
    category_id = get_or_create_category(category)

    # Obtener o crear etiquetas en WooCommerce
    tag_ids = [get_or_create_tag(tag) for tag in tags]

    data = {
        "name": name,
        "type": "simple",
        "regular_price": str(price),
        "description": description,
        "sku": str(card_id),  # Usar el ID de la carta como SKU
        "categories": [{"id": category_id}] if category_id else [],
        "tags": [{"id": tag_id} for tag_id in tag_ids if tag_id],
        "images": [{"src": image_url}],  # Agregar la imagen de la carta
        "manage_stock": True,
        "stock_quantity": 10  # Ajustar la cantidad en inventario
    }

    try:
        response = wcapi.post("products", data).json()
        if 'id' in response:
            print(f"Producto '{name}' añadido exitosamente con SKU {card_id}.")
        else:
            print("Error al añadir el producto:", response)
    except Exception as e:
        print("Error al conectar con WooCommerce:", e)


def get_or_create_category(category_name):
    # Obtener categorías actuales de WooCommerce
    categories = wcapi.get("products/categories").json()

    for cat in categories:
        if cat['name'].lower() == category_name.lower():
            return cat['id']

    # Si la categoría no existe, crearla
    new_category = wcapi.post("products/categories",
                              {"name": category_name}).json()
    return new_category.get("id")


def get_or_create_tag(tag_name):
    # Obtener etiquetas actuales de WooCommerce
    tags = wcapi.get("products/tags").json()

    for tag in tags:
        if tag['name'].lower() == tag_name.lower():
            return tag['id']

    # Si la etiqueta no existe, crearla
    new_tag = wcapi.post("products/tags", {"name": tag_name}).json()
    return new_tag.get("id")


if __name__ == '__main__':
    get_card()
