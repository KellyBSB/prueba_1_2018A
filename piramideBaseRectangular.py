# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:00:39 2018

@author: José Cortez
"""
#Ingreso de datos
print("**********Cálculo del área de una pirámide de base rectángular**********")
l=float(input("Ingrese el valor del mayor radio en centímetros\n"))
h=float(input("Ingrese el valor de la altura en centímetros\n"))

#Funcion que calcula el volumen de una pirámide de base rectángular
def volCono(l,h):
    
    # Cálculo del volumen de la figura
    volumen=(1/3*(l*l*h))
    
    # Muestra en consola el resultado del volumen
    print("El volumen de la pirámide de base rectángular = "+str(volumen)+" Cm cúbicos ")
    
# Llamado a la función que cálcula el volumen de la piramide de base rectángular
volCono(l,h)