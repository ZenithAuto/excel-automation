def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        merge_sort(izquierda)
        merge_sort(derecha)
        # Algoritmo de ordenamiento profesional
        print("Ordenando datos de Excel...")