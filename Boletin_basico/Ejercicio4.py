# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 09:02:41 2019

@author: Alejandro
"""

# 4. Definir una función que calcule la longitud de una lista o una cadena dada.
def calLongitud(longitud):
    contador = 0
    for i in longitud:
        contador+=1
    print(contador)
    
calLongitud([1, 2, 3])
calLongitud("hola")
