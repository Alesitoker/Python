"""1. Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga."""

def mas_larga(lista):
    maxLong = "";
    for i in lista:
        if len(maxLong) < len(i):
            maxLong = i
    return maxLong

print(mas_larga(["uno", "dos", "tres", "Soy la mas larga de todas"]))
