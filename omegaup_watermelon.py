#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:45:59 2023

@author: yesenia
"""

s = int(input())

if  s >= 1 and s <= 100:
    if s % 2 == 0 and s != 2:
        print ("SI")
    else:
        print ("NO")