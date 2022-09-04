# ejercicio numero 5 ultimos 2 digitos iguales

print("---------------------------------------------------------------------")
print("---se determina si los ultimos 2 valores de un numero son iguales---")
print("---------------------------------------------------------------------")

#input

n= int(input("digite  un valor"))

#output


if n %10 == ((n%1000)%100)%10:
    print("los ultimos digitos son iguales: ")
else:
    print("los ultimos digitos no son iguales: ")
