def contarInicial(lista, inicial):
    contador = 0;
    for i in lista:
        if i[0].upper() == inicial.upper():
            contador = contador + 1
    print(contador)

letra = str(input("Introduce la inicial: "))
contarInicial(["Aiala", "Napoleón", "Valentina", "Izan", "Arhane"], letra)