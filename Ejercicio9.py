#Leer una cadena y contar cuántas vocales contiene.
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
frase = input("Introduce una cadena: ")
contador = 0
for i in frase:
    if i in vocales:
        contador += 1
print("La cadena contiene", contador, "vocales")
