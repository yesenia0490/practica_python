#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:51:35 2023

@author: yesenia
"""

a = int(input())

b = int(input())

c = int(input())

mayor = a

if mayor < b:
    mayor = b
elif mayor < c:
    mayor = c
    
print(mayor)
    