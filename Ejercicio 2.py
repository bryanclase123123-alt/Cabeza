nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
altura = int(input("Introduce tu altura en cm: "))
print("Nombre:", nombre)
print("Edad:", edad, "años")
print("Altura:", altura, "cm")

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
suma = num1 + num2
print("La suma de", num1, "+", num2, "es =", suma)

import math
radio = int(input("Introduce el radio del círculo: "))
area = math.pi * (radio ** 2)
print("El área del círculo es =", area)