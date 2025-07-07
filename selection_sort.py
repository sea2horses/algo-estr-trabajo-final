def selection_sort(lista):
    # Usaremos la variable inicio para el índice donde
    # empezaremos la sección de búsqueda
    inicio = 0

    # Mientras tengamos una sección de al menos dos elementos
    while(inicio < len(lista) - 1):
        # Aqui almacenaremos el valor más pequeño que hemos encontrado
        # (siempre asumimos que es el primero)
        # para poder intercambiarlo si es necesario
        minimo_indice = inicio

        # Ciclaremos por el arreglo para encontrar el valor mínimo
        for i in range(inicio + 1, len(lista)):
            # Si encontramos un valor más pequeño
            if lista[i] < lista[minimo_indice]:
                # Actualizamos nuestros mínimo
                minimo_indice = i
        
        # Si el mínimo no es el valor inicial, hacemos el cambio
        if minimo_indice != inicio:
            # Cambiamos de posiciones los elementos
            lista[inicio], lista[minimo_indice] = lista[minimo_indice], lista[inicio]
        
        # El valor mínimo ya está el inicio, podemos seguir con el resto del arreglo
        inicio += 1

def selection_sort_recursivo(lista, inicio=0):
    # Si el inicio está en el último elemento o fuera de la lista
    if inicio >= len(lista) - 1:
        return

    # Aqui almacenaremos el valor más pequeño que hemos encontrado
    # (siempre asumimos que es el primero)
    # para poder intercambiarlo si es necesario
    minimo_indice = inicio

    # Ciclaremos por el arreglo para encontrar el valor mínimo
    for i in range(inicio + 1, len(lista)):
        # Si encontramos un valor más pequeño
        if lista[i] < lista[minimo_indice]:
            # Actualizamos nuestro mínimo
            minimo_indice = i

    # Si el mínimo no es el valor inicial, hacemos el cambio
    if minimo_indice != inicio:
        # Cambiamos de posiciones los elementos
        lista[inicio], lista[minimo_indice] = lista[minimo_indice], lista[inicio]
    
    # Recursivamente ordenamos el resto de la lista
    selection_sort_recursivo(lista, inicio+1)

lista = [3,1,12,4,1,-8,90,15,64]
selection_sort_recursivo(lista)
print(lista)