#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 20:51:00 2023

@author: yesenia
"""

n = int(input())
numeros = list( map(lambda n : int(n), input().split(" ")))
mayor = numeros[0]
i = 1
while i < n:
    if mayor < numeros[i]:
        mayor = numeros[i]
    i += 1
    
print(mayor)