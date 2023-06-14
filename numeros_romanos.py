#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 23:03:13 2023

@author: yesenia
"""
v_rom ={1000:"M",900:"CM", 500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}

valores = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

n_romanos = ""

n = int(input())

i = 0

if n <=3:
    n_romanos= "I"*n
else:
    while n != 0:
        if n >= valores[i]:
            n_romanos += v_rom[valores[i]]*(n//valores[i])
            n %= valores[i]
        else:
            i += 1
                
print(n_romanos)

