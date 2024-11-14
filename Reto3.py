def minimum_unmakeable_change(coins):
    # Ordenar las monedas
    coins.sort()
    print (f"Organizos: {coins}")
    # Inicializar el cambio máximo que podemos generar
    current_change_created = 0

    # Iterar sobre las monedas
    for coin in coins:
        # Si la moneda actual es mayor que el cambio que podemos crear + 1, encontramos el resultado
        if coin > current_change_created + 1:
            return current_change_created + 1
        # Actualizar el cambio máximo que podemos generar
        current_change_created += coin

    # Devolver el resultado final si todas las monedas se pueden combinar
    return current_change_created + 1


# Ejemplos de prueba
coins = [5, 1, 1, 1, 10, 15, 20, 100]

print(f"Con monedas {coins}, no se puede crear: {minimum_unmakeable_change(coins)}")

