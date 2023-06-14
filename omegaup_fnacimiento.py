#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 12:35:23 2023

@author: yesenia
"""
while True:
    fecha = [int(i) for i in input().split("/")]
    if fecha[2]>= 74:
        print(f'{fecha[0]}/{fecha[1]}/19{fecha[2]}')
    else:
        print(f'{fecha[0]}/{fecha[1]}/20{fecha[2]}')

    
    
        
    
    
    
    
    