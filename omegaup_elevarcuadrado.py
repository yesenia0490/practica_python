#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:25:19 2023

@author: yesenia
"""

n = int(input())

suma = 0

while n < 30000:
    suma +=1
    n **= 2 #simplificado n = n**2
    
print(n, suma)