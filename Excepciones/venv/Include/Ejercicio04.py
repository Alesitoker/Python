"""4. Crea una función own_sqrt(x),
que reciba un número entero y realice las validaciones necesarias (
x no sea negativa, x sea numérica) para poder calcular la raíz cuadrada, en otro caso que lance una excepción.

Busca una función para calcular la raíz cuadrada, ¿qué librería debes importar?"""
import math
def own_sqrt(x):
    try:
        math.sqrt(x)
    except ValueError:
        print("El tipo del valor es incorrecto debe ser numerico")
    except TypeError:
        print("El numero tiene que ser positivo")

own_sqrt(-2)
own_sqrt("sadad")