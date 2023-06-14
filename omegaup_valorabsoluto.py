#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:11:53 2023

@author: yesenia
"""

a,b =input().split(" ")
a = int(a)
b = int(b)
suma = (a + b)
if suma < 0:
    print (suma*-1)
else:
    print (suma)