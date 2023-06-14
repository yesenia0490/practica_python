#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 17:00:31 2023

@author: yesenia
"""

n = int(input())

suma = 0

for i in range(1,n+1):
   
    if i % 2 == 0:
        
        suma += i
    else:
       suma -= i
        
print(suma)

