#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 17:23:23 2023

@author: yesenia
"""

d1, m1 ,a1 = input().split(" ")
d2, m2, a2 = input().split(" ")
d1 = int(d1)
m1 = int(m1)
a1 = int(a1)
d2 = int(d2)
m2 = int(m2)
a2 = int(a2)

if a1 > a2:
    print("primera")
elif a1 == a2 and m1 == m2 and d1 > d2:
    print("primera")
elif a1 == a2 and m1 > m2:
    print("primera")
elif a1 == a2 and m2 > m1:
    print("segunda")
elif a1 ==a2 and m1 == m2 and d2 > d1:
    print ("segunda")
elif a2 > a1:
    print("segunda")
else:
    print("igual")
    


            

