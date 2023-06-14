#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 16:55:28 2023

@author: yesenia
"""

#herencia
class vehiculos():
    
    def __init__(self,marca,modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera= False
        self.frena=False
        
    def arrancar(self):
    
        
        self.enmarcha = True
        
    def acelerar(self):
        
        self.acelera= True
        
    def frenar(self):
        
        self.frena= True
        
        
    def estado(self):
        
        print("\nmarca: ",self.marca,"\nmodelo: ",self.modelo,"\nen marcha:",self.enmarcha,"\nacelera: ",self.acelera,"\nfrena: ",self.frena)
class furgoneta(vehiculos):
    
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return"la furgoneta esta cargada"
        else:
            return"la furgoneta no esta cargada"
            

class moto(vehiculos):
    caballitos = ""
    def caballito(self):
        self.caballitos = "voy haciendo el caballito"
        
       
    def estado(self):
        
        print("\nmarca: ",self.marca,"\nmodelo: ",self.modelo,"\nen marcha:",self.enmarcha,"\nacelera: ",self.acelera,"\nfrena: ",self.frena,"\nva haciendo caballitos",self.caballitos)

class VElectricos():
    def __init__(self):
        self.autonomia = 100
        
    def cargarenergia(self):
        
        self.cargando=True
        
        
mimoto = moto("Honda","CBR")

mimoto.caballito()

mimoto.estado()

mifurgoneta=furgoneta("Renault","kangoo")

mifurgoneta.arrancar()

mifurgoneta.estado()

print(mifurgoneta.carga(True))

class bicicletaelectrica(VElectricos,vehiculos):
    pass

mibici=bicicletaelectricas()
