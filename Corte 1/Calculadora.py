class Calculadora:
    def __init__(self):
        pass

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: No se puede dividir por 0"
        return a / b

    def calcular(self):
        print("Bienvenido a la calculadora")

        # Solicitar los valores
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))

        # Solicitar la operación
        print("Elige la operación: ")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        opcion = input("Introduce el número de la operación (1/2/3/4): ")

        # Ejecutar la operación elegida
        if opcion == "1":
            print(f"Resultado: {self.sumar(a, b)}")
        elif opcion == "2":
            print(f"Resultado: {self.restar(a, b)}")
        elif opcion == "3":
            print(f"Resultado: {self.multiplicar(a, b)}")
        elif opcion == "4":
            print(f"Resultado: {self.dividir(a, b)}")
        else:
            print("Opción no válida")

# Crear una instancia de la calculadora y ejecutar
calc = Calculadora()
calc.calcular()
