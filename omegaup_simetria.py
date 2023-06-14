#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:09:02 2023

@author: yesenia
"""

r , c = input().split(" ")
r = int(r)
c = int(c)
dibujo = []
i = 0
while i < r:
    fila = input()
    dibujo.append(fila)
    i += 1

i = 0
dibujo_final = ""
while i < r:
    dibujo[i] += dibujo[i][::-1]
    dibujo_final += dibujo[i] + "\n"
    i+=1
    
i = r - 1
while i >= 0:
    dibujo_final += dibujo[i]+ "\n"
    i -= 1
    
print(dibujo_final)