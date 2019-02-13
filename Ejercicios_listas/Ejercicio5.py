def contarYRemover(lista, elemento):
    contador = 0
    posiciones = ""

    for i in range(len(lista)):
        if lista[i] == elemento:
            posiciones += str(i)
            if posiciones != "":
                posiciones += ", "
            contador += 1

    if contador == 1:
        print("El elemento se encuentra en la posicion: "+posiciones)
    elif contador > 1:
        print("El elemento se encuentra en las posiciones: "+posiciones)
    print("El elemento aparece: " + str(contador))

    for i in range(contador):
        lista.remove(elemento)


lista = [1, 2, 3, 4, 1, 5, 6, 1, 7, 1, 9, 2]

contarYRemover(lista, 1)
print("La lista: " + str(lista))