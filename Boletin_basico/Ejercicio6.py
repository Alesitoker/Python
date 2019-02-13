# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:07:49 2019

@author: Alejandro
"""

""" 6. Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena estoy probando debería devolver la cadena odnaborp yotse """

def inversa(cadena):
    inversa = ""
    for i in range(len(cadena), 0, -1):
        inversa += cadena[i-1]
    return inversa

if __name__ == '__main__':
    print(inversa("estoy probando"))