#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 23 18:43:36 2023

@author: yesenia
"""
n =int(input())

alum_cal = {}

while n > 0:
    name = input()
    cal = float(input())
    if cal >=0 and cal<= 100:
        alum_cal[name]= cal
        n-=1
    else:
        while cal > 100 or cal < 0:
            print("UPS, ERROR!, DIGITE DE NUEVO LA CALIFICACION DE",name)
            cal = float(input())
        alum_cal[name] = cal
        n -= 1


def promedio(alum_cal):
    calif = alum_cal.values()
    promedio = sum(calif)
    lon = len(calif)
    
    return promedio/lon
    
if cal < 60:
    
    


