# 💪 EJERCICIOS PRÁCTICOS - Fundamentos de Python
# ================================================

print("=" * 50)
print("EJERCICIOS - NIVEL PRINCIPIANTE")
print("=" * 50)

# EJERCICIO 1: Saludar y pedir nombre
print("EJERCICIO 1: Saludar y pedir nombre")
nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola, {nombre}! Bienvenido a Python.")

# EJERCICIO 2: Calcular el área de un rectángulo
print("\nEJERCICIO 2: Calcular el área de un rectángulo")
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: ")) 
area = base * altura
print(f"El área del rectángulo es: {area}")


# EJERCICIO 3: Encontrar el número mayor de tres
print("\nEJERCICIO 3: Encontrar el número mayor de tres")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
mayor = max(num1, num2, num3)
print(f"El número mayor es: {mayor}")


# EJERCICIO 4: Tabla de multiplicar
print("\nEJERCICIO 4: Tabla de multiplicar")
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    


# EJERCICIO 5: Contar números pares e impares
print("\nEJERCICIO 5: Contar números pares e impares")
cantidad = int(input("¿Cuántos números desea ingresar? "))
pares = 0
impares = 0

for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"La cantidad de números pares es: {pares}")
print(f"La cantidad de números impares es: {impares}")


# EJERCICIO 6: Invertir una lista
print("\nEJERCICIO 6: Invertir una lista")
lista = []
cantidad = int(input("¿Cuántos elementos desea ingresar en la lista? "))
for _ in range(cantidad):
    elemento = input("Ingrese un elemento: ")
    lista.append(elemento)
lista_invertida = lista[::-1]
print("Lista original:", lista)
print("Lista invertida:", lista_invertida)


# EJERCICIO 7: Buscar elemento en diccionario


# EJERCICIO 8: Función para calcular factorial


# EJERCICIO 9: Validar si es número perfecto


# EJERCICIO 10: Contador de vocales
