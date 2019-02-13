def traducir(palabra):
    diccionario = {'avocado':'aguacate', 'colors':'colores'}
    return diccionario.get(palabra)

print(traducir(str(input("Introduce palabra:"))))