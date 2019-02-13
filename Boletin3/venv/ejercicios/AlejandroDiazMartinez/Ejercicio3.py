"""3. Escribir un programa que le diga al usuario que ingrese una cadena.
El programa tiene que evaluar la cadena y decir cuántas letras mayúsculas tiene."""

def evaluarCadena(cadena):
    contador = 0
    for i in cadena:
        if i.isupper():
            contador += 1
    return contador

print("Introduce una cadena:")
cadena = str(input())

print("La cadena tiene:"+str(evaluarCadena(cadena))+"letras mayúsculas")