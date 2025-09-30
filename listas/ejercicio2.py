# Lista con elementos
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"] #se agrega lo que compone la lista

# Indexación (comienza en 0) SUBLISTAS
print(componentes[0])  # "alas"
print(componentes[-1])  # "tren de aterrizaje" (indexación negativa)

# Slicing (rebanado)
print(componentes[1:3])  # ["fuselaje", "motores"] son el 1 y el 2
print(componentes[:2])   # ["alas", "fuselaje"] desde el 0 hasta el 2-1
print(componentes[2:])   # ["motores", "tren de aterrizaje"] desde el 2 hasta el final