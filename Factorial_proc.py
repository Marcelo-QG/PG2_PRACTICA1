n=input("Introducir un numero: ")
factorial=1
cont =1
while cont <= int(n):
    factorial = factorial * cont
    cont += 1
print("El factorial de ", n, " es: ", factorial)