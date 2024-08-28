import numpy as np

def sumar_arrays(array1, array2):
    """Suma dos arrays de igual tamaño."""
    try:
        return np.add(array1, array2)
    except ValueError as e:
        print(f"Error al sumar arrays: {e}")
        return None

def restar_arrays(array1, array2):
    """Resta el segundo array del primero de igual tamaño."""
    try:
        return np.subtract(array1, array2)
    except ValueError as e:
        print(f"Error al restar arrays: {e}")
        return None

def multiplicar_arrays(array1, array2):
    """Multiplica dos arrays de igual tamaño."""
    try:
        return np.multiply(array1, array2)
    except ValueError as e:
        print(f"Error al multiplicar arrays: {e}")
        return None

def dividir_arrays(array1, array2):
    """Divide el primer array entre el segundo array de igual tamaño. Maneja división por cero."""
    try:
        with np.errstate(divide='ignore', invalid='ignore'):
            result = np.divide(array1, array2)
            result[np.isnan(result)] = 0  # Reemplaza NaN resultantes de la división por cero con 0
        return result
    except ValueError as e:
        print(f"Error al dividir arrays: {e}")
        return None

def generar_datos():
    """Genera arrays de prueba y realiza operaciones."""
    # Crear dos arrays de ejemplo
    array1 = np.array([1, 2, 3, 4, 5])
    array2 = np.array([5, 4, 3, 2, 1])

    # Realizar operaciones
    suma = sumar_arrays(array1, array2)
    resta = restar_arrays(array1, array2)
    multiplicacion = multiplicar_arrays(array1, array2)
    division = dividir_arrays(array1, array2)

    # Generar datos aleatorios para pruebas adicionales
    datos = np.random.randn(1000)

    # Calcular estadísticas
    media = np.mean(datos)
    desviacion_estandar = np.std(datos)
    mediana = np.median(datos)

    return array1, array2, suma, resta, multiplicacion, division, datos, media, desviacion_estandar, mediana

def imprimir_resultados(array1, array2, suma, resta, multiplicacion, division, datos, media, desviacion_estandar, mediana):
    """Imprime los resultados de las operaciones y estadísticas."""
    print(f"Array 1: {array1}")
    print(f"Array 2: {array2}")
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
    print(f"Datos: {datos}")
    print(f"Media: {media}")
    print(f"Desviación estándar: {desviacion_estandar}")
    print(f"Mediana: {mediana}")

if __name__ == "__main__":
    array1, array2, suma, resta, multiplicacion, division, datos, media, desviacion_estandar, mediana = generar_datos()
    imprimir_resultados(array1, array2, suma, resta, multiplicacion, division, datos, media, desviacion_estandar, mediana)
