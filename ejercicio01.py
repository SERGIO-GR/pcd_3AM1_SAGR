
import string

caracteres_ascii = string.ascii_letters
print(caracteres_ascii)

def verificar(cadena):
    # Escribe el codigo que verifique que todos los caracteres de una
    # cadena son letras ASCII
    # Devuelve: True en caso de que todos los caracteres sean letras ascii
    #           False en caso contrario
    for c in cadena:
        for a in caracteres_ascii:
            if a == c:
                return True

    return False        


cadena1 = "Hola"
print(verificar(cadena1))