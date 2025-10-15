class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def ArbolBinario(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        ArbolBinario(nodo.izquierda)
        ArbolBinario(nodo.derecha)


def OrdenarArbol(nodo):
    if nodo:
        OrdenarArbol(nodo.izquierda)
        print(nodo.valor, end=" ")
        OrdenarArbol(nodo.derecha)


def ArbolBinarioInverso(nodo):
    if nodo:
        ArbolBinarioInverso(nodo.derecha)
        ArbolBinarioInverso(nodo.izquierda)
        print(nodo.valor, end=" ")


if __name__ == "__main__":
    raiz = Nodo(10)
    raiz.izquierda = Nodo(5)
    raiz.derecha = Nodo(15)
    raiz.izquierda.izquierda = Nodo(3)
    raiz.izquierda.derecha = Nodo(7)
    raiz.derecha.izquierda = Nodo(12)
    raiz.derecha.derecha = Nodo(18)

    print("Recorrido Preorden:")
    ArbolBinario(raiz)
    print("\nRecorrido Inorden:")
    OrdenarArbol(raiz)
    print("\nRecorrido Postorden:")
    ArbolBinarioInverso(raiz)
