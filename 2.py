# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:39:36 2018

@author: Kelly Soto
"""
def cadena():
    cadena = "Esta es la cadena"
    p=-1
    cadenaArreglada=['->']
    for i in cadena:
       cadenaArreglada.append(cadena[p])
       p=p-1
    return cadenaArreglada
  
def creartxt():
    archivo2 = open('2.txt', 'w')
    archivo2.close()
def guardartxt():
    resultado= str (cadena())
    archivo2 = open('2.txt', 'a')
    archivo2.write(resultado)
    archivo2.close()
def leertxt():
    archivo2 = open('2.txt', 'r')
    linea = archivo2.readline()
    print (linea)
    archivo2.close()
creartxt()
guardartxt()
leertxt()