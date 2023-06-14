#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 11:10:11 2023

@author: yesenia
"""

medidas = [int(v) for v in input().split(" ")]



valores = [3.785, 0.946, 0.473, 0.236, 0.029 ]

litros = 0
for i in range(0,5):
    litros += medidas[i]*valores[i]
resultado = ""
 
for i in range(0,5):
    if (i+1) % 2 == 1:

        aux = litros/valores[i]
        print(litros,valores[i])
    else:
        aux = int(litros/valores[i])
    
    resultado += str(aux) +" "
    litros = litros % valores[i]*1.1

print(resultado)

    
