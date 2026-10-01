"""Vamos a crear una función de rotación circular. Consiste en una rotación de n números en una dirección (izquierda o derecha) de una determinada lista.

Por ejemplo, la siguiente lista:

lista = [2, 4, 1, 3, 7, 9]

Se le aplicaría f(lista, 2, right) y tendría la siguiente salida:

return [7, 9, 2, 4 , 1, 3]"""


def rotar_lista(lista, n, direccion="right"):
    if not lista:
        return []


    n = n % len(lista)

    if n == 0:
        return list(lista)

    if direccion == "right":

        return lista[-n:] + lista[:-n]
    elif direccion == "left":
        return lista[n:] + lista[:n]

lista = [2, 4, 1, 3, 7, 9]
resultado = rotar_lista(lista, 2, "right")
print(resultado)



def rotar_lista(lista, n, direccion="right"):
    if not lista:
        return []

    n = n % len(lista)

    if n == 0:
        return list(lista)

    if direccion == "right":
        return lista[-n:] + lista[:-n]

    elif direccion == "left":
        return lista[n:] + lista[:n]

    else:
        print("Direccion no valida, usa right o left")
        return list(lista)


lista = [2, 4, 1, 3, 7, 9]

resultado = rotar_lista(lista, 3, "left")
print("Lista rotada:", resultado)
"""Pullrequest hacia Chenqi, revisado por Oscar, esta todo correcto ✅ lo unico modificado es que he añadido un else
en caso que el usuario escriba algo distinto a right o left"""