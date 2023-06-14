#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:27:39 2023

@author: yesenia
"""

n_tablas = int(input())
tablas = [int(tabla) for tabla in input().split(" ")]

for i in range(0,n_tablas):
    t = tablas[i]
    for j in range(1, 11):
        print(f'{t}X{j}={t*j}')
    print()
    
    
    
