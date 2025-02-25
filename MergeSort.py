def merge_sort(arr):
    if len(arr) > 1:
        # Encontrar el punto medio de la lista
        mid = len(arr) // 2
        
        # Dividir la lista en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamar recursivamente a merge_sort en ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializar índices para recorrer las mitades
        i = j = k = 0

        # Combinar las mitades
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Comprobar si quedan elementos en la mitad izquierda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Comprobar si quedan elementos en la mitad derecha
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Ejemplo de uso
lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista)
print("Lista ordenada:", lista)
