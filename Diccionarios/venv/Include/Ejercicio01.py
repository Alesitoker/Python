def agenda():
    seguir = True
    diccionario = {}
    while seguir:
        nombre = str(input("Introduce el nombre:"))
        tel = int(input("Introduce el telefono:"))
        diccionario.update({nombre:tel})
        salir = input("Introduce -1 para salir, cualquier cosa para continuar:")
        if salir.isnumeric() and int(salir) == -1:
            seguir = False
    return diccionario

print(agenda())