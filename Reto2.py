def squared_sorted_array(array, S):
    # Definimos el rango máximo permitido
    max_range = int(str(S) + str(S))  # Concatenar S consigo mismo y convertir a entero

    # Lista para almacenar cuadrados válidos
    squared_array = []
    
    # Validar y calcular cuadrados
    for num in array:
        square = num * num  # Calcular el cuadrado
        if 0 <= square <= max_range:  # Verificar que esté dentro del rango
            squared_array.append(square)

    # Ordenar con Bubble Sort
    n = len(squared_array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if squared_array[j] > squared_array[j + 1]:  # Comparar y ordenar ascendente
                temp = squared_array[j]
                squared_array[j] = squared_array[j + 1]
                squared_array[j + 1] = temp
    return squared_array

S = 5 
array = [-6, -5, 0, 5, 6]
result = squared_sorted_array(array, S)
print(f"Entrada: {array} -> Resultado: {result}")