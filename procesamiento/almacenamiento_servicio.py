from flask import Flask, request, jsonify

app = Flask(__name__)

# Almacena los resultados en una lista para demostración
resultados = []

@app.route('/almacenar_resultado', methods=['POST'])
def almacenar_resultado():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    resultados.append(data)
    return jsonify({'message': 'Resultado almacenado'}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)
