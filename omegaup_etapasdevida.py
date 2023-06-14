#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 16:24:00 2023

@author: yesenia
"""

edad= int(input())

if edad >= 0 and  edad <= 3:
    print("BEBE")
elif edad >=4 and edad <= 14:
    print("NINO")
elif edad >=15 and edad <= 18:
    print("JOVEN")
elif edad >=19 and edad <= 65:
    print("ADULTO")
else:
    print("ADULTO 3RA")