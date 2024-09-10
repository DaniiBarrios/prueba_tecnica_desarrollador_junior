from flask import Flask, request, jsonify
import pydicom
import numpy as np

app = Flask(__name__)

@app.route('/procesar_imagen', methods=['POST'])
def procesar_imagen():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    try:
        dicom_file = pydicom.dcmread(file)
        
        # Ejemplo de procesamiento: extraer algunos datos del archivo DICOM
        nombre_paciente = dicom_file.get('PatientName', 'No disponible')
        fecha_estudio = dicom_file.get('StudyDate', 'No disponible')
        modalidad = dicom_file.get('Modality', 'No disponible')
        
        # Procesar la imagen DICOM si tiene datos de imagen
        if 'PixelData' in dicom_file:
            pixel_array = dicom_file.pixel_array
            # Ejemplo: calcular la media de los píxeles
            media_pixeles = np.mean(pixel_array)
        else:
            media_pixeles = 'No disponible'
        
        resultado = {
            'nombre_paciente': str(nombre_paciente),
            'fecha_estudio': fecha_estudio,
            'modalidad': modalidad,
            'media_pixeles': media_pixeles
        }

        return jsonify(resultado)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Cambiar el puerto si es necesario
