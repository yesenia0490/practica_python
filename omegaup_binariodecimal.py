#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 11:07:45 2023

@author: yesenia
"""
b = input()

decimal = 0

i = len(b)-1

pot = 0 

while i >= 0:
    decimal += int(b[i]) *(2**pot)
    pot +=1
    i -= 1

print(f'{b}={decimal}')
    
    
