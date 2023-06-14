#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:31:14 2023

@author: yesenia
"""

intensidad, a = input().split(" ")
resistencia, h = input().split(" ")

intensidad = int(intensidad)
resistencia = int(resistencia)

voltios = (intensidad) * (resistencia)
#print(voltios,"V"+1)

