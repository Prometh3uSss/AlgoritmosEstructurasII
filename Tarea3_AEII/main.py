class Descarga:
    def __init__(self, url, tamano, fecha_inicio, estado):
        self.url = url
        self.tamano = tamano
        self.fecha_inicio = fecha_inicio
        self.estado = estado

    def __str__(self):
        return f"URL: {self.url}, Tamaño: {self.tamano}, Fecha: {self.fecha_inicio}, Estado: {self.estado}"

import json

class HistorialDescargas:
    def __init__(self):
        self.historial_completadas = []
        self.cola_descargas = []

    def cargar_descargas_desde_json(self, archivo_json):
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
            for descarga_data in datos:
                descarga = Descarga(
                    url=descarga_data['url'],
                    tamano=descarga_data['tamano'],
                    fecha_inicio=descarga_data['fecha_inicio'],
                    estado=descarga_data['estado']
                )
                if descarga.estado == 'completada':
                    self.historial_completadas.append(descarga)
                else:
                    self.cola_descargas.append(descarga)
        print("Descargas cargadas correctamente desde el archivo JSON.")

    def mostrar_descargas(self):
        print("\nDescargas en cola (pendientes/en progreso):")
        for descarga in self.cola_descargas:
            print(descarga)
        print("\nDescargas completadas:")
        for descarga in self.historial_completadas:
            print(descarga)

from datetime import datetime
from urllib.parse import urlparse

class Reporte:
    def __init__(self, historial):
        self.historial = historial

    def menu(self):
        while True:
            print("\n--- Menú de Reportes ---")
            print("a. Descargas completadas ordenadas por tamaño (descendente, Quicksort)")
            print("b. Descargas no completadas ordenadas por fecha (ascendente, Mergesort)")
            print("c. Descargas desde fecha y dominio ordenadas por tamaño (ascendente, Heapsort)")
            print("d. Descargas por longitud de URL y estado (descendente, Shellsort)")
            print("e. Salir")
            opcion = input("Seleccione una opción: ").lower()

            if opcion == 'a':
                self.listar_completadas_quicksort()
            elif opcion == 'b':
                self.listar_no_completadas_mergesort()
            elif opcion == 'c':
                self.listar_desde_fecha_dominio_heapsort()
            elif opcion == 'd':
                self.listar_por_url_estado_shellsort()
            elif opcion == 'e':
                break
            else:
                print("Opción inválida.")

    def listar_completadas_quicksort(self):
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr)//2].tamano
            left = [x for x in arr if x.tamano > pivot]
            middle = [x for x in arr if x.tamano == pivot]
            right = [x for x in arr if x.tamano < pivot]
            return quicksort(left) + middle + quicksort(right)
        sorted_list = quicksort(self.historial.historial_completadas)
        print("\nDescargas completadas (ordenadas por tamaño descendente):")
        for d in sorted_list:
            print(d)

    def listar_no_completadas_mergesort(self):
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return self.merge(left, right)
        
        def merge(left, right):
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i].fecha_inicio <= right[j].fecha_inicio:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged
        
        sorted_list = mergesort(self.historial.cola_descargas)
        print("\nDescargas no completadas (ordenadas por fecha ascendente):")
        for d in sorted_list:
            print(d)

    def listar_desde_fecha_dominio_heapsort(self):
        fecha_str = input("Ingrese fecha (YYYY-MM-DD HH:MM:SS): ")
        dominio = input("Ingrese dominio (ej. example.com): ")
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        except:
            print("Formato de fecha incorrecto.")
            return
        
        all_descargas = self.historial.historial_completadas + self.historial.cola_descargas
        filtered = []
        for d in all_descargas:
            d_fecha = datetime.strptime(d.fecha_inicio, "%Y-%m-%d %H:%M:%S")
            d_dominio = urlparse(d.url).netloc
            if d_fecha >= fecha and d_dominio == dominio:
                filtered.append(d)
        
        def heapsort(arr):
            n = len(arr)
            for i in range(n//2 -1, -1, -1):
                self.heapify(arr, n, i)
            for i in range(n-1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                self.heapify(arr, i, 0)
            return arr
        
        sorted_list = heapsort(filtered)
        print(f"\nDescargas desde {fecha_str} en {dominio} (ordenadas por tamaño ascendente):")
        for d in sorted_list:
            print(d)

    def listar_por_url_estado_shellsort(self):
        estado = input("Ingrese estado (completada, pendiente, en_progreso, cancelada): ")
        all_descargas = self.historial.historial_completadas + self.historial.cola_descargas
        filtered = [d for d in all_descargas if d.estado == estado]
        
        def shellsort(arr):
            n = len(arr)
            gap = n // 2
            while gap > 0:
                for i in range(gap, n):
                    temp = arr[i]
                    j = i
                    while j >= gap and len(arr[j - gap].url) < len(temp.url):
                        arr[j] = arr[j - gap]
                        j -= gap
                    arr[j] = temp
                gap //= 2
            return arr
        
        sorted_list = shellsort(filtered)
        print(f"\nDescargas con estado '{estado}' (ordenadas por longitud de URL descendente):")
        for d in sorted_list:
            print(d)

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left].tamano > arr[largest].tamano:
            largest = left
        if right < n and arr[right].tamano > arr[largest].tamano:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

# Ejemplo de ejecución
if __name__ == "__main__":
    historial = HistorialDescargas()
    historial.cargar_descargas_desde_json("C:/Users/Romar/AlgoritmosEstructurasII/Tarea3_AEII/descargas.json")
    reporte = Reporte(historial)
    reporte.menu()