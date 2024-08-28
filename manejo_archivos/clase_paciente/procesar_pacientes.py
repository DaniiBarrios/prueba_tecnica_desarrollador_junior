import threading
from paciente import Paciente

def procesar_paciente(paciente):
    """
    Aquì se hace una función que simula el procesamiento de un paciente.
    """
    print(f"Procesando a {paciente.name} (ID: {paciente.patient_id})")
    # Simular algún procesamiento
    paciente.actualizar_datos({"cholesterol": 200})
    print(f"Paciente {paciente.name} procesado con éxito.")

if __name__ == "__main__":
    # Crear varios pacientes
    pacientes = [
        Paciente(1, "Juan Pérez", 30, 70, 175, 190, 80),
        Paciente(2, "María López", 40, 65, 160, 200, 85),
        Paciente(3, "Carlos Martínez", 25, 80, 180, 210, 90)
    ]

    # Crear un hilo para cada paciente
    hilos = []
    for paciente in pacientes:
        hilo = threading.Thread(target=procesar_paciente, args=(paciente,))
        hilos.append(hilo)
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    print("Procesamiento concurrente de pacientes completado.")
