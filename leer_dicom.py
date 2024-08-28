import pydicom
import logging

# Configuración del logger
logging.basicConfig(filename='error.log', level=logging.ERROR)

def leer_dicom(ruta_archivo):
    """Lee y extrae datos de un archivo DICOM especificado por la ruta."""
    try:
        # Intentar leer el archivo DICOM
        ds = pydicom.dcmread(ruta_archivo)
        
        # Extraer y mostrar información del paciente
        nombre_paciente = ds.get('PatientName', 'No disponible')
        fecha_estudio = ds.get('StudyDate', 'No disponible')
        modalidad = ds.get('Modality', 'No disponible')
        edad_paciente = ds.get('PatientAge', 'No disponible')
        sexo_paciente = ds.get('PatientSex', 'No disponible')
        identificador_estudio = ds.get('StudyID', 'No disponible')
        
        # Imprimir la información extraída
        print(f"Leyendo archivo: {ruta_archivo}")
        print(f"Nombre del Paciente: {nombre_paciente}")
        print(f"Fecha del Estudio: {fecha_estudio}")
        print(f"Modalidad: {modalidad}")
        print(f"Edad del Paciente: {edad_paciente}")
        print(f"Sexo del Paciente: {sexo_paciente}")
        print(f"Identificador del Estudio: {identificador_estudio}")
        print("-" * 40)
    
    except Exception as e:
        # Manejar y registrar errores en caso de que el archivo no pueda ser leído
        logging.error(f"Error al leer el archivo {ruta_archivo}: {e}")
        print(f"Error al procesar el archivo {ruta_archivo}. Revisa error.log para más detalles.")

# Rutas de los archivos DICOM
archivos_dicom = [
    'C:/Users/00dan/Documents/prueba_tecnica_desarrollador_junior/sample-01-dicom.dcm',
    'C:/Users/00dan/Documents/prueba_tecnica_desarrollador_junior/sample-02-dicom.dcm'
]

# Leer y procesar cada archivo DICOM
for archivo in archivos_dicom:
    leer_dicom(archivo)
