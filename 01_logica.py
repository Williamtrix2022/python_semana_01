#numeros mayores,menor, suma o si son iguales 
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
suma = num1 + num2 + num3

#mayor
mayor = num1
if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3
#menor
menor = num1
if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
print(f"La suma de los números es: {suma}")