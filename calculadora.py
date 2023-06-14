#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 18:19:19 2023

@author: yesenia
"""

def calculadora(num1,num2,oper):
    if oper == "+":
        num1 += num2
    elif oper == "-":
        num1 -= num2
    elif oper == "/":
        num1 /= num2
    elif oper == "*":
        num1 *= num2
    return num1

print("bienvenidos a mi calculadora")
num1 = float(input())
op = input()
while True:
    num2 = float(input())
    num1 = calculadora(num1,num2,op)
    sprint (num1) 
    op = input()
        