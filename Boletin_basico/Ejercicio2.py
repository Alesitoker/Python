# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 08:33:54 2019

@author: Alejandro
"""

# 2.Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def max_de_tres(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num1 and num2 > num3):
        return num2
    else:
        return num3
print(max_de_tres(1, 2, 3))
print(max_de_tres(2, 7, 1))
print(max_de_tres(4, 1, 2))