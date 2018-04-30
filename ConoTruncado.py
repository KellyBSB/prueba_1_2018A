# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:06:08 2018
"Calculo de el volumen de un cono truncado"
@author: José Cortez
"""

import math# Biblioteca para operaciones matemáticas

#Ingreso de datos
print("**********Cálculo del área de un Cono Truncado**********")
R=float(input("Ingrese el valor del mayor radio en centimetros\n"))
r=float(input("Ingrese el valor del menor radio en centimetros\n"))
h=float(input("Ingrese el valor de la altura en centimetros\n"))

#Funcion que calcula el volumen de un cono truncado
def volCono(R,r,h):
    
    # Cálculo del volumen de la figura
    volumen=((1/3)*(math.pi)*(h)*(R**2+r**2+R*r))
    
    # Muestra en consola el resultado del volumen
    print("El volumen de el Cono Truncado es = "+str(volumen)+" Cm ")
    
# Llamado a la función que cálcula el volumen de un cono truncado
volCono(R,r,h)

