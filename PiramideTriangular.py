# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 22:48:33 2018

@author:Diana Narváez
"""
import math# Biblioteca para operaciones matemáticas

#Ingreso de datos
print("**********Cálculo del volumen de un pirámide de base triángular (regular)**********")
l=float(input("Ingrese el valor del lado en centímetros\n"))
h=float(input("Ingrese el valor de la altura en centímetros\n"))

#Función que calcula del volumen de una pirámide de base triángular(regular)
def volPirTri(l,h):
    
    # Cálculo del volumen de la figura
    volumen=(math.sqrt(3)*(1/12)*(l**2)*h)
    
    # Muestra en consola el resultado del volumen
    print("El volumen pirámide de base triángular (regular) = "+str(volumen)+" Cm cúbicos ")
    
# Llamado a la función que cálcula el volumen de una pirámide de 
#base triángular (regular)
volPirTri(l,h)
