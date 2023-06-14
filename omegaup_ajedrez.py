#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:03:27 2023

@author: yesenia
"""

posicion = input()
letra = ord(posicion[0])
num = int(posicion[1])
           

if num >= 1 and num <= 8 and letra >= 65 and letra <= 72:
    if (num % 2 == 0 and letra % 2 == 0) or(num % 2 != 0 and letra % 2 != 0 ):
        print("NEGRA")
    else:
        print("BLANCA")
        
        
