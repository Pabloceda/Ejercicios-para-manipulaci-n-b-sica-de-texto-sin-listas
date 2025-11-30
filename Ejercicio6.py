#Extraer subcadenas usando slicing (rebanado de cadenas sin usar listas).
cadena = input("Introduce una cadena: ")

subcadena = cadena[0:4]  
print(subcadena)

subcadena_desde_indice = cadena[5:] 
print(subcadena_desde_indice)

subcadena_hasta_indice = cadena[:4]  
print(subcadena_hasta_indice)

subcadena_con_paso = cadena[0:10:2] 
print(subcadena_con_paso)

subcadena_invertida = cadena[::-1] 
print(subcadena_invertida)
