#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:38:13 2023

@author: yesenia
"""
#estado inicial= caracteristicas comunes de objetos
#propiedades
class coche():
    
  #metodo constructor init encapsulacion __
    def __init__(self):
    
        self.__largoChasis=2600
        self.__anchoChasis=1250
        self.__ruedas=4
        self.__enmarcha=False
        self.__color = "rojo"
        self.__eso = 2900
    
    
    #comportamiento   #metodo
    def arrancar(self,arrancamos):
        
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
        
        if(self.__enmarcha and chequeo):
            return"el coche esta en marcha"
            
        elif(self.__enmarcha and chequeo == False):
            return "algo esta mal. no podemos arrancar"
        
        else:
            return"el coche esta parado"
            
        

    def estado(self):
        print("el coche tiene: ", self.__ruedas,"ruedas., un ancho de :", self.__anchoChasis,"y un largo de ",
              self.__largoChasis)
        
    def __chequeo_interno(self):
        print("realizando chequeo interno")
         
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        
        if(self.gasolina =="ok" and self.aceite == "ok" and self.puertas == "cerradas"):
        
            return True
        
        else:
            
            return False
            
        


#instanciarunaclase
micoche=coche()

print(micoche.arrancar(True))

micoche.estado()

print("a continuacion creamos el segundo objeto")

micoche2=coche()


print(micoche2.arrancar(False))

(micoche2.estado())

