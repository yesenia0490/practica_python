#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 22:57:30 2023

@author: yesenia
"""
res = ""
n = int (input())
for i in range(1 , n +1):
    if i % 2 == 0:
        res += str(i) + " "
        
if len(res)== 0:
    print("Nada que imprimir")
else:
    print(res)
    
        