# calculadora.py — Calculadora CLI interactiva

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return None
    return a / b

def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo.")

print("Bienvenido a la Calculadora CLI interactiva")

while True:
    print("\nSeleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación: ")

    if opcion == '5':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break

    if opcion not in ['1', '2', '3', '4']:
        print("Opción no válida. Elige entre 1 y 5.")
        continue

    num1 = pedir_numero("Ingrese el primer número: ")
    num2 = pedir_numero("Ingrese el segundo número: ")

    if opcion == '1':
        resultado = sumar(num1, num2)
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcion == '2':
        resultado = restar(num1, num2)
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcion == '3':
        resultado = multiplicar(num1, num2)
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcion == '4':
        resultado = dividir(num1, num2)
        if resultado is None:
            print("Error: No se puede dividir por cero.")
        else:
            print(f"Resultado: {num1} / {num2} = {resultado}")