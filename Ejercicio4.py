#Construir manualmente una nueva cadena añadiendo un carácter a la vez (ejemplo: filtrar caracteres o construir cadenas invertidas).

frase = input("Introduce una frase: ")

def construir_cadena_invertida(cadena):
    cadena_invertida = ""
    for i in cadena:
        cadena_invertida = i + cadena_invertida
    return cadena_invertida
print(construir_cadena_invertida(frase))


