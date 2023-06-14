#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:06:36 2023

@author: yesenia
"""

a = int(input())
b = int(input())
c = int(input())

menor = a

if b < a:
    menor = b
elif c < b:
    menor = c


print(menor)
    