from OpcionesDelMenu import *
from utils.InputUtils import *

opcion = ''
opcion1 = 1
opcion2 = 2
opcion3 = 3
opcion4 = 4
opcion5 = 5
salir = 6

while True:
    opcion = inputNumber("1.Crear plato\n"+
    "2.Eliminar Plato\n"+
    "3.Dar de alta o baja\n"+
    "4.Leer la lista de repartidores\n"+
    "5.Crear un pedido\n"+
    "6.Salir\n", "Debes elegir una de las opciones")

    if opcion == opcion1:
        crearPlato()
    elif opcion == opcion2:
        eliminarPlato()
    elif opcion == opcion3:
        while True:
            opcion = inputNumber("1. Alta\n2. Baja\n")
            if opcion == opcion1:
                altaUser()
                break
            elif opcion == opcion2:
                bajaUser()
                break
    elif opcion == opcion4:
        listarRepartidores()
    elif opcion == opcion5:
        crearPedido()
    elif opcion == salir:
        print("Adios")
        break

