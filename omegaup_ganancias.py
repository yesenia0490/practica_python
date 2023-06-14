#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:41:49 2023

@author: yesenia
"""

ganancias = int(input())
perdidas = int(input())

negocio = (ganancias - perdidas)

if ganancias > perdidas:
    print("El negocio si va a jalar",negocio)
else:
    print("Dejalo ya esta muerto",negocio)
