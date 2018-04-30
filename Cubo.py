# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 22:34:38 2018

@author: José Cortez
"""
#Ingreso de datos
print("**********Cálculo del área de un Cubo**********")
l=float(input("Ingrese el valor de la longuitud del lado\n"))

#Función que cálcula el volumen del cubo
def volCubo(l):
    
    # Cálculo del volumen de la figura
    volumen=(l**3)
    
    # Muestra en consola el resultado del volumen
    print("El volumen del Cubo es = "+str(volumen)+" Cm cúbicos ")
    
# Llamado a la función que cálcula el volumen del cubo
volCubo(l)
