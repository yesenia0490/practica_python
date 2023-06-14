#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:29:35 2023

@author: yesenia
"""

ph = int(input())

if ph >= 0 and ph <= 6:
    print("Acido")
elif ph >=7 and ph <= 13:
    print("Neutro")
elif ph == 14:
    print("Base")
else:
    print("Are you kidding me?")