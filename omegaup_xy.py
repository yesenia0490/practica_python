#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:19:16 2023

@author: yesenia
"""

x = int(input())
y = int(input())
suma =""

for i in range(x,y+1):
    if i % 3 == 0:
        suma += str(i) + "\n"

print(suma)
       
    
    
    