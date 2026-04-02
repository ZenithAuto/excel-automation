def merge_sort(lista):
    # Caso base: si la lista tiene 0 o 1 elementos, ya está ordenada
    if len(lista) <= 1:
        return lista

    # 1. Dividir la lista en dos mitades
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # 2. Llamada recursiva para ordenar cada mitad
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    # 3. Mezclar las mitades ordenadas
    return mezclar(izquierda, derecha)

def mezclar(izq, der):
    resultado = []
    i = j = 0

    # Comparar elementos y agregar el mayor al resultado (orden descendente)
    while i < len(izq) and j < len(der):
        if izq[i] > der[j]:  # Cambiar '>' por '<' para orden ascendente
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    # Agregar los elementos restantes de ambas listas
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado

# Ejemplo de uso
numeros = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(numeros)

print(f"Lista original: {numeros}")
print(f"Lista ordenada (Mayor a Menor): {lista_ordenada}")