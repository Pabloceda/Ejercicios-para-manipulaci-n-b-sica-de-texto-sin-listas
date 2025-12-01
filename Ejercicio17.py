# Leer una cadena y crear una nueva donde sólo aparezcan los caracteres que se repiten más de una vez.

cadena = input("Introduce una cadena: ")
nueva_cadena = ""
for i in cadena:
    if cadena.count(i) > 1 and i not in nueva_cadena:
        nueva_cadena += i
salida = " "
for i in range(len(nueva_cadena)):
    salida += '"' + nueva_cadena[i] + '"'
    if i < len(nueva_cadena) - 1:
        salida += ", "

print("Estos son los caracteres que se repiten más de una vez: " + salida)
