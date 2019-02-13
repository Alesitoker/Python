# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 08:50:32 2019

@author: Alejandro
"""

"""9. Definir una función generar_n_caracteres() que tome un entero n y devuelva el carácter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx"."""

def generar_n_caracteres(num, caracter):
    cadena = ""
    for i in range(num):
        cadena += caracter
    print(cadena)

def generar_n_caracteres_Otra(num, caracter):
    print(num * caracter)

generar_n_caracteres(1800, 'P')
generar_n_caracteres_Otra(18, '+')
