# Lista de componentes con sus masas (kg) y posiciones (m)
componentes = ["motor izquierdo", "motor derecho", "fuselaje", "ala izquierda", "ala derecha", "cola"]
masas = [1200, 1200, 5000, 800, 800, 600]
posiciones_x = [2, 2, 0, -2, 2, -6]

# Cálculo del centro de masa en eje X sin list comprehensions
masa_total = 0
momento_total = 0

for i in range(len(masas)): #dentro de range quedan las canridades de masas, donde len lee la cantidad de elementos q hay en la lista
    masa_total += masas[i] #la i va tomando los valores desde 0 a 5, en la posicion i se tiene la posicion 0
    momento_total += masas[i] * posiciones_x[i] #multiplica masas en posicion i por posiciones en x 

centro_masa_x = momento_total / masa_total

print(f"Centro de masa en eje X: {centro_masa_x:.2f} m")