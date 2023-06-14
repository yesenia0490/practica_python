#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 18:48:59 2023

@author: yesenia
"""

a, b = input().split(" ")
a = int(a)
b = int(b)



for i in range(a,b+1):
    if i % 3 == 0 and i % 5 == 0:
        print("BuzzFizz")
    elif i % 3 == 0:
        print("Buzz")
    elif i % 5 == 0:
        print("Fizz")
    else:
        print(i)