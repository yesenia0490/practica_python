#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 20:15:10 2023

@author: yesenia
"""

puntos = 0

i = 0

while i < 5:
    compra = int(input())
    if compra >= 1000 and compra < 3000:
        puntos += 100
    elif compra >= 3000:
        puntos += 500
    
    i += 1

if puntos >= 2000:
    print("SE OBTIENE DESCUENTO")
else:
    print("NO SE OBTIENE DESCUENTO")

