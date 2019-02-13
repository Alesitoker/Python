"""5. Crea un programa que pida al usuario introducir su edad.
La edad no puede ser negativa, mayor a 120 y no numérica,
en esos casos lanzar la excepción correspondiente.
Atrápala y vuelve a pedir la edad hasta que sea correcta.
El código no debe parar su ejecución hasta que el usuario introduzca una edad correcta."""

noValido = True
edad = 0

while noValido:
    try:
        edad = int(input("Introduce edad:"))
        try:
            if edad >= 120:
                raise ValueError("La edad no puede superar 120")
            elif edad < 0:
                raise ValueError("La edad tiene que ser positiva")
            else:
                noValido = False
        except ValueError as e:
            print(e)
    except ValueError:
        print("El valor introducido debe ser numerico")