#Leer una cadena y contar cuántos caracteres numéricos ('0' a '9') contiene.
numero = ["0","1","2","3","4","5","6","7","8","9"]
frase = input("Introduce una frase: ")
contador = 0
for i in frase:
    if i in numero:
        contador += 1
print("La frase contiene", contador, "numeros")


