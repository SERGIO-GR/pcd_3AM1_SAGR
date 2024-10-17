# Crear un programa que genere 100 numeros aleatorios entre 1 y 1000
# inserte en un alista los pares y en otr alos impares
# Imprimir ambas listas y el tamaño de las mismas
import random

numeros_aleatorios=[random.randint(1,1000) for i in range(100)]

lambda_pares = lambda numeros_aleatorios: [c for c in numeros_aleatorios if c%2==0]
lambda_impares = lambda numeros_aleatorios: [c for c in numeros_aleatorios if not c%2==0]

print(f'los numeros pares son: {lambda_pares(numeros_aleatorios)} \n los impares son: {lambda_impares(numeros_aleatorios)} \n tamaño pares: {len(lambda_pares(numeros_aleatorios))}\n tamaño impares: {len(lambda_impares(numeros_aleatorios))}')
