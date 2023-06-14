#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 20:57:35 2023

@author: yesenia
"""

numeros = list( map(lambda n :int(n), input().split(" ")))


i = 1
menor = numeros[0]
mayor = numeros[0]


while i < len(numeros):
    if menor > numeros[i]:
        menor = numeros[i]
        
    if mayor < numeros[i]:
        mayor = numeros[i]
    i+=1  
print(menor,mayor)
        
        
    