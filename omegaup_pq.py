#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:43:22 2023

@author: yesenia
"""

p, q = [int(i)for i in input().split(" ")]

formula = (p**3)+(q**4)-(2*(p**2))

if formula <= 680:
    print(f'{p}\n{q}')
