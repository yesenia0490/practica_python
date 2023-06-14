#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:18:04 2023

@author: yesenia
"""

w = int(input())

palabras=[]

for i in range(0,w):
    palabras.append(input())#append = "+="
    
menor = palabras[0]
for i in range(1,w):
    if len(menor) > len(palabras[i]):
        menor = palabras[i]
print(menor)
print(len(menor))
if len(menor) % 2 == 0:
    print("par")
else:
    print("impar")
    
    
    
    
    