import random
# Lista vacía
componentes = [] #Es lo primero que se hace, pq no se sabe cuales son #
elemento = input("Ingrese un componente del avion: ")
componentes.append(elemento)
print(componentes)

# Lista numerica
numeros = []
aleatorio = random.randint(0,100)
numeros.append(aleatorio)
numeros.append(10)
for i in range (10):
    aleatorio = random.randint(0,100)
    numeros.append(aleatorio)

print(numeros)

# Lista con diferentes tipos de datos
datos_vuelo = [202, "Boeing 737", True, 10500.5]

# Listas anidadas
matriz_rotacion = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
