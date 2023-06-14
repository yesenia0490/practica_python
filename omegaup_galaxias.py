#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:01:34 2023
 
@author: yesenia
"""

a, b, c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

re = ""

if a < b:
    re += "True "
else:
    re += "False "
    
if c > a:
    re += "True "
else:
    re += "False "
    
if a == b:
    re += "True "
else:
    re += "False "
    
if a != c:
    re += "True "
else:
    re += "False"

if c <= b:
    re += "True "
else:
    re += "False "
    
    
print(re)
    