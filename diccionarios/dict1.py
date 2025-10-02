# Diccionario vacío
aeronave = {}

# DICCIONARIO 1 (CON ELEMENTOS)
aeronave = {
    "modelo": "Boeing 787-9",
    "envergadura": 60.17,  # metros
    "longitud": 62.81,     # metros
    "mtow": 254000,        # kg
    "velocidad_max": 954   # km/h
}

#Escribir el modelo y su longitud con un print
print(f"Modelo:{aeronave["modelo"]}, mide {aeronave['longitud']} metros")
#nota: en vez de posicion con numero se menciona el nombre de la variable que esta con el valor

# Diccionario 2 (con diferentes tipos de datos como valores)
vuelo = {
    "numero": "AA123",
    "origen": "KLAX",
    "destino": "KJFK",
    "distancia": 3983,
    "a_tiempo": True,
    "tripulacion": ["Capitán Smith", "F/O Johnson", "F/E Williams"]
}

#Imprimir la tripulacion y el destino
print(f"Origen:{vuelo["origen"]} - Destino:{vuelo["destino"]}")


#print(f"Tripluacion:{vuelo['tripulacion']}") asi seria para imprimirla normal, se busca imprimir en listado

for i in vuelo["tripulacion"]:
    print (i) 

#TEORIA
# Acceso a valores
print(aeronave["modelo"])  # "Boeing 787-9"

# Modificación de valores
aeronave["mtow"] = 260000

# Añadir nuevo par clave-valor
aeronave["alcance"] = 14140  # km

# Eliminar par clave-valor
del aeronave["velocidad_max"]

# Comprobar existencia de clave
if "alcance" in aeronave:
    print(f"El alcance es {aeronave['alcance']} km")

# Método get() (devuelve None o un valor por defecto si la clave no existe)
velocidad = aeronave.get("velocidad_max", "No disponible")

Método	Descripción	Ejemplo
clear()	Elimina todos los elementos	aeronave.clear()
copy()	Retorna una copia superficial	copia = aeronave.copy()
fromkeys()	Crea diccionario con claves y valor por defecto	dict.fromkeys(["mtow", "zfw"], 0)
get()	Retorna valor de clave o valor por defecto	aeronave.get("modelo", "Desconocido")
items()	Retorna vista de pares clave-valor	for k, v in aeronave.items(): ...
keys()	Retorna vista de claves	for k in aeronave.keys(): ...
values()	Retorna vista de valores	for v in aeronave.values(): ...
pop()	Elimina clave y retorna su valor	mtow = aeronave.pop("mtow")
popitem()	Elimina y retorna par arbitrario (último)	ultimo = aeronave.popitem()
setdefault()	Inserta par si clave no existe	aeronave.setdefault("alcance", 0)
update()	Actualiza con pares de otro diccionario	aeronave.update(datos_nuevos)
