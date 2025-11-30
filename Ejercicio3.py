#Contar cuántas veces aparece un carácter dado en una cadena usando for y un contador.

frase = input("Introduce una frase: ")

contador_caracter = 0

for i in frase:
    if i == "a":
        contador_caracter += 1

print("El caracter 'a' aparece", contador_caracter, "veces")
