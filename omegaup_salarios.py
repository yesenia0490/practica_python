#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:37:05 2023

@author: yesenia
"""

def salario_normal(h,pago):
    return h*pago

def extra(h,pago,vcs):
    salario1 = pago * 40
    salario2 = pago * ((h-40)*vcs)
    return salario1 + salario2


def inicio():
    hrs, pago = [float(i)for i in input().split(" ")]
    if hrs <= 40:
        print(salario_normal(hrs,pago))
    elif hrs < 50:
        print(extra(hrs,pago,1.5))
    else:
        print(extra(hrs,pago,2))
        
inicio()
        
        
    


