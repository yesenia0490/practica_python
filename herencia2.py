#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 14:04:03 2023

@author: yesenia
"""

#alternativas para pasar parametros
#super()"metodo de la clase padre
class persona():
    def __init__ (self,nombre,edad,lugar_residencia):
        
        self.nombre = nombre
        
        self.edad = edad
        
        self.lugar_residencia = lugar_residencia
        
    def descripcion(self):
        
        print("nombre: ",self.nombre,"edad: ",self.edad,"lugar_residencia: ",self.lugar_residencia)
        
        

class empleado(persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):
        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)
        
        self.salario = salario
        self.antiguedad = antiguedad

def descripcion(self):
    
    super().descripcion()
    print ("salario: ", self.salario,"antiguedad: ", self.antiguedad)        
#yesenia = persona("yesenia",32, "zacatecas")

yesenia = empleado(666,88,66,777,88)
yesenia.descripcion()

    
        
    