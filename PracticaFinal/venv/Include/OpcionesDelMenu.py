import os
import re
from utils.InputUtils import *

def listarPlatos():
    file = "./data/Platos.txt"
    emptyPlatos = "No hay platos"
    nombre = ""
    ingredientes = ""
    alergenos = ""
    raciones = ""
    precio = ""
    diccionario = {}

    if os.path.exists(file):
        with open(file, 'r', encoding='utf8') as reader:
            for line in reader:
                nombre = line[line.find(':') + 1:line.find('|')]
                ingredientes = line[line.find('Ingredientes:') + 13:line.find('|A')]
                alergenos = line[line.find('Alergenos:') + 10:line.find('|R')]
                raciones = line[line.find('Raciones:') + 9:line.find('|P')]
                precio = line[line.rfind(':') + 1:]
                diccionario.update({nombre: [ingredientes, alergenos, raciones, precio]})

                print("Nombre: "+nombre+"\nIngredientes: "+ingredientes+"\nAlergenos: "+alergenos+
                      "\nRaciones: "+raciones+"\nPrecio: "+precio+"\n")
        if diccionario:
            return diccionario
    print(emptyPlatos)

def crearPlato():
    file = "./data/Platos.txt"
    fichero = open(file, 'a')
    plato = ""
    nombre = ""
    ingredientes = ""
    alergenos = ""
    raciones = 0
    precio = 0
    errorMsg = "Debe ser un numero entero"
    diccionario = {}

    diccionario = listarPlatos()

    while True:
        nombre = inputString("Introduce el nombre del plato:\n")
        if not diccionario.get(nombre):
            break
        else:
            print("El plato ya existe debe tener otro nombre.\n")
    ingredientes = inputString("Introduce los ingredientes: (separados por coma)\n")
    alergenos = inputString("Introduce los alergenos: (separados por coma)\n")
    raciones = inputNumber("Introduce el numero de raciones:\n")
    precio = inputNumber("Introduce el precio:\n")

    plato = "Nombre:{}|Ingredientes:{}|Alergenos:{}|Raciones:{}|Precio:{}\n".\
        format(nombre, ingredientes, alergenos, raciones, precio)
    fichero.write(plato)
    fichero.close()


def eliminarPlato():
    file = "./data/Platos.txt"
    plato = ""
    platoB = ""
    nombre = ""
    ingredientes = ""
    alergenos = ""
    raciones = 0
    precio = 0
    newList = []

    if not os.path.exists(file) or os.stat(file).st_size == 0:
        print("Debes tener por lo menos un plato para poder eliminar.\n")
    else:
        diccionario = listarPlatos()
        platoB = inputString("Introduce nombre del plato a eliminar:")

        if diccionario.get(platoB):
            for i in diccionario.items():
                nombre = i[0]
                if not nombre == platoB:
                    ingredientes = i[1][0]
                    alergenos = i[1][1]
                    raciones = i[1][2]
                    precio = i[1][3]

                    plato = "Nombre:{}|Ingredientes:{}|Alergenos:{}|Raciones:{}|Precio:{}".\
                        format(nombre, ingredientes, alergenos, raciones, precio)
                    newList.append(plato)

            fichero = open(file, 'w')
            for plato in newList:
                fichero.write(plato)
            print("Plato eliminado satisfactoriamente.")
        else:
            print("El plato no existe, es imposible eliminar")



def altaUser():
    file = "./data/Users.txt"
    fichero = open(file, 'a')
    user = ""
    id = 0
    nombre = ""
    apellidos = ""
    direccion = ""
    tel = ""
    lastUserId = 0
    numTelSize = 9

    lastUserId = getLastUserId()
    id = lastUserId + 1
    nombre = inputString("Introduce el nombre:")
    apellidos = inputString("Introduce los apellidos:")
    direccion = inputString("Introduce la dirección:")
    while True:
        tel = inputNumber("Introduce el numero de telefono:")
        if len(str(tel)) == numTelSize:
            break
    user = "id:{}|Nombre:{}|Apellidos:{}|Direccion:{}|tel:{}\n".\
        format(id, nombre, apellidos, direccion, tel)
    fichero.write(user)

def bajaUser():
    file = "./data/Users.txt"
    userB = ""
    id = ""
    newList = []
    eliminado = False

    if not os.path.exists(file) or os.stat(file).st_size == 0:
        print("Debes tener por lo menos un usuario para poder eliminar.\n")
    else:
        userB = inputString("Introduce id del usuario a eliminar:")

        with open(file, 'r', encoding='utf8') as reader:
            for line in reader:
                id = line[line.find(":")+1:line.find("|")]
                if not userB == id:
                    newList.append(line)
                else:
                    eliminado = True
                    print("Usuario eliminado satisfactoriamente.")
        if eliminado:
            fichero = open(file, 'w')
            for user in newList:
                fichero.write(user)
        else:
            print("El usuario no existe, es imposible eliminar")



def listarRepartidores():
    file = "./data/Repartidores.txt"
    repartidor = ""
    id = ""
    nombre = ""
    apellidos = ""

    if not os.path.exists(file) or os.stat(file).st_size == 0:
        print("No se encuentran repartidores registrados")
    else:
        with open(file, 'r', encoding='utf8') as reader:
            for line in reader:
                id = line[line.find(":")+1:line.find("|")]
                nombre = line[line.find("e:")+2:line.find("|A")]
                apellidos = line[line.find("s:")+2:]

                repartidor = "id: {}\nNombre: {}\nApellidos: {}".\
                    format(id, nombre, apellidos)
                print(repartidor)


def getLastUserId():
    lastLine = ""
    lastId = 0
    file = "./data/Users.txt"
    with open(file, 'r', encoding='utf8') as reader:
        lastLine = reader.readlines()
    if lastLine:
        lastLine = lastLine[-1]
        lastId = int(lastLine[lastLine.find(':')+1:lastLine.find('|')])
    return lastId
