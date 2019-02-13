# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 12:30:42 2019

@author: Alejandro
"""

"""
10. Definir un histograma procedimiento() que tome una lista de números enteros e 
imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) 
debería imprimir lo siguiente: 
**** 
********* 
*******
"""

def procedimiento(lista):
    cadena = ""
    for i in lista:
        for j in range(i):
            cadena += '*'
        print(cadena)
        cadena = ""
        
procedimiento([4, 9, 7])