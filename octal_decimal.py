#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 11:48:31 2023

@author: yesenia
"""

o = input()

i = len(o)-1

octal = 0

potencia = 0 

while i >= 0:
    octal += int(o[i])*(8**potencia)
    potencia += 1
    i -=1

print(f'{o}={octal}')