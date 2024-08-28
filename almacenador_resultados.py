from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para almacenar resultados
@app.route('/almacenar_resultado', methods=['POST'])
def almacenar_resultado():
    data = request.get_json()
    
    # Por simplicidad, solo devolveremos los datos recibidos
    return jsonify({'mensaje': 'Datos almacenados con éxito', 'datos': data})

if __name__ == '__main__':
    app.run(port=5002, debug=True)  # Cambiar el puerto si es necesario
