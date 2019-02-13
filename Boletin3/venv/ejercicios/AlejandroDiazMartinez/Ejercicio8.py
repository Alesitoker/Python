def contar_vocales(cadena):
    contA = 0
    contE = 0
    contI = 0
    contO = 0
    contU = 0

    for i in cadena:
        if i.upper() == "A":
            contA = contA + 1
        elif i.upper() == "E":
            contE = contE + 1
        elif i.upper() == "I":
            contI = contI + 1
        elif i.upper() == "O":
            contO = contO + 1
        elif i.upper() == "U":
            contU = contU + 1
    if contA == 1:
        print("La letra a aparece " + str(contA) + " vez")
    else:
        print("La letra a aparece " + str(contA) + " veces")
    if contE == 1:
        print("La letra e aparece " + str(contE) + " vez")
    else:
        print("La letra e aparece " + str(contE) + " veces")
    if contI == 1:
        print("La letra i aparece " + str(contI) + " vez")
    else:
        print("La letra i aparece " + str(contI) + " veces")
    if contO == 1:
        print("La letra o aparece " + str(contO) + " vez")
    else:
        print("La letra o aparece " + str(contO) + " veces")
    if contU == 1:
        print("La letra u aparece " + str(contU) + " vez")
    else:
        print("La letra u aparece " + str(contU) + " veces")


print("Introduce una palabra:")
cadena = str(input())
contar_vocales(cadena)