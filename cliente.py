import requests

# URL del servidor de procesamiento de imágenes
url_procesar = 'http://127.0.0.1:5001/procesar_imagen'

# URL del servidor de almacenamiento
url_almacenar = 'http://127.0.0.1:5002/almacenar_resultado'

# Ruta del archivo DICOM
file_path = 'C:/Users/00dan/Documents/prueba_tecnica_desarrollador_junior/sample-01-dicom.dcm'

# Enviar imagen al servidor de procesamiento
with open(file_path, 'rb') as f:
    response = requests.post(url_procesar, files={'file': f})

    if response.status_code == 200:
        resultado = response.json()
        print('Resultado del procesamiento:', resultado)

        # Enviar los resultados al servidor de almacenamiento
        response = requests.post(url_almacenar, json=resultado)
        print('Respuesta del almacenamiento:', response.json())
    else:
        print('Error en el procesamiento:', response.json())
