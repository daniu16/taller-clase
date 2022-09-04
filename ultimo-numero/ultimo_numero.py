#  ejercicio numero 4 ultimo numero par

print ("---------------------------------------")
print("---determinar si el ultimo digito es par")
print ("---------------------------------------")

#input

n = int(input("digite un numero"))

#proseccing

num = n % 10
if num %2 == 0:
    print("el numer",num,"es par")
else:
    print("el numero",num,"es impar")
    