#Vas a construir una calculadora CLI interactiva. El usuario elige la operación y los números, y puede seguir calculando hasta que quiera salir. Usa todo lo que aprendiste esta semana: funciones, condicionales, bucles, input.
print("Bienvenido a la Calculadora CLI interactiva")
def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."
while True:
    print("\nSeleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = input("Ingrese el número de la operación que desea realizar: ")
    if opcion == '5':
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if opcion == '1':
        resultado = sumar(num1, num2)
        print(f"El resultado de {num1} + {num2} es: {resultado}")
    elif opcion == '2':
        resultado = restar(num1, num2)
        print(f"El resultado de {num1} - {num2} es: {resultado}")
    elif opcion == '3':
        resultado = multiplicar(num1, num2)
        print(f"El resultado de {num1} * {num2} es: {resultado}")
    elif opcion == '4':
        resultado = dividir(num1, num2)
        print(f"El resultado de {num1} / {num2} es: {resultado}")
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")