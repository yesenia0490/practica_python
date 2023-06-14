#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:15:30 2023

@author: yesenia
"""
r1,r2 = input().split()
r1 = float(r1)
r2 = float(r2)

dis_media = (r1 + r2)/2 

aux_dis = int(dis_media)
if dis_media == aux_dis:
    print(aux_dis)
else:
    print(dis_media)
