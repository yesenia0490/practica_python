#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:48:33 2023

@author: yesenia
"""

a , b = input().split(" ")
a = int(a)
b = int(b)
resultado = 0
diferencia = (a - b)
if diferencia < 0:
    print(diferencia * (-1))
else:
    print(diferencia)