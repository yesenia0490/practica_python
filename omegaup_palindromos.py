#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:03:14 2023

@author: yesenia
"""

palabra1 = input()

i = len(palabra1)-1

palabra2 = ""

while i >= 0:
    palabra2 += palabra1[i]
    i -=1

if palabra1 == palabra2:
    print("SI")
else: 
    print("NO")