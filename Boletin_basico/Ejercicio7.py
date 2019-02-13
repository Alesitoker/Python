# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:20:20 2019

@author: Alejandro
"""

"""7. Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True."""

import Ejercicio6


def es_palindromo(cadena):
    inversar = Ejercicio6.inversa(cadena)
    if inversar == cadena:
        return "Es palindroma"
    else:
        return "No es palindroma"


print(es_palindromo("radar"))
