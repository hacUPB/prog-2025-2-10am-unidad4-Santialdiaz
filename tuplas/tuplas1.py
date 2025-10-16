''''
# Tupla vacía
coordenada = ()

# Tupla con elementos
coordenada = (33.9425, -118.4081)  # LAX (Aeropuerto de Los Ángeles)

# Tupla con un solo elemento (requiere coma al final)
rumbo = (270,)  # Sin la coma sería tratado como un entero entre paréntesis

# Tupla sin paréntesis (empaquetado implícito)
avion_info = "Boeing 787", "Dreamliner", 2009, 242 #python reconoce 

# Indexación (similar a las listas)
print(coordenada[0])  # 33.9425
print(avion_info[-1])  # 242 (pasajeros)

# Slicing
print(avion_info[0:2])  # ("Boeing 787", "Dreamliner")

# Desempaquetado de tuplas
fabricante, modelo, año, capacidad = avion_info
print(f"El {fabricante} {modelo} se lanzó en {año}")

# Desempaquetado con *
lat, lon = coordenada
print(f"Latitud: {lat}, Longitud: {lon}")
'''
lista_de_tuplas = [(0,0) , (4,5) , (5,0)]
lista_de_tuplas.append((9,4)) #agregarle a la tupla, siempre se agrega al final 
print(lista_de_tuplas)
lista_de_tuplas[0] = (1,1)   #cambiar el elemento 0 de la tupla
print(lista_de_tuplas)

tupla_de_listas = ([1,4,6] , [9,7,0])
print(tupla_de_listas)
tupla_de_listas [0][0] = 10
print(tupla_de_listas)
#No puedo agregar una nueva lista, ni borrar una lista ni modificiar toda una lista, pero puedo acceder a la lista a modificarla
numeros = (3, 12, 90, 45, 32)

for n in numeros:
    print(n)
#Imprimir una tupla como una lista, recordar que no se pueden cambiar

#CONDICIONALES CON LISTAS Y TUPLAS
if 12 in numeros:
    print("El 12 es aparte de la tupla")    
else:
    print("No se encuentra el 12")




# Representando una flota de aeronaves con tuplas
# (modelo, envergadura (m), longitud (m), mtow (kg), velocidad_max (km/h))
fleet_data = [
    ("Airbus A320", 35.80, 37.57, 78000, 871),
    ("Boeing 737-800", 35.79, 39.47, 79010, 853),
    ("Embraer E190", 28.72, 36.24, 51800, 871),
    ("Bombardier CRJ-900", 24.85, 36.40, 38330, 870)
]

# Encontrar el avión con mayor envergadura (paso a paso)
print("=== Buscando el avión con mayor envergadura ===")

# Inicializamos variables para el seguimiento
avion_mayor_envergadura = None
mayor_envergadura_valor = 0

# Recorremos cada avión en la flota
for avion in fleet_data: #for itera en la estructura, la variable avion toma los elementos de la lista
    # Extraemos los datos del avión actual
    modelo = avion[0]
    envergadura = avion[1]
    longitud = avion[2]
    mtow = avion[3]
    velocidad_max = avion[4]
    
    print(f"Revisando: {modelo} - Envergadura: {envergadura} m")
    
    # Comparamos si esta envergadura es mayor que la que teníamos guardada
    if envergadura > mayor_envergadura_valor:
        # Si es mayor, actualizamos nuestros valores
        mayor_envergadura_valor = envergadura
        avion_mayor_envergadura = avion
        print(f"  → Nuevo récord encontrado: {modelo}")
    else:
        print(f"  → No supera el récord actual")

# Mostramos el resultado
print(f"\nResultado: Avión con mayor envergadura: {avion_mayor_envergadura[0]} ({avion_mayor_envergadura[1]} m)")

print("\n" + "="*50)

# Calcular velocidad promedio de la flota (paso a paso)
print("=== Calculando velocidad promedio de la flota ===")

# Inicializamos variables para el cálculo
suma_velocidades = 0
contador_aviones = 0

# Recorremos cada avión para sumar las velocidades
for avion in fleet_data:
    # Extraemos el modelo y la velocidad del avión actual
    modelo = avion[0]
    velocidad = avion[4]
    
    print(f"Procesando: {modelo} - Velocidad: {velocidad} km/h")
    
    # Sumamos la velocidad al total
    suma_velocidades = suma_velocidades + velocidad
    contador_aviones = contador_aviones + 1
    
    print(f"  → Suma acumulada: {suma_velocidades} km/h")
    print(f"  → Aviones procesados: {contador_aviones}")

# Calculamos el promedio
velocidad_promedio = suma_velocidades / contador_aviones

# Mostramos el resultado
print(f"\nCálculo final:")
print(f"Suma total de velocidades: {suma_velocidades} km/h")
print(f"Número de aviones: {contador_aviones}")
print(f"Velocidad promedio de la flota: {velocidad_promedio:.2f} km/h")