#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:41:20 2023

@author: yesenia
"""

n = input()
lon = len(n)
suma = 0
for i in range(0,lon):
    suma += int(n[i])
     
print(suma)
