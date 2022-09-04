# ejercicio numero 8 ecuacion de primer grado

from math import sqrt


print("------------------------------------------------------------------------")
print("---asigne los valores para resolver a siguiente ecuacion: ax^(2)+bx+c---")
print("------------------------------------------------------------------------")

#input

a= int(input("ingrese el valor de a: "))
b= int(input("ingrese el valor de b: "))
c= int(input("ingrese el valor de c: "))

#proseccing

x1 =(a+ sqrt(b^(2)-4*a*c))/2*a

x2 =(a- sqrt(b^(2)-4*a*c))/2*a

#output

print("el primer resultado es: "+str(x1))
print("el primer segundo es: "+str(x2))