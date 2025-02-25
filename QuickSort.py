
def quicksort(arr):
    if len(arr) <= 1:  # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Elegir el pivote (en este caso, el elemento del medio)
        left = []   # Lista para elementos menores que el pivote
        middle = [] # Lista para elementos iguales al pivote
        right = []  # Lista para elementos mayores que el pivote

        # Particionar la lista
        for x in arr:
            if x < pivot:
                left.append(x)  # Agregar a la lista de elementos menores
            elif x == pivot:
                middle.append(x)  # Agregar a la lista de elementos iguales
            else:
                right.append(x)  # Agregar a la lista de elementos mayores

        # Combinar las listas
        return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso
lista = [3, 6, 8, 10, 1, 2, 1]
lista_ordenada = quicksort(lista)
print(lista_ordenada)  # Salida: [1, 1, 2, 3, 6, 8, 10]