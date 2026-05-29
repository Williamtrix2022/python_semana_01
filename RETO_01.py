#pide dos números al usuario y muestra cuál es el mayor. Si son iguales, dilo.

print("EJERCICIO 1: Comparar dos números")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Los números son iguales.")
        