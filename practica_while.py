#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 19:23:01 2023

@author: yesenia
"""

i = 3

while i <= 10:
    print("ejecucion " + str(i))
    i += 1
    
print("terminó la ejecución" )

print("hola")





edad = int(input("intruduce tu edad: "))

while edad < 5 or edad > 100:
    print("edad negativa")
    edad = int(input("intruduce tu edad; "))
    
print("edad del aspirante " + str ( edad))


import math
print("programa sw calculo para raiz cuadrada")
numero = int(input("introduce un numero por favor: "))

intentos = 0

while numero < 0 :
    print("no se puede encontrar raiz de numero negativo")
    
    if intentos == 3:
        print(" demasiados intentos. programa finalizado")
        break;
        #excepcion
    try:
    
    numero = int(input("introduce un numero por favor: "))
    if numero < 0:
        intentos += 1
    except ZeroDivisionError
    return"operación erronea"
        
if intentos < 2:
    solucion = math.sqrt(numero)
    print ("la raiz cuadrado de " + str(numero) + "es" + str(solucion))
        
    