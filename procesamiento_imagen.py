from flask import Flask, request, jsonify
import pydicom

app = Flask(__name__)

@app.route('/procesar_imagen', methods=['POST'])
def procesar_imagen():
    """
    Endpoint para procesar archivos DICOM.
    - Recibe un archivo DICOM.
    - Extrae y devuelve información como el nombre del paciente, fecha del estudio, modalidad.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    try:
        dicom_file = pydicom.dcmread(file)
        nombre_paciente = dicom_file.get('PatientName', 'No disponible')
        fecha_estudio = dicom_file.get('StudyDate', 'No disponible')
        modalidad = dicom_file.get('Modality', 'No disponible')

        resultado = {
            'nombre_paciente': nombre_paciente,
            'fecha_estudio': fecha_estudio,
            'modalidad': modalidad
        }

        return jsonify(resultado)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
