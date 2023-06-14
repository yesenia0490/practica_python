#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 22:16:52 2023

@author: yesenia
"""

x = float(input())

y = ((x + (x**2)) / ((5*x)+3))+x
y*=((x + (x**2))/((5*x)+3)) / ((x+(x**2))/((5*x)+3)+(2*x))
print (y) 