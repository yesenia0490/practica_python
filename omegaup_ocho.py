#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:35:31 2023

@author: yesenia
"""

n_par = 0
n_num = 0

while True:
    n = int(input())
    n_num += 1
    if n % 2 == 0:
        n_par += 1
    if n == 8:
        break;

print(n_num, n_par)
    
