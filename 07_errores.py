# 🎯 Lección 7: Manejo de Errores
# ===============================

# TRY-EXCEPT: Capturar errores sin que el programa se bloquee
print("=== MANEJO DE ERRORES ===\n")

try:
    numero = int("abc")  # Esto va a generar error
    print(numero)
except ValueError:
    print("Error: No puedo convertir 'abc' a número")

# MÚLTIPLES EXCEPCIONES
try:
    lista = [1, 2, 3]
    print(lista[10])  # Índice fuera de rango
except IndexError:
    print("Error: Índice fuera de la lista")
except ValueError:
    print("Error: Valor inválido")

# CAPTURAR CUALQUIER ERROR
try:
    resultado = 10 / 0
except Exception as error:
    print(f"Error general: {error}")

# ELSE: Se ejecuta si NO hay error
try:
    numero = int("42")
    print(f"Conversión exitosa: {numero}")
except ValueError:
    print("Error en la conversión")
else:
    print("Bien, el número se convirtió correctamente")

# FINALLY: Se ejecuta SIEMPRE (con o sin error)
try:
    archivo = open("inexistente.txt")
except FileNotFoundError:
    print("Archivo no encontrado")
finally:
    print("Esto se ejecuta siempre")

# VALIDACIÓN CON USUARIO
print("\n=== EJEMPLO PRÁCTICO ===")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad < 0:
            print("La edad no puede ser negativa")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido")

print(f"Tu edad es: {edad}")

# LEVANTAR EXCEPCIONES PERSONALIZADAS
def verificar_edad(edad):
    if edad < 18:
        raise ValueError("Debes ser mayor de 18 años")
    return True

try:
    verificar_edad(15)
except ValueError as error:
    print(f"Error de validación: {error}")
