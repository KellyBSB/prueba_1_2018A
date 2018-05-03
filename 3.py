# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:26:55 2018

@author: Kelly soto
"""
def decifrarCodigo():
    listaNumeros=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    listaLetras=['t','r','w','a','g','m','y','f','p','d','x','b','n','j','z','s','q','v','h','l','c','k','e']
    listaDeLista=[listaNumeros, listaLetras]
    mensajeClave=[2,5,6,9,8,4,1]
    resultado=['->']
    p=0
    for i in mensajeClave:
         resultado.append(listaDeLista[1][mensajeClave[p]])
         p=p+1
    return resultado
def creartxt():
    archivo3 = open('3.txt', 'w')
    archivo3.close()
def guardartxt():
    resultado= str(decifrarCodigo())
    archivo3 = open('3.txt', 'a')
    archivo3.write(resultado)
    archivo3.close()
def leertxt():
    archivo3 = open('3.txt', 'r')
    linea = archivo3.read()
    print (linea)
    archivo3.close()
creartxt()
guardartxt()
leertxt()