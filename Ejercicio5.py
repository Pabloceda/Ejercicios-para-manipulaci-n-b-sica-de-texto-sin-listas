#Verificar si un carácter específico está en la cadena con un ciclo y comparaciones.
encontrado = False
frase = input("Introduce una frase: ")

caracter = "a"

for i in frase:
    if i == caracter:
        encontrado = True
        break

if encontrado:
    print("El carácter está en la cadena")
else:
    print("El carácter no está en la cadena")


