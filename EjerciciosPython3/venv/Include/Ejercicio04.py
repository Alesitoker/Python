def insertarCursos(cursos):
    curso = ""
    profesor = ""
    maxAlumnos = 0
    salir = 0
    volverAPedir = True
    seguir = True

    while seguir:
        while volverAPedir:
            curso = str(input("Introduce el curso:"))
            profesor = str(input("Introduce el profesor:"))
            maxAlumnos = int(input("Introduce el numero maximo de alumnos:"))

            if salir > 1:
                for i in cursos:
                    if i[0] == profesor:
                        volverAPedir = True
                        print("El profesor ya imparte en otro curso\n.")
                    else:
                        volverAPedir = False
            else:
                volverAPedir = False


        cursos.update({curso:[profesor, maxAlumnos]})
        salir = int(input("¿Salir de la insercion de cursos?\n-1.Si\n-2.No\n"))
        if  salir == 1:
            seguir = False
        else:
            volverAPedir = True

def eliminarCurso(cursos, cursoAEliminar):
    result = ""
    for i in cursos.keys():
        if i == cursoAEliminar:
            result = cursos.pop(cursoAEliminar)
            print("Curso eliminado satisfactoriamente")
            break
    if result == "":
        print("El curso "+cursoAEliminar+" no se ha podido eliminar\n")

def listarCursos(cursos):
    for i in cursos.items():
        print("Nombre del curso: "+i[0])
        print("Profesor: "+i[1][0])
        print("Numero maximo de alumnos: "+str(i[1][1])+"\n")

cursos = {"cursito":["mapa",23], "aguacate":["pepe",45]}
salir = 0
opcion = 0
cursoEliminar = ""

insertarCursos(cursos)
while True:
    while True:
        opcion = int(input("-1.Insertar cursos\n-2.Listar cursos\n-3.Eliminar curso\n"))
        if opcion == 1 or opcion == 2 or opcion == 3:
            break

    if opcion == 1:
        insertarCursos(cursos)
    elif opcion == 2:
        listarCursos(cursos)
    elif opcion == 3:
        cursoEliminar = str(input("¿Que curso quieres eliminar?"))
        eliminarCurso(cursos, cursoEliminar)
    salir = int(input("¿Salir?\n-1.Si\n-2.No\n"))
    if salir == 1:
        print("Adios")
        break
