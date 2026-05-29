# 🎯 Lección 1: Inicio con Python
# ================================

# ✅ Tu primer programa
print("¡Hola, mundo!")
print("Bienvenido a Python")

# 📝 Comentarios: Empieza con # (no se ejecutan)

# Las variables almacenan información
nombre = "Juan"
edad = 25
altura = 1.75

print(nombre)
print(edad)
print(altura)

# Puedes imprimir varias cosas juntas
print("Yo soy", nombre, "y tengo", edad, "años")

# O con f-strings (más moderno)
print(f"Yo soy {nombre} y tengo {edad} años")

# Tipos de datos básicos
texto = "Python"        # str (string - texto)
numero = 42             # int (entero)
decimal = 3.14          # float (decimal)
verdadero = True        # bool (booleano: True o False)

print(type(texto))      # <class 'str'>
print(type(numero))     # <class 'int'>
print(type(decimal))    # <class 'float'>
print(type(verdadero))  # <class 'bool'>
