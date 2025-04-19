import os
import pandas as pd
from woocommerce import API

# Verificar el directorio actual
print("Directorio actual:", os.getcwd())

# Configuración de WooCommerce API
wcapi = API(
    url="http://woocomertest.test",  # Cambia esto a tu URL local de WordPress
    consumer_key="ck_a6966a362b7e0d41bfefe104c77aa1171d525d66",
    consumer_secret="cs_d256414cdef91bbad160621ffa336c167754074b",
    version="wc/v3"
)


def read_excel_and_create_products(file_path):
    # Leer el archivo Excel
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return

    # Procesar cada fila en el DataFrame
    for index, row in df.iterrows():
        card_id = row.get("ID")
        name = row.get("Name")
        description = row.get("Description", "Sin descripción")
        category = row.get("Category", "Sin categoría")
        price = row.get("Price", "1.99")
        image_url = row.get("Image URL", "")

        # Crear el producto en WooCommerce
        create_product_in_woocommerce(
            card_id=card_id,
            name=name,
            description=description,
            price=price,
            category=category,
            tags=[category],  # Usamos la categoría como etiqueta también
            image_url=image_url
        )
        print(f"Producto '{name}' creado en WooCommerce.")


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
    # Ruta relativa si está en la misma carpeta que el código
    file_path = 'cartas_productos.xlsx'
    read_excel_and_create_products(file_path)
