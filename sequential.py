# Busqueda Secuencial (se asume que el arreglo está ordenado)
def busqueda_secuencial_ordenada(lista, valor):
    # i es nuestra variable de contador
    i = 0 # O(1)
    while i < len(lista) and lista[i] <= valor: # O(n)

        if lista[i] == valor: # O(1)
            return True # O(1)

        # Sumamos a i
        i += 1 # O(1)
    # Ciclamos por toda la lista y no encontramos el valor
    return False # O(1)

# Busqueda Secuencial (se asume que el arreglo está ordenado)
def busqueda_secuencial_ordenada_recursiva(lista, valor, indice=0):
    # Si ya pasamos el final de la lista y no hemos encontrado el elemento, retornamos falso
    if indice >= len(lista):
        return False
    
    # Si el valor actual es mayor al valor buscado, ya no lo encontraremos
    # ya que estamos en un arreglo ordenado
    if lista[indice] > valor:
        return False
    
    # Si encontramos el valor, retornamos verdadero
    if lista[indice] == valor:
        return True
    
    # Si ninguna condición de fin se dió, buscaremos en el índice siguiente
    # de manera recursiva
    return busqueda_secuencial_ordenada_recursiva(lista, valor, indice+1)

lista = [1,5,8,12,16,22,67]
valor_a_buscar = 13
print(f"Lista: {lista}, Valor a buscar: {valor_a_buscar}")
print(f"Búsqueda resolvió a {busqueda_secuencial_ordenada_recursiva(lista, valor_a_buscar)}")