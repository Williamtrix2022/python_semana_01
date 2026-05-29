#Haz una función que reciba un número y devuelva True si es positivo, False si no.
print("EJERCICIO 2: Verificar si un número es positivo")
def es_positivo(numero):
    return numero > 0
num = float(input("Ingrese un número: "))
if es_positivo(num):
    print(f"{num} es un número positivo.")
else:
    print(f"{num} no es un número positivo.")
    