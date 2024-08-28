from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)

@app.route('/operaciones', methods=['POST'])
def operaciones():
    """
    Endpoint para realizar operaciones con arrays.
    - Recibe dos arrays en formato JSON.
    - Realiza operaciones: suma, resta, multiplicación, división.
    - Calcula: media, desviación estándar, mediana.
    - Devuelve los resultados en formato JSON.
    """
    data = request.get_json()
    array1 = data.get('array1')
    array2 = data.get('array2')
    
    if not (array1 and array2):
        return jsonify({'error': 'Faltan datos'}), 400

    array1 = np.array(array1)
    array2 = np.array(array2)

    resultado = {
        'suma': (array1 + array2).tolist(),
        'resta': (array1 - array2).tolist(),
        'multiplicacion': (array1 * array2).tolist(),
        'division': (array1 / array2).tolist(),
        'media': float(np.mean(array1)),
        'desviacion': float(np.std(array1)),
        'mediana': float(np.median(array1))
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
