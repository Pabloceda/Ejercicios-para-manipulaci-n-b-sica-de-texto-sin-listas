#Leer dos cadenas y concatenarlas manualmente sin usar el operador + en una sola operación (concatenar carácter a carácter con un ciclo).
cadena1 = input("Introduce su primera frase")
cadena2 = input("Introduce su segunda frase")
cadena_concatenada = " "
for i in cadena1:
    cadena_concatenada += i
for i in cadena2:
    cadena_concatenada += i

print(cadena_concatenada)