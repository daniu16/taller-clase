# ejersicio numero 10 numeros en orden

from xml.etree.ElementTree import ProcessingInstruction


print("----------------------------------------------------")
print("--ingrese 3 numeros y se los debolveremos en orden--")
print("----------------------------------------------------")

#input

a= int(input("ingrese el valor a: "))
b= int(input("ingrese el valor b: "))
c= int(input("ingrese el valor c: "))

#proseccing

if a>b:
    if a>c:
        if b>c:
            print("la secuencias es:"+str(a,b,c))
        else:
            print("la secuencias es:"+str(a,c,b))
    else:
        print("la secuencias es:"+str(c,a,b))
if b>c:
    if c>a:
        print("la secuencias es:"+str(b,c,a))
    else:
        print("la secuencias es:"+str(b,a,c))
else:
    print("la secuencias es:"+str(c,b,a))