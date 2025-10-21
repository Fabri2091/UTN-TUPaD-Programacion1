
#ACTIVIDAD 1

# def imprimir_hola_mundo():
#     return "Hola, Mundo!"


# hola = imprimir_hola_mundo()
# print(hola)


#ACTIVIDAD 2

# def saludar_usuario(nombre):
#     return f"Hola, {nombre}!"


# Usuario = input("Ingrese su nombre: ")
# saludo = saludar_usuario(Usuario)
# print(saludo)


#ACTIVIDAD 3

# def informacion_personal(nombre, apellido, edad, residencia):
#     return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

# Nombre = input("Ingrese su nombre: ")
# Apellido = input("Ingrese su apellido: ")
# Edad = int(input("Ingrese su edad: "))
# Pais = input("Ingrese su nacionalidad: ")
# info = informacion_personal(Nombre, Apellido, Edad, Pais)
# print(info)



#ACTIVIDAD 4

# def calcular_area_circulo(radio):
#     pi = 3.1416
#     area = pi * (radio ** 2)
#     return area

# def calcular_perimetro_circulo(radio):
#     pi = 3.1416
#     perimetro = 2 * pi * radio
#     return perimetro


# radio = float(input("Ingrese el radio del circulo: "))
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)
# print(f"El área del circulo es: {area} y el perimetro es: {perimetro}")


#ACTIVIDAD 5

# def segundos_a_horas(segundos):
#     horas = segundos / 3600
#     return horas

# Segundos = int(input("Ingrese la cantidad de segundos: "))
# Horas = segundos_a_horas(Segundos)
# print(f"{Segundos} segundos equivalen a {Horas} horas")


#ACTIVIDAD 6

# def tabla_multiplicar(numero):

#     for i in range(1, 11):
#         resultado = numero * i
#         print(f"{numero} x {i} = {resultado}")
#     return resultado



# numero = int(input("Ingrese un numero para multiplicar: "))
# tabla_multiplicar(numero)


#ACTIVIDAD 7

# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b if b != 0 else "Indefinido (division por cero)"
#     return suma, resta, multiplicacion, division


# num1 = float(input("Ingrese el primer numero: "))
# num2 = float(input("Ingrese el segundo numero: "))

# suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)

# print(f"Suma: {suma}")
# print(f"Resta: {resta}")
# print(f"Multiplicacion: {multiplicacion}")
# print(f"Division: {division}")

#ACTIVIDAD 8

# def calcular_imc(peso, altura):
#     IMC = peso / (altura ** 2)
#     return IMC


# peso = float(input("Ingrese su peso en kilogramos: "))
# altura = float(input("Ingrese su altura en metros: "))

# imc = calcular_imc(peso, altura)

# print(f"Su Indice de Masa Corporal (IMC) es: {imc: }")


#ACTIVIDAD 9

# def farenheit_a_celsius(fahrenheit):
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius


# farenheit = float(input("Ingrese la temperatura en grados Farenheit: "))

# celsius = farenheit_a_celsius(farenheit)

# print(f"La temperatura en grados Celsius es: {celsius}")

#ACTIVIDAD 10

# def calcular_promedio(a, b, c):
#     promedio = (a + b + c) / 3
#     return promedio


# nota1 = float(input("Ingrese la primera nota: "))
# nota2= float(input("Ingrese la segunda nota: "))
# nota3 = float(input("Ingrese la tercera nota: "))

# promedio = calcular_promedio(nota1, nota2, nota3)

# print(f"El promedio de las notas es: {promedio}")








