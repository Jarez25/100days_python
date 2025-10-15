# -*- coding: utf-8 -*-
import requests as rs
from woocommerce import API


wcapi = API(
    url="http://woocomertest.test",  
    consumer_key="ck_758e23a228b97539e94ec86cdb416e6179247810",
    consumer_secret="cs_d8abf301d44e10bd224823648ad0d67e0e2281f5",
    version="wc/v3"
)


def get_card(url="https://db.ygoprodeck.com/api/v7/cardinfo.php"):
    try:
        respuesta = rs.get(url)

        if respuesta.status_code == 200:
            payload = respuesta.json()
            resultado = payload.get("data", [])

            if resultado:
                for card in resultado:
                    card_id = card.get("id")
                    name = card.get("name")
                    description = card.get("desc", "Sin descripción")
                    human_readable_card_type = card.get(
                        "type", "Sin categoría")
                    archetype = card.get("archetype", "Sin arquetipo")
                    price = card.get("card_prices", [{}])[
                        0].get("tcgplayer_price", "1.99")
                    image_url = card.get("card_images", [{}])[
                        0].get("image_url")

                    # Crear o actualizar el producto en WooCommerce
                    create_or_update_product_in_woocommerce(
                        card_id=card_id,
                        name=name,
                        description=description,
                        price=price,
                        category=human_readable_card_type,
                        tags=[archetype],
                        image_url=image_url
                    )
                    print(f"Producto '{name}' procesado en WooCommerce.")
            else:
                print("No hay más cartas para mostrar.")
        else:
            print("Error en la solicitud:", respuesta.status_code)
    except Exception as e:
        print("Error en la conexión:", e)


def create_or_update_product_in_woocommerce(card_id, name, description, price, category, tags, image_url):
    # Verificar si el producto ya existe usando el SKU
    existing_product = find_product_by_sku(card_id)

    if existing_product:
        # Actualizar producto existente
        update_product_in_woocommerce(
            existing_product['id'], name, description, price, category, tags, image_url)
    else:
        # Crear un nuevo producto
        create_product_in_woocommerce(
            card_id, name, description, price, category, tags, image_url)


def find_product_by_sku(sku):
    try:
        response = wcapi.get("products", params={"sku": sku}).json()
        return response[0] if response else None
    except Exception as e:
        print("Error al buscar el producto:", e)
        return None


def update_product_in_woocommerce(product_id, name, description, price, category, tags, image_url):
    category_id = get_or_create_category(category)
    tag_ids = [get_or_create_tag(tag) for tag in tags]

    data = {
        "name": name,
        "regular_price": str(price),
        "description": description,
        "categories": [{"id": category_id}] if category_id else [],
        "tags": [{"id": tag_id} for tag_id in tag_ids if tag_id],
        "images": [{"src": image_url}],
        "manage_stock": True,
        "stock_quantity": 10  # Ajustar la cantidad en inventario
    }

    try:
        response = wcapi.put(f"products/{product_id}", data).json()
        if 'id' in response:
            print(f"Producto '{name}' actualizado exitosamente con ID {
                  product_id}.")
        else:
            print("Error al actualizar el producto:", response)
    except Exception as e:
        print("Error al conectar con WooCommerce:", e)


def create_product_in_woocommerce(card_id, name, description, price, category, tags, image_url):
    category_id = get_or_create_category(category)
    tag_ids = [get_or_create_tag(tag) for tag in tags]

    data = {
        "name": name,
        "type": "simple",
        "regular_price": str(price),
        "description": description,
        "sku": str(card_id),
        "categories": [{"id": category_id}] if category_id else [],
        "tags": [{"id": tag_id} for tag_id in tag_ids if tag_id],
        "images": [{"src": image_url}],
        "manage_stock": True,
        "stock_quantity": 10
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
    categories = wcapi.get("products/categories").json()

    for cat in categories:
        if cat['name'].lower() == category_name.lower():
            return cat['id']

    new_category = wcapi.post("products/categories",
                              {"name": category_name}).json()
    return new_category.get("id")


def get_or_create_tag(tag_name):
    tags = wcapi.get("products/tags").json()

    for tag in tags:
        if tag['name'].lower() == tag_name.lower():
            return tag['id']

    new_tag = wcapi.post("products/tags", {"name": tag_name}).json()
    return new_tag.get("id")


if __name__ == '__main__':
    get_card()
