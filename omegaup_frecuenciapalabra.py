#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:13:50 2023

@author: yesenia
"""

a, b = input().split(" ")
lon = len(a)
total = 0
for i in range(0,lon):
    if a[i]==b:
        total += 1

print(total)
    