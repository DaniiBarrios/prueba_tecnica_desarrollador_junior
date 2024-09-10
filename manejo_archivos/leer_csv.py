import pandas as pd
import logging

def leer_csv(ruta_archivo):
    """
    Lee un archivo CSV y muestra estadísticas básicas sobre él.
    """
    try:
        # Leer el archivo CSV usando pandas
        df = pd.read_csv(ruta_archivo)
        
        # Imprimir el número y nombre de las columnas
        print(f"Número de columnas: {len(df.columns)}")
        print(f"Nombre de las columnas: {df.columns.tolist()}")
        
        # Imprimir el número de filas
        print(f"Número de filas: {len(df)}")
        
        # Imprimir promedio y desviación estándar por columna (solo numéricas)
        print("Promedio y desviación estándar por columna:")
        for columna in df.select_dtypes(include='number').columns:
            print(f"{columna} - Promedio: {df[columna].mean()}, Desviación estándar: {df[columna].std()}")
    
    except FileNotFoundError:
        logging.basicConfig(filename='error.log', level=logging.ERROR)
        logging.error(f"Archivo no encontrado: {ruta_archivo}")
        print(f"Archivo no encontrado: {ruta_archivo}")
    except Exception as e:
        logging.basicConfig(filename='error.log', level=logging.ERROR)
        logging.error(f"Error al leer el archivo CSV: {e}")
        print(f"Error al leer el archivo CSV: {e}")

if __name__ == "__main__":
    # Define la ruta del archivo CSV
    ruta_archivo = 'sample-01-csv.csv'  # Cambia esto si es necesario
    
    # Llama a la función para leer el archivo CSV
    leer_csv(ruta_archivo)

