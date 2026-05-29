# 🎯 Lección 6: Funciones
# =======================

# FUNCIÓN BÁSICA: Bloque de código reutilizable
def saludar():
    """Esta es una función de saludo"""
    print("¡Hola, mundo!")

saludar()

# FUNCIÓN CON PARÁMETROS
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("Juan")
saludar_persona("María")

# FUNCIÓN CON MÚLTIPLES PARÁMETROS
def suma(a, b):
    resultado = a + b
    return resultado  # Devolver un valor

numero1 = 10
numero2 = 5
total = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {total}")

# FUNCIÓN CON VALOR POR DEFECTO
def presentar(nombre, edad=18):
    print(f"Me llamo {nombre} y tengo {edad} años")

presentar("Carlos")          # usa edad = 18
presentar("Ana", 25)         # usa edad = 25

# FUNCIÓN QUE DEVUELVE MÚLTIPLES VALORES
def obtener_coordenadas():
    x = 10
    y = 20
    return x, y  # Devuelve una tupla

resultado_x, resultado_y = obtener_coordenadas()
print(f"Coordenadas: ({resultado_x}, {resultado_y})")

# SCOPE: Variables locales y globales
nombre_global = "Juan"

def cambiar_nombre():
    nombre_local = "Pedro"  # Solo existe dentro de la función
    print(f"Dentro de función: {nombre_global}")
    print(f"Local: {nombre_local}")

cambiar_nombre()
print(f"Fuera de función: {nombre_global}")
# print(nombre_local)  # ❌ ERROR: no existe fuera de la función

# FUNCIÓN CON MÚLTIPLES ARGUMENTOS
def imprimir_datos(**datos):
    """Recibe cualquier cantidad de parámetros nombrados"""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

imprimir_datos(nombre="Carlos", edad=30, ciudad="Madrid")

# FUNCIÓN CON LISTA DE ARGUMENTOS
def sumar_numeros(*numeros):
    """Recibe cualquier cantidad de números"""
    total = 0
    for num in numeros:
        total += num
    return total

print("Suma:", sumar_numeros(1, 2, 3, 4, 5))
print("Suma:", sumar_numeros(10, 20))

# FUNCIÓN COMO PARÁMETRO (Funciones de orden superior)
def aplicar_operacion(a, b, operacion):
    return operacion(a, b)

def multiplicar(x, y):
    return x * y

resultado = aplicar_operacion(4, 5, multiplicar)
print(f"4 * 5 = {resultado}")
