# 🎯 Lección 3: Control de Flujo - Condicionales
# ==============================================

# IF - SI una condición es verdadera
edad = 18

if edad >= 18:
    print("Eres mayor de edad")

# IF-ELSE - Si o si no
hora = 14

if hora < 12:
    print("Buenos días")
else:
    print("Buenas tardes/noches")

# IF-ELIF-ELSE - Múltiples condiciones
calificacion = 85

if calificacion >= 90:
    print("Excelente: A")
elif calificacion >= 80:
    print("Muy bien: B")
elif calificacion >= 70:
    print("Bien: C")
elif calificacion >= 60:
    print("Aprobado: D")
else:
    print("Reprobado: F")

# EJEMPLO: Verificar si puedes entrar a un cine
edad_usuario = 15
tiene_entrada = True

if edad_usuario >= 18 and tiene_entrada:
    print("✓ Puedes entrar")
elif edad_usuario < 18 and tiene_entrada:
    print("✓ Puedes entrar con un adulto")
else:
    print("✗ No puedes entrar")

# Anidamiento (condicionales dentro de condicionales)

numero = -5
if numero > 0:
    if numero % 2 == 0:
        print(f"{numero} es positivo y par")
    else:
        print(f"{numero} es positivo e impar")
else:
    print(f"{numero} no es positivo")
