def heapify(arr, n, i):
    largest = i  # Inicializar el nodo más grande como raíz
    left = 2 * i + 1  # Índice del hijo izquierdo
    right = 2 * i + 2  # Índice del hijo derecho

    # Verificar si el hijo izquierdo es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verificar si el hijo derecho es mayor que el nodo más grande hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el nodo más grande no es la raíz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar

        # Recursivamente heapificar el subárbol afectado
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir un max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno del heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar
        heapify(arr, i, 0)  # Heapificar el árbol reducido

# Ejemplo de uso
lista = [4, 10, 3, 5, 1]
heap_sort(lista)
print("Lista ordenada:", lista)