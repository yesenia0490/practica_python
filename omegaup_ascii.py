#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:03:10 2023

@author: yesenia
"""

lista = list( map(lambda n : int(n), input().split(" ")))

i = 0

texto = ""

while i < len(lista):
    texto += chr(lista[i])
    i += 1

print(texto)