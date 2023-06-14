#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 18:03:54 2023

@author: yesenia
"""

compra = float(input())

if compra < 500:
    print(compra)
elif compra <= 1000:
    print(compra - (compra*(0.05)))
elif compra <= 7000:
    print(compra -(compra*(0.11)))
elif compra <= 15000:
    print(compra - (compra*(0.18)))
else:
    print(compra - (compra*(0.25)))