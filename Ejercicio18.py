# Leer una cadena y construir una nueva cadena dejando sólo los caracteres que son consonantes (sin listas, usando condiciones y concatenación).

cadena = input("Introduce una cadena: ")
nueva_cadena = ""

for i in cadena:
    if i.isalpha() and i not in "aeiouAEIOU":
        nueva_cadena += i

print(nueva_cadena)
