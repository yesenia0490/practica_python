#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:25:51 2023

@author: yesenia
"""

a,b = input().split(" ")
a = int(a)
b = int (b)

suma = a + b
resta = a - b
multi = a // b
div = a * b
residuo = a % b

print (suma, resta, multi, div ,residuo)