#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:53:02 2023

@author: yesenia
"""

a = int(input())

if a >= 0 and a <= 3:
    print("BEBE")
elif a >= 4 and a <= 14:
    print("NINO")
elif a >= 15 and a <= 18:
    print("JOVEN")
elif a >= 19 and a <= 65:
    print("ADULTO")
else:
    print("ADULTO 3RA")
    
    