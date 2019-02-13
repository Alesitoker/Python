# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:11:54 2019

@author: Alejandro
"""


def countAp(lista, cadena):
    contador = 0
    for i in lista:
        if i == cadena:
            contador += 1
    return contador


print(countAp(['bollitos', 'bollito', 'bollititos', 'Bollito', 'bollito'], 'bollito'))
