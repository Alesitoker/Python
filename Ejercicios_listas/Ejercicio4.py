def producto_punto(lista1, lista2):
    total = 0
    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            total += lista1[i]*lista2[i]
    return total


print("(1, 2, 3)*(4, -4, 1) = "+str(producto_punto([1, 2, 3], [4, -4, 1])))