#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 19:59:33 2023

@author: yesenia
"""

def pares (limite):
    
    num = 1
    
    #milista=[]
    
    while num < limite:
    #en su lugar yield
    
        #milista.append(num *2)
    
        yield num * 2
        num += 1
        
    #return milista

regresapares= pares(20)
#print(pares(9))
 
for i in regresapares:
    
    print(i)
    
    
#para que solo te imprima determinadas cifras

print(next(regresapares))