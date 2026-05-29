# 🎯 Lección 2: Operadores y Cálculos
# ===================================

# OPERADORES ARITMÉTICOS
a = 10 
b = 3

print("SUMA:", a + b)          # 13
print("RESTA:", a - b)         # 7
print("MULTIPLICACIÓN:", a * b) # 30
print("DIVISIÓN:", a / b)      # 3.333...
print("DIVISIÓN ENTERA:", a // b) # 3
print("MÓDULO (resto):", a % b)  # 1
print("POTENCIA:", a ** b)     # 1000

# OPERADORES DE COMPARACIÓN (devuelven True o False)
print("\nCOMPARACIONES:")
print("10 > 3:", 10 > 3)       # True
print("10 < 3:", 10 < 3)       # False
print("10 == 10:", 10 == 10)   # True (¿igual?)
print("10 != 3:", 10 != 3)     # True (¿diferente?)
print("10 >= 10:", 10 >= 10)   # True

# OPERADORES LÓGICOS
print("\nLÓGICA:")
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("True or False:", True or False)     # True
print("not True:", not True)               # False

# PRIORIDAD DE OPERADORES
resultado = 2 + 3 * 4  # Multiplicación primero
print("\n2 + 3 * 4 =", resultado)  # 14, no 20

# Con paréntesis
resultado = (2 + 3) * 4
print("(2 + 3) * 4 =", resultado)  # 20

resultado = 10 - 4 / 2 + 3 * 2
print("10 - 4 / 2 + 3 * 2 =", resultado)  # 10 - 2 + 6 = 14 