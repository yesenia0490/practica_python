#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:38:01 2023

@author: yesenia
"""

years = list( map(lambda n : int(n), input().split(" ")))
res = ""
i = 0
while i < 4:
    if (years[i]% 4 == 0 and years[i] %100 != 0) or (years[i]% 400 == 0):
        res += "29 "
    else:
        res += "28 "
    i+=1
    
print(res)