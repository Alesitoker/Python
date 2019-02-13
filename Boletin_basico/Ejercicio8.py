# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:26:05 2019

@author: Alejandro
"""

"""8. Definir una función superposicion() que tome dos listas y 
devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
Escribir la función usando el bucle for anidado."""

def superposicion(lista1, lista2):
    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    return False

print(superposicion([1,2,3,4,5], [7,8,2,9,1]))
print(superposicion([1,2,3,4,5], [7,7,7,8]))