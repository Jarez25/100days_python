def hola(nombre="Covadonga"):
    def saluda():
        return "Estás dentro de la función saluda()"

    def bienvenida():
        return "Estás dentro de la función bienvenida()"

    if nombre == "Covadonga":
        return saluda
    else:
        return bienvenida

a = hola()

print(a)

print(a())
