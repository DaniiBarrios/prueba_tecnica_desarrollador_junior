import os
import logging

def listar_contenidos_carpeta(ruta='.'):
    """
    Debemos Listar todos los elementos en la carpeta especificada por 'ruta'.
    Imprime el número de elementos y los nombres de cada uno.
    """
    try:
        # Aqui debemos Listar todos los elementos en la carpeta
        elementos = os.listdir(ruta)
        
        # Imprimir el número de elementos
        print(f"Elementos en '{ruta}': {len(elementos)}")
        
        # Imprimir los nombres de los elementos
        for elemento in elementos:
            print(elemento)
    except Exception as e:
        # Configurar el logging para registrar errores
        logging.basicConfig(filename='error.log', level=logging.ERROR)
        logging.error(f"Error al listar contenidos: {e}")

if __name__ == "__main__":
    # Se define la ruta de la carpeta que deseas listar
    ruta = '.'  # Usa la ruta actual como ejemplo
    
    # Se llama a la función para listar los contenidos
    listar_contenidos_carpeta(ruta)

