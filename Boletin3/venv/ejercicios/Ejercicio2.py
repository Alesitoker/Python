"""2. Escribir una función filtrar_palabras() que tome una lista de palabras y
un entero n, y devuelva las palabras que tengan más de n caracteres."""

def filtrar_palabras(lista, long):
    maxLong = []
    for i in lista:
        if len(i) > long:
            maxLong.append(i)
    return maxLong

lista = ["pollo", "pollito", "Holita", "eretu", "jar", "zip", "kiri"]
print(filtrar_palabras(lista, 4))