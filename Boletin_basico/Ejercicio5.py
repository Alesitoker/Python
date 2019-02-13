# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 09:08:18 2019

@author: Alejandro
"""

""" 
5. Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente 
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) 
debería devolver 24.
"""

def sum(lista):
    result = 0
    for i in lista:
        result += i
    print(result)
    
def multip(lista):
    result = 1
    for i in lista:
        result *= i
    print(result)

sum([1,2,3,4])
multip([1,2,3,4])