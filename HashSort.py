def hash_sort(arr):
    if not arr:
        return []

    # Determinar el rango de los valores
    min_value = min(arr)
    max_value = max(arr)
    
    # Crear la tabla hash
    hash_table_size = max_value - min_value + 1
    hash_table = [None] * hash_table_size

    # Insertar elementos en la tabla hash
    for num in arr:
        hash_table[num - min_value] = num

    # Recuperar los elementos en orden
    sorted_list = [num for num in hash_table if num is not None]

    return sorted_list

# Ejemplo de uso
lista = [4, 2, 7, 1, 3]
lista_ordenada = hash_sort(lista)
print("Lista ordenada:", lista_ordenada)