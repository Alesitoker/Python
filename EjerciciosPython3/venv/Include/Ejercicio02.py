def mayorProducto(num1, num2, num3, num4):
    lista = [num1, num2, num3, num4];
    productoMayor = 0;
    result = 0;

    for i in lista:
        for j in lista:
            if i != j:
                productoMayor = i * j
                if productoMayor > result:
                    result = productoMayor

    return result;

numeros = []

for i in range(4):
    numeros.append(int(input("Introduce numero "+str(i+1)+":")))

print(mayorProducto(numeros[0], numeros[1], numeros[2], numeros[3]))