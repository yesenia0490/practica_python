#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:48:36 2023

@author: yesenia
"""

a, b, c, = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

x1 = (-b + (((b**2)-(4*a*c))**0.5)) /(2*a)

x2 = (-b - (((b**2)-(4*a*c))**0.5)) /(2*a)

if x1 == int(x1):
    x1 = int(x1)
if x2 == int(x2):
    x2 = int(x2)
print(x1,x2)