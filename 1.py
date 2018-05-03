# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:06:09 2018

@author: Kelly Soto
"""
def convercion():
    binario = [1,1,0,1,0,1]
    potencia= len(binario)
    print ('esta es la potencia', potencia)
    p=0
    exadecimal=0
    for i in binario: 
        exadecimal1=(binario[p]*(2**(potencia-1)))
        p=p+1
        potencia=potencia-1
        exadecimal=exadecimal+exadecimal1
        print (exadecimal)
  
    return ('El numero binario es ', binario, ' = ', exadecimal, ' exadecimal')
   
def creartxt():
    archivo1 = open('1.txt', 'w')
    archivo1.close()
def guardartxt():
    resultado = str(convercion())
    archivo1 = open('1.txt', 'a')
    archivo1.write(resultado)
    archivo1.close()
def leertxt():
    archivo1 = open('1.txt', 'r')
    linea = archivo1.read()
    print (linea)
    archivo1.close()
creartxt()
guardartxt()
leertxt()