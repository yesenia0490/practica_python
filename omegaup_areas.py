#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:13:23 2023

@author: yesenia
"""

a = int(input())

if a == 0:
    bm, bmn, al =[float(n)for n in input().split(" ")]
    area =round(((bm+bmn)/2)*al,3)
    print(f'Trapecio \n{area}')
elif a == 1:
    b, al = [float(n)for n in input().split(" ")]
    area = round((b * al)/2,3)
    print(f'Triangulo\n{area}')
elif a == 2:
    l = float(input())
    area = round(l*l,3)
    print(f'Cuadrado\n{area}')
elif a == 3:
    b , alt =[float(n)for n in input().split(" ")]
    area = round(b*alt,3)
    print(f'Rectangulo\n{area}')
elif a == 4:
    pi, r = [float(n) for n in input().split(" ")]
    area = round((pi*r)**2,3)
    print (f'Circulo\n {area}')
else:
    print("Figura no valida")
    
    
