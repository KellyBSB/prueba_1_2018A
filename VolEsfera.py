# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:06:19 2018

@author: Diana Narváez
"""
import math# Biblioteca para operaciones matemáticas

#Ingreso de datos
print("**********Cálculo del volumen de una esfera**********")
R=float(input("Ingrese el valor radio en centimetros\n"))

#Funcion que calcula el volumen de la esfera
def volEsfera(R):
    
    # Cálculo del volumen de la figura
    volumen=((4/3)*(math.pi)*(R**3))
    
    # Muestra en consola el resultado del volumen
    print("El volumen de la Esfera es = "+str(volumen)+" Cm cúbicos ")
    
# Llamado a la función que cálcula de la esfera
volEsfera(R)
