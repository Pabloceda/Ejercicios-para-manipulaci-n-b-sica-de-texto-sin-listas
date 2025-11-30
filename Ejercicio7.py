#Reemplazar un carácter por otro recorriendo la cadena y concatenando a una nueva cadena.
nueva_frase = ""
frase = input("Introduce una frase: ")
caracter = "a"
caracter_reemplazado = "e"
for i in frase:
    if i == caracter:
        i = caracter_reemplazado
    nueva_frase += i
print(nueva_frase)

