#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 12:30:52 2023

@author: yesenia
"""
def calificaciones():
    examen = int(input())*0.6
    asistencia = int(input())*0.2
    tareas = int(input())*0.2
    return int(examen + asistencia + tareas)

print(calificaciones())