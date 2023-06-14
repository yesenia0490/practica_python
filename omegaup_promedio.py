#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:22:22 2023

@author: yesenia
"""

n = int(input())
cal = list( map(lambda n : float(n), input().split(" ")))
promedio, reprob , i = 0,0,0
while i < n:
    promedio += cal[i]
    if cal[i] < 6:
        reprob += 1
    i += 1

print(round(promedio/n, 2), reprob)
