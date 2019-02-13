diccionario = {}

def introducirHumanos():
    diccionario = {}
    contador = 0
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    dniSize = 9
    dni = ""
    nombre = ""

    while contador < 4:
        while True:
            dni = input("Introduce el DNI:")
            if len(dni) == dniSize and dni[0:8].isnumeric() and dni[-1].isupper() and letras.find(dni[-1]) != -1:
                break;

        nombre = str(input("Introduce el nombre:"))
        diccionario.update({dni: nombre})
        contador += 1
    return diccionario

def consultar(diccionario, dni):
    return diccionario.get(dni)

diccionario = introducirHumanos()
print(diccionario)

print(consultar(diccionario, str(input())))

