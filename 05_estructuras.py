# 🎯 Lección 5: Listas y Estructuras de Datos
# ===========================================

# LISTAS: Colección ordenada y mutable (se puede modificar)
print("=== LISTAS ===")

numeros = [1, 2, 3, 4, 5]
print("Lista:", numeros)
print("Largo:", len(numeros))
print("Tipo:", type(numeros))
print("¿Es una lista?", isinstance(numeros, list))


# Acceso por índice (empieza en 0)
print("\nPrimer elemento:", numeros[0])     # 1
print("Segundo elemento:", numeros[1])    # 2
print("Último elemento:", numeros[-1])    # 5
print("Penúltimo:", numeros[-2])          # 4

# SLICING (obtener una porción)
print("\nPrimeros 3:", numeros[0:3])       # [1, 2, 3]
print("Del 2 al 4:", numeros[1:4]) 
       # [2, 3, 4]

# MODIFICAR LISTAS
print("\n=== MODIFICAR LISTAS ===")
colores = ["rojo", "verde", "azul"]

# Cambiar un elemento
colores[1] = "amarillo"
print("Después de cambiar:", colores) 

# Agregar al final
colores.append("rosa")
print("Después de append:", colores)

# Insertar en posición específica
colores.insert(0, "negro")
print("Después de insert:", colores)

# Eliminar un elemento (verificar antes para evitar error si no existe)
if "verde" in colores:
    colores.remove("verde")
else:
    print("'verde' no está en la lista")
print("Después de remove:", colores)

# TUPLAS: Colección ordenada e INMUTABLE (no se puede cambiar)
print("\n=== TUPLAS ===")
coordenadas = (10, 20, 30)
print("Tupla:", coordenadas)
print("Primer elemento:", coordenadas[0])
# coordenadas[0] = 5  # ❌ ERROR: no se puede modificar

# DICCIONARIOS: Pares clave-valor (útiles para datos estructurados)
print("\n=== DICCIONARIOS ===")
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Madrid",
    "email": "carlos@example.com"
}

print("Diccionario:", persona)
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# Modificar
persona["edad"] = 31
print("Edad actualizada:", persona["edad"])

# Agregar nueva clave
persona["profesion"] = "Ingeniero"
print("Diccionario actualizado:", persona)

# Iterar sobre diccionarios
print("\nIterando diccionario:")
for clave in persona:
    print(f"{clave}: {persona[clave]}")

# SETS: Colección de elementos únicos (sin duplicados)
print("\n=== SETS ===")
numeros_unicos = {1, 2, 2, 3, 3, 3, 4}
print("Set (sin duplicados):", numeros_unicos)

# Agregar elemento
numeros_unicos.add(5)
print("Después de add:", numeros_unicos)
