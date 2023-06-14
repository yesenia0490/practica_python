#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:03:37 2023

@author: yesenia
"""
i = 0
cambio = ""
while i < 5:
    costo,pago = input().split(" ")
    costo = float(costo)
    pago = float (pago)
    cambio = str(pago - costo)+ "\n"
    i +1
    

print(cambio)