# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 08:39:29 2019

@author: Alejandro
"""

# 3.Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def esVocal(vocal):
    result = False
    if (vocal == 'a' or vocal == 'A'):
        result = True
    elif (vocal == 'e' or vocal == 'E'):
        result = True
    elif (vocal == 'i' or vocal == 'I'):
        result = True
    elif (vocal == 'o' or vocal == 'O'):
        result = True
    elif (vocal == 'u' or vocal == 'U'):
        result = True
    return result

print(esVocal('a'))
print(esVocal('e'))
print(esVocal('i'))
print(esVocal('o'))
print(esVocal("u"))
print(esVocal("g"))
print(esVocal("A"))
print(esVocal("E"))
print(esVocal("I"))
print(esVocal("O"))
print(esVocal("U"))
