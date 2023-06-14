#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:20:31 2023

@author: yesenia
"""

a, b, = input().split(" ")
a = int(a)
b = int(b)

a *= 300 #es lo mismo a = a * 300
b *= 1500

h = round(b / a,1)
print(h) 