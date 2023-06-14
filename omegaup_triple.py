#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 14:48:37 2023

@author: yesenia
"""

n = int(input())

res = ""

resultado = 0

for i in range(1,n+1):
    a = int(input())
    if a % 3 == 0:
        resultado += 1
        res += str(i)+" "

if resultado == 0:
    print("no hay triples")
else:
    print(str(resultado)+"\n"+res)
    
    