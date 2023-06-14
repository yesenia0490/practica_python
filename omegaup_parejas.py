#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 19:47:02 2023

@author: yesenia
"""
n = int(input())

res = ""

i = 0

while i < n:
    n1, n2 = input().split(" ")
    suma = int(n1)+ int(n2)
    res += str(suma) + "\n"
    i += 1
    
print (res)