# teller punto #1 calcular minutos

print("----------------------------------")
print("---calcular el valor en minutos---")
print("----------------------------------")

#input
n=int(input("ingrese los minutos utilisados"))

#proseccing

if n>3:
    m= 300+(n-3)*50
else:
    m=300

#output
print("---------RESULTADOS---------")
print("valor a pagar: "+str(m))
