# 🎯 Lección 4: Bucles
# ===================

# FOR: Repetir algo una cantidad de veces
print("=== BUCLE FOR ===")


for i in range(5):  # 0, 1, 2, 3, 4
    print(f"Vuelta {i}")

# Tabla de multiplicar del 3
print("\nTabla del 3:")
for numero in range(1, 11):  # 1 a 10
    resultado = 3 * numero
    print(f"3 x {numero} = {resultado}")

# ITERAR sobre un string
print("\n=== ITERAR SOBRE STRING ===")
palabra = "Python"
for letra in palabra:
    print(letra)    

# ITERAR sobre un rango con paso
print("\n=== ITERAR CON PASO ===")
for numero in range(0, 20, 2):  # 0, 2, 4, ..., 18
    print(numero)
# ITERAR sobre un rango en orden inverso
print("\n=== ITERAR INVERSO ===")
for numero in range(10, 0, -1):  # 10, 9, ..., 1
    print(numero)
# ITERAR sobre un rango con números negativos
print("\n=== ITERAR CON NÚMEROS NEGATIVOS ===")
for numero in range(-5, 0):  # -5, -4, -3, -2, -1
    print(numero)
# ITERAR sobre un rango con números negativos e inverso
print("\n=== ITERAR CON NÚMEROS NEGATIVOS E INVERSO ===")
for numero in range(-1, -6, -1):  # -1, -2, -3, -4, -5
    print(numero)

# ITERAR sobre un rango con números negativos, inverso y paso
print("\n=== ITERAR CON NÚMEROS NEGATIVOS, INVERSO Y PASO ===")
for numero in range(-1, -10, -2):  # -1, -3, -5, -7, -9
    print(numero)

# WHILE: Repetir mientras se cumpla una condición
print("\n=== BUCLE WHILE ===")

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador = contador + 1  # ⚠️ IMPORTANTE: aumentar, sino bucle infinito

# ITERAR sobre una lista
print("\n=== ITERAR SOBRE LISTA ===")
frutas = ["manzana", "plátano", "naranja", "fresa"]

for fruta in frutas:
    print(f"Me gusta la {fruta}")
# ITERAR sobre una lista con índice
print("\n=== ITERAR SOBRE LISTA CON ÍNDICE ===")
for indice, fruta in enumerate(frutas):
    print(f"{indice}: Me gusta la {fruta}")

# ITERAR sobre una lista con índice e inverso
print("\n=== ITERAR SOBRE LISTA CON ÍNDICE E INVERSO ===")
for indice, fruta in enumerate(reversed(frutas)):
    print(f"{indice}: Me gusta la {fruta}")



# BREAK: Salir del bucle
print("\n=== BREAK ===")
for numero in range(1, 11):
    if numero == 5:
        print("¡Encontré el 5! Saliendo...")
        break  # Sale del bucle
    print(numero)

# CONTINUE: Saltar a la siguiente iteración
print("\n=== CONTINUE ===")
for numero in range(1, 6):
    if numero == 3:
        print(f"{numero}: saltando...")
        continue  # Salta este número
    print(f"Procesando {numero}")

# EJEMPLO: Encontrar el primer número par
print("\n=== EJEMPLO ===")
for num in range(1, 20):
    if num % 2 == 0:
        print(f"El primer número par encontrado: {num}")
        break
# EJEMPLO: Contar cuántos números pares hay entre 1 y 20
print("\n=== EJEMPLO CONTAR PARES ===")
contador_pares = 0
for num in range(1, 21):
    if num % 2 == 0:
        contador_pares += 1
print(f"Hay {contador_pares} números pares entre 1 y 20.")
# EJEMPLO: Imprimir solo los números impares entre 1 y 20
print("\n=== EJEMPLO IMPRIMIR IMPARES ===")
for num in range(1, 21):
    if num % 2 == 0:
        continue  # Saltar los pares
    print(num)
