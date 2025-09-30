import random
' Generar una lista con 100 numeros aleatorios entre 100 y 1000, Calcular el promedio de los valores de la lista y calcular el mayor y el menor de los promedios'
numeros = []

for i in range (100):
    aleatorio = random.randint(100,1000)
    numeros.append(aleatorio)

print(numeros)

suma = 0 
for i in numeros:
    suma += i 

#otra forma seria for i in range(len(numeros)): suma +=numeros[i]

prom= suma / len(numeros)
print(f"promedio = {prom}") 
#otra forma seria promedio= sum(numeros)/len(numeros)

mayor = max(numeros)
menor = min(numeros)
