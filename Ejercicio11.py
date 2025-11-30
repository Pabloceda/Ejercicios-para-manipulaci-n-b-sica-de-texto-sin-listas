#Construir una nueva cadena con todos los caracteres de la cadena original, pero duplicando cada vocal.
frase = input("Introduce una frase: ")
vocales = "aeiouAEIOU"
nueva_frase = ""
for i in frase:
    if i in vocales:
        nueva_frase += i*2
    else:
        nueva_frase += i
print(nueva_frase)
