from productos import obtener_producto

def calcular_total(lista_productos):
    """ Calcular el total de la compra. """
    total = 0
    for producto in lista_productos:
        total += producto['precio']
        return calcular_total
    