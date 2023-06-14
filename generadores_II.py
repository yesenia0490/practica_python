#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 20:56:17 2023

@author: yesenia
"""

def devuelve_ciudades(*ciudades):
    
    for elemento in ciudades:
        
        yield elemento
        
devuelve_ciudades=devuelve_ciudades("México","canada",)
#un print para imprimir cada ciudad
print(next(devuelve_ciudades))

print(next(devuelve_ciudades))
return"operación errónea"

op1 = (int(input("introduce el primer numero: ")))
op2 =(int(input("introduce el segundo numero: ")))
operacion = input("introduce la operacion a realizar(suma,resta,multiplicacion,division); ")


if operacion == "suma":
    print (suma(op1,op2))

elif operacion =="resta":
    print(resta(op1,op2))
    
elif operacion == multi