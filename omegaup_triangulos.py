#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:55:57 2023

@author: yesenia
"""

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

if a == b and b == c:
    print("equilatero")
elif a == b or b == c or a == c:
    print("isosceles")
elif a != b and b != c:
    print("escaleno")

