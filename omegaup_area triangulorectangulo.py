#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 20:28:44 2023

@author: yesenia
"""

b = float(input())
c= float(input())

a = ((c**2) - (b**2))**0.5

perimetro = a + b + c

area = (a*b)/2
print (perimetro)
print (area)