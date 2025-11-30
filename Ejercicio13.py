#Leer una cadena y eliminar todos los espacios, construyendo una cadena continua.
cadena = input("Introduce una cadena: ")
cadena_sin_espacios = " "
for i in cadena:
    if i != " ":
        cadena_sin_espacios += i
print(cadena_sin_espacios)

