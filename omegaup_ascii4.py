#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 14:14:16 2023

@author: yesenia
"""



i = 0

nombre = input()

while i <= 3 and i < len(nombre):
    print(f'{nombre[i]} ASCII value is {ord(nombre[i])}')
    i += 1
