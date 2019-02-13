def listaDeListas(lista):
    mat = ""
    for i in lista:
        for j in i:
            mat += str(j)+" "
        print(mat)
        mat = ""

def enPosition(lista, row, column):
    contadorI = 0
    contadorJ = 0

    for i in lista:
        if contadorI == row-1:
            for j in i:
                if contadorJ == column-1:
                    print(i[contadorJ])
                contadorJ += 1
        contadorI += 1
    if contadorI > row:
        print('No se ha encontrado nigun elemento en esa posicion')

lista = [[1, 2, 7], [3, 4], [6, 9, 4, 2, 4]]
listaDeListas(lista)
print("-----------------------------------------------------------")
enPosition(lista, 1, 0)