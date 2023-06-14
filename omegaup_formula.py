#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 21:02:32 2023

@author: yesenia
"""

x, y, z = input().split(" ")
x = float(x)
y = float(y)
z = float(z)

condicion = (x >= 1 and x <= 100 and y >= 1 and y <= 100 and z >= 1 and z <= 100)

if condicion:
    formula = (((2*x + y)/z)*(y**3 - z))
    
    formula /=(((x + 2*y + 3*z)/(z - 2*y - 3*x))+ x**2 + z**2)
    print(formula)