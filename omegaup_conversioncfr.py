#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:22:11 2023

@author: yesenia
"""
import math

c = int(input())


k = math.trunc(c + 273.15)


f = math.trunc((c*(9/5))+32)


r = math.trunc((c*(4/5))/5)

print(f'{k} {f} {r}')

