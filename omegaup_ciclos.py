#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 17:49:14 2023

@author: yesenia
"""

def suma(n, a_b):
    i = 1
    while i <= a_b:
        n += i
        i += 1
    return n
    
n, a, b = input().split(" ")
n = int(n)
a = int(a)
b = int(b)

while n < 1000:
    if n % 2 == 0:
        n += suma(n,a)
    else:
        n += suma (n,b)

print(n)

