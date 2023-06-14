#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 13:17:39 2023

@author: yesenia
"""

r = int(input())

lista_re = list( map(lambda n : int(n), input().split(" ")))

np = int(input())

i = 0

res = ""

while i < np:
    p = int(input())
    res += str(lista_re[p-1]) + "\n"
    i +=1
    

print (res)


    
    
    
    