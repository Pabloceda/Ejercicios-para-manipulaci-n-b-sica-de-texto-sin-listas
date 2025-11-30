#Dada una cadena, construir una nueva cadena donde cada vocal se reemplaza por un asterisco '*'.

vocal = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
frase = input("Introduce una frase: ")
nueva_frase = ""
for i in frase:
    if i in vocal:
        nueva_frase += "*"
    else:
        nueva_frase += i
print(nueva_frase)
