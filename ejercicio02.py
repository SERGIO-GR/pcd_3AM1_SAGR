import string
import random
minusculas_ascii = string.ascii_lowercase
print(minusculas_ascii)

mayusculas_ascii = string.ascii_uppercase
print(mayusculas_ascii)

numeros = string.digits
print(numeros)


def generarPassword(n):
    ascii=minusculas_ascii+mayusculas_ascii+numeros
    lista=list(ascii)
    i= random.randint(1,len(lista))
    password=lista[i]
    return password
    


for i in range(10, 20):
    print(generarPassword(i))