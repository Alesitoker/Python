def calcularDesglose(cantidad):
    valor = cantidad
    result = 0;
    lista = [500, 200, 100, 50, 20, 10, 5 , 2, 1]
    diccionario = {}

    for i in lista:
        result = int(valor / i)
        if result > 0:
            valor = valor % i
            diccionario.update({i:result})

    return diccionario

def obtenerDesglose(cantidad):
    desglose = calcularDesglose(cantidad)
    plurarBillete = ""
    plurarEuro = ""

    for i in desglose:
        if desglose.get(i) == 1:
            plurarBillete = " billete"
        else:
            plurarBillete = " billetes"

        if i == 1:
            plurarEuro = " euro"
        else:
            plurarEuro = " euros"

        print(str(desglose.get(i)) + plurarBillete + " de " + str(i) + plurarEuro)

cantidad = int(input("Introduce la cantidad de dinero:"))
obtenerDesglose(cantidad)