#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:06:47 2023

@author: yesenia
"""

n = int(input())

lista = [int(i)for i in input().split(" ")]
i = 0
j =len(lista)-1
res = ""

while i < (len(lista)/2):
    aux = lista[i]+lista[j]
    res += str(aux)+" "
    i += 1
    j -= 1
print(res)

                        