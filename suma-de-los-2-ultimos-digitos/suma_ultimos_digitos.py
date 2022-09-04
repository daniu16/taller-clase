# ejercisio No 6 suma de los ultimos numeros

print ("----------------------------------------------------------")
print("---se sumara los ultimos numeros del valor que ingreses---")
print ("----------------------------------------------------------")

#input

n=int(input("ingrese un valor"))

#proseccing

a = n%10
b = (n%100)%10

suma= a+b

#output

print("el vaor es: "+str(suma))
