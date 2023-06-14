#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:01:17 2023

@author: yesenia
"""

a,b,c =input().split(" ")
a = int(a)**2
b = int(b)**2
c = int(c)**2

if a + b == c:
    print ("SI")
else:
    print ("NO")