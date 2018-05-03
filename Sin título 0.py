# -*- coding: utf-8 -*-
"""
Created on Wed May  2 22:48:19 2018
Menu de volumenes
@author: José Cortez
"""
def calculoVolumen(n):
    if n == 1:
        import ConoTruncado
        ConoTruncado.volCono
    elif n==2:
        import Cubo
        Cubo.volCubo 
    elif n==3:
        import piramideBaseRectangular
        piramideBaseRectangular.volPiraRec
    elif n==4:
        import PiramideTriangular
        PiramideTriangular.volPirTri
    elif n==5:
        import volEsfera
        volEsfera.volEsfera
    elif n==0:
        return 0
    else:
        print("Opcion ingresada es incorrecta")
        
def menu():
    print("\n ")       
    print("              ***Menu***")
    print("0.-CALCULO DEL VOLUMEN DE UNA SALIR.")
    print("1.-CALCULO DEL VOLUMEN DE UNA ESFERA.")
    print("2.-CALCULO DEL VOLUMEN DE UN CONO TRUNCADO.")
    print("3.-CALCULO DEL VOLUMEN DE UNA CUBO.")
    print("4.-CALCULO DEL VOLUMEN DE UNA PIRAMIDE DE BASE RECTANGULAR.")
    n=int(input("INGRESE UNA DE LAS SIGUIENTES OPCIONES\n"))
    calculoVolumen(n)
n=1  
while not n<0:
    menu()
