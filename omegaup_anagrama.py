#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:26:04 2023

@author: yesenia
"""

n = int(input())

res = ""

while n > 0:
    estr1,estr2 = "", ""
    estr1,estr2= input().split(" ")
    i,j = 0, 0
    suma1, suma2 = 0, 0
    
    while i < len(estr1):
        suma1 += ord(estr1[i])
        i += 1
        
    while j < len(estr2):
        suma2 += ord(estr2[j])
        j += 1
        
    if suma1 == suma2:
        res += "si\n"
    else: 
        res += "no\n"

    n-=1
    
print(res)