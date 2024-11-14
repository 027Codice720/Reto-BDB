def process_list(numbers, S):
    # Creamos una lista para almacenar los numeros validos
    processed_numbers = []

    # Iteramos sobre cada número en la lista de entrada
    for num in numbers:
        # Variable auxiliar para almacenar los dígitos válidos del número actual
        filtered_digits = ""
        # Iteramos sobre cada dígito del número convirtiéndolo a cadena
        for d in str(num):
            if int(d) < S:  # Comprobamos si el dígito es menor que S
                filtered_digits += d  # Concatenamos el dígito válido

        # Si existen dígitos válidos, añadimos el número procesado a la lista
        if filtered_digits:
            processed_numbers.append(int(filtered_digits))
    
    #Creamos una lista para imprimir los valores de atras hacia adelante
    result_numbers = []
    for i in range(len(processed_numbers)-1,-1,-1):
        result_numbers.append(processed_numbers[i])

    # Devolver la lista ordenada
    return result_numbers
    

# Entradas
numbers =  [60, 6, 5, 4, 3, 2, 7, 7, 29, 1]
S = 5

# Llamada a la función
result = process_list(numbers, S)
print(f"Resultado: {result}")
