# Kelly Soto
import math#
def volCono():
    print("**********Cálculo del volumen de un Cono Truncado**********")
    R = float(input("Ingrese el valor del mayor radio en centímetros\n"))
    r = float(input("Ingrese el valor del menor radio en centímetros\n"))
    h = float(input("Ingrese el valor de la altura en centímetros\n"))

    volumen = ((1 / 3) * (math.pi) * (h) * (R ** 2 + r ** 2 + R * r))
    print("El volumen de el Cono Truncado es = " + str(volumen) + " Cm cúbicos ")


def volCubo():
    print("**********Cálculo del volumen de un Cubo**********")
    l = float(input("Ingrese el valor de la longuitud del lado\n"))
    volumen = (l ** 3)
    print("El volumen del Cubo es = " + str(volumen) + " Cm cúbicos ")


def volCono():

    print("**********Cálculo del volumen de una pirámide de base rectángular**********")
    l = float(input("Ingrese el valor del mayor radio en centímetros\n"))
    h = float(input("Ingrese el valor de la altura en centímetros\n"))

    volumen = (1 / 3 * (l * l * h))
    print("El volumen de la pirámide de base rectángular = " + str(volumen) + " Cm cúbicos ")


print ('1. Cubo' , '\n2. Piramide de base rectangualar ', '\n3. Volumen de un cono truncado' )
opcion = (int(input(' Escoja una de las opciones: ')))
if(opcion==1):
    print ('Este es el calculo de un Cubo')
    volCubo()
elif(opcion == 2):
     print('Este es el calculo de una Piramide de base rectangular')
     volCono()
elif(opcion == 3):
    print('Este es el calculo de un Volumen de un cono truncado')
    volCono()