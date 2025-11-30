#Leer una cadena y contar cuántos caracteres son letras mayúsculas.
mayus = 0
frase = input("Introduce una frase: ")
for i in frase:
    if i >= "A" and i <= "Z":
        mayus += 1
print("La frase contiene", mayus, "letras mayúsculas")
