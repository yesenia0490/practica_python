#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:12:34 2023

@author: yesenia
"""

compra = int(input())
pago = 0

if compra > 1000:
    pago = (compra -(compra*0.15))
else:
    pago = (compra)

if pago == int(pago):
    print(int(pago))
else:
    print(pago)

