
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

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

Segundos = int(input("Ingrese la cantidad de segundos: "))
Horas = segundos_a_horas(Segundos)
print(f"{Segundos} segundos equivalen a {Horas} horas")

