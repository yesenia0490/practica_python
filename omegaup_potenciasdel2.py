#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 21:22:59 2023

@author: yesenia
"""

n = int(input())

i = 0

while i < 100:
    if 2**i == n:
        print (i)
        break;
    i += 1