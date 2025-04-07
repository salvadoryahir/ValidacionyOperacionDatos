# Programa que genera una contraseña de 8 caracteres a partir de 3 palabras dadas por el usuario
import random

# Lista de vocales para hacer la contraseña más natural
vocales = "aeiou"

# Función para rellenar palabras cortas con una vocal aleatoria
def completar_palabra(palabra):
    while len(palabra) < 2:
        palabra += random.choice(vocales) # Agrega una vocal aleatoria
        return palabra

# Pedir tres palabras al usuario
palabra1 = completar_palabra (input("Introduce la primera palabra: "))
palabra2 = completar_palabra (input("Introduce la segunda palabra: "))
palabra3 = completar_palabra (input("Introduce la tercera palabra: "))

# Generar la contraseña de 8 caracteres

contraseña = (palabra1[:3] + palabra2[:3] + palabra3[:2])[:8]

print("La contraseña generada es:", contraseña)

#Pedir al usuario que ingrese la contraseña
contraseña_usuario = input("Introduce la contraseña: ")

# Comparar longitudes y verificar si es correcta
if len(contraseña_usuario) < len(contraseña):
    print("Faltan", len(contraseña)- len(contraseña_usuario), "caracteres")
elif len(contraseña_usuario) > len (contraseña):
    print("Sobran", len(contraseña_usuario) - len(contraseña), "caracteres")
elif contraseña_usuario == contraseña:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")