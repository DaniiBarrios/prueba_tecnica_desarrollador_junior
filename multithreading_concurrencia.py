import threading
import time
import json
import logging
from sklearn.preprocessing import MinMaxScaler

# Configuración del logging
logging.basicConfig(filename='procesamiento_json.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Función para imprimir números pares
def imprimir_pares():
    for i in range(2, 201, 2):
        print(f'Par: {i}')
        time.sleep(0.5)

# Función para imprimir números impares
def imprimir_impares():
    for i in range(1, 201, 2):
        print(f'Impar: {i}')
        time.sleep(0.5)

# Función para procesar datos del archivo JSON
def procesar_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        scaler = MinMaxScaler()
        
        for key, value in data.items():
            id_elemento = value['id']
            datos = [list(map(float, x.split())) for x in value['data']]
            datos = [item for sublist in datos for item in sublist]  # Aplanar la lista de datos
            
            # Normalización
            datos_normalizados = scaler.fit_transform([[x] for x in datos])
            promedio_antes = sum(datos) / len(datos)
            promedio_despues = sum([x[0] for x in datos_normalizados]) / len(datos_normalizados)
            
            # Registro
            logging.info(f'ID: {id_elemento}')
            logging.info(f'Datos: {datos}')
            logging.info(f'Promedio antes de la normalización: {promedio_antes}')
            logging.info(f'Promedio después de la normalización: {promedio_despues}')
            logging.info(f'Tamaño de los datos: {len(datos)}')

# Crear hilos para impresión de números pares e impares
def iniciar_hilos():
    hilo_pares = threading.Thread(target=imprimir_pares)
    hilo_impares = threading.Thread(target=imprimir_impares)

    hilo_pares.start()
    hilo_impares.start()

    hilo_pares.join()
    hilo_impares.join()

# Ejecución principal
if __name__ == "__main__":
    iniciar_hilos()
    # Procesar archivo JSO
