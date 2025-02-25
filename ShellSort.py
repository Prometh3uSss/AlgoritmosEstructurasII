def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicializar el gap

    # Comenzar con el gap y reducirlo
    while gap > 0:
        # Realizar una ordenación por inserción con el gap
        for i in range(gap, n):
            temp = arr[i]  # Elemento a insertar
            j = i

            # Mover los elementos que están gap posiciones por delante
            # de la posición actual hacia la derecha
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp  # Colocar el elemento en su posición correcta

        gap //= 2  # Reducir el gap

# Ejemplo de uso
lista = [8, 5, 3, 7, 6, 2, 4, 1]
shell_sort(lista)
print("Lista ordenada:", lista)