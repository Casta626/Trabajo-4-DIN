# Programa que ejecuta continuamente el método
from name_function import formatted_name

print("Por favor, introduce los nombres y apellidos o escribe x para salir")

while True:
   first_name = input("Introduce el nombre: ")
   if first_name == "x":
       print("Hasta luego.")
       break

   last_name = input("Introduce los apellidos: ")
   if last_name == "x":
       print("Hasta luego.")
       break

   result = formatted_name(first_name, last_name)
   print("El nombre formateado es: " + result + ".")