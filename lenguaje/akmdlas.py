import random

# Función para simular la finalización de un proceso con un tiempo de espera de E/S del 80%
def simular_proceso(inicio, duracion, espera_80):
    tiempo_simulado = inicio
    tiempo_real = 0
    while tiempo_real < duracion:
        if random.random() < espera_80:
            # El proceso está en espera de E/S, se elige un tiempo aleatorio de E/S
            tiempo_espera = random.randint(1, 5)  # Suponiendo que el tiempo de E/S es entre 1 y 5 minutos
            tiempo_simulado += tiempo_espera
        else:
            # El proceso está en ejecución
            tiempo_simulado += 1
            tiempo_real += 1
    return tiempo_simulado

# Definición de los procesos con sus tiempos de inicio y duración
procesos = [
    {"nombre": "A", "inicio": 600, "duracion": 4},
    {"nombre": "B", "inicio": 610, "duracion": 3},
    {"nombre": "C", "inicio": 615, "duracion": 2},
    {"nombre": "D", "inicio": 620, "duracion": 2}
]

# Configuración del tiempo promedio de espera de E/S del 80%
espera_80 = 0.8

# Simulación de los procesos y cálculo de sus tiempos de finalización
for proceso in procesos:
    tiempo_finalizacion = simular_proceso(proceso["inicio"], proceso["duracion"], espera_80)
    horas = tiempo_finalizacion // 60
    minutos = tiempo_finalizacion % 60
    print(f"Proceso {proceso['nombre']} finaliza a las {int(horas):02d}:{int(minutos):02d} hs")
