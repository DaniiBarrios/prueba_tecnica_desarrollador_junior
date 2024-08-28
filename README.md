
# Prueba Técnica - Daniela Barrios

## Instrucciones para la Ejecución del Proyecto

### 1. Requisitos Previos

Antes de ejecutar los scripts, asegúrate de tener instalados los siguientes paquetes:

- Python 3.x
- Django
- PostgreSQL
- Bibliotecas adicionales: `numpy`, `pandas`, `pydicom`, `scikit-learn`

Puedes instalarlos utilizando el siguiente comando:

```bash
pip install django psycopg2-binary numpy pandas pydicom scikit-learn
```

### 2. Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:

- `listar_contenidos.py`: Lista los contenidos de una carpeta especificada.
- `leer_csv.py`: Lee y procesa un archivo CSV, mostrando estadísticas.
- `leer_dicom.py`: Lee un archivo DICOM y muestra detalles del paciente.
- `oop.py`: Contiene las clases `PatientRecord` y `StudyRecord` para manejo de datos de pacientes y estudios.
- `multithreading_concurrencia.py`: Implementa hilos para procesar datos JSON y generar números pares e impares.
- `mi_proyecto/`: Contiene el proyecto Django para la API RESTful.

### 3. Ejecución de los Scripts

#### Listar Contenidos de una Carpeta

Ejecuta el script `listar_contenidos.py` para listar los archivos dentro de una carpeta:

```bash
python listar_contenidos.py
```

#### Leer y Procesar un Archivo CSV

Ejecuta el script `leer_csv.py` para leer un archivo CSV:

```bash
python leer_csv.py
```

#### Leer y Procesar un Archivo DICOM

Ejecuta el script `leer_dicom.py` para procesar un archivo DICOM:

```bash
python leer_dicom.py
```

#### Clases y Manejo de Objetos

El archivo `oop.py` contiene las clases necesarias para gestionar datos de pacientes y estudios:

```bash
python oop.py
```

#### Multithreading y Concurrencia

Ejecuta el script `multithreading_concurrencia.py` para ver la implementación de hilos:

```bash
python multithreading_concurrencia.py
```

### 4. Configuración y Ejecución de la API RESTful

#### Configuración

1. Ve al directorio `mi_proyecto/`.
2. Modifica el archivo `settings.py` para configurar la base de datos PostgreSQL.

#### Migraciones

Ejecuta las migraciones para configurar la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Ejecución del Servidor

Para correr el servidor Django:

```bash
python manage.py runserver
```

La API estará disponible en `http://127.0.0.1:8000/`.

### 5. Sistema Distribuido de Procesamiento de DICOM

Este apartado describe un diseño conceptual para un sistema distribuido de procesamiento de imágenes médicas. Para más detalles, consulta el documento de diseño en la carpeta correspondiente.

## Contacto

Para cualquier consulta, por favor contacta a Daniela Barrios en [00danielabarrios@gmail.com](mailto:00danielabarrios@gmail.com).
