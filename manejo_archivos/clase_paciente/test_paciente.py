from paciente import Paciente

# Crear una instancia de la clase Paciente
paciente1 = Paciente(patient_id=1, name="Juan", age=30, weight=70, height=175, cholesterol=220, heart_rate=85)

# Probar los métodos
print(f"Paciente ID: {paciente1.patient_id}")
print(f"Age: {paciente1.age}")
print(f"Weight: {paciente1.weight}")
print(f"Height: {paciente1.height}")
print(f"Cholesterol: {paciente1.cholesterol}")
print(f"HeartRate: {paciente1.heart_rate}")
print(f"BMI: {paciente1.calcular_bmi()}")
print(f"Clasificación del Colesterol: {paciente1.clasificar_colesterol()}")
print(f"Clasificación del Ritmo Cardiaco: {paciente1.clasificar_ritmo_cardiaco()}")

# Probar actualizar los datos del paciente
nuevos_datos = {"age": 35, "weight": 75, "cholesterol": 180}
paciente1.actualizar_datos(nuevos_datos)

# Verificar los nuevos datos
print("\nDespués de actualizar los datos:")
print(f"Age: {paciente1.age}")
print(f"Weight: {paciente1.weight}")
print(f"Cholesterol: {paciente1.cholesterol}")
