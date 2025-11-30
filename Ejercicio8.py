#Convertir todas las letras a mayúsculas o minúsculas usando ciclos y sumas de caracteres (sin usar los métodos upper() o lower()).
def convertir_mayusculas(texto):
    resultado = ""
    for i in texto:
        # Si el caracter está entre 'a' y 'z', restamos 32 a su valor ASCII para hacerlo mayúscula
        if 'a' <= i <= 'z':
            resultado += chr(ord(i) - 32)
        else:
            resultado += i
    return resultado

def convertir_minusculas(texto):
    resultado = ""
    for i in texto:
        # Si el caracter está entre 'A' y 'Z', sumamos 32 a su valor ASCII para hacerlo minúscula
        if 'A' <= i <= 'Z':
            resultado += chr(ord(i) + 32)
        else:
            resultado += i
    return resultado

texto_usuario = input("Ingrese una cadena de texto: ")
opcion = input("Escriba 'M' para mayúsculas o 'm' para minúsculas: ")

if opcion == 'M':
    print("Texto en mayúsculas:", convertir_mayusculas(texto_usuario))
elif opcion == 'm':
    print("Texto en minúsculas:", convertir_minusculas(texto_usuario))
else:
    print("Opción no válida.")
