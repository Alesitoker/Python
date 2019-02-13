# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:01:40 2019

@author: Alejandro
"""
num = 0
lista = []

while num >= 0:
    num = int(input("Ingrese numero: "))
    if num >= 0:
        lista.append(num)
print(lista)