#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 11:33:00 2023

@author: yesenia
"""

num = int(input())

n = ""

i = 1

while i <= (num**2):
    if i % 2 == 0:
        n += "0"
    else:
        n += "1"
        
    if i % num == 0:
        n += "\n"
    i +=1
    
print(n)
