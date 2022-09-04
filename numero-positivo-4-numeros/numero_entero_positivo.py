#ejercicion No3. 4 numero positivos



print("---------------------------------------------------------------------------")
print("--- se determina si es un numero entero positivo de 4 cifras---")
print("---------------------------------------------------------------------------")

#input
n = input("Digite el valor que desea")
n = int(n)

#proseccing
positivo = print("numero postivo de 4 cifras")
falso = print("no es un numero positivo de 4 cifras")
m= n/1000
if  m>1:
    m=positivo
else:
    m=falso

