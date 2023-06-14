#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 12:24:14 2023

@author: yesenia
"""
import math

f = int(input())

c = math.ceil((f-32)*(5/9))



if c <= 36:
    print(c, "0" )
else:
    print(c, "1")
    


