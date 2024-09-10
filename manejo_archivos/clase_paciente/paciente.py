class Paciente:
    def __init__(self, patient_id, name, age, weight, height, cholesterol, heart_rate):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.cholesterol = cholesterol
        self.heart_rate = heart_rate

    def calcular_bmi(self):
        """Calcula el índice de masa corporal (BMI)"""
        try:
            height_m = self.height / 100  # Convertir la altura a metros
            bmi = self.weight / (height_m ** 2)
            return round(bmi, 2)
        except ZeroDivisionError:
            return "Error: Altura no puede ser cero"

    def clasificar_colesterol(self):
        """Clasifica el nivel de colesterol"""
        if self.cholesterol < 200:
            return "Normal"
        elif 200 <= self.cholesterol < 240:
            return "Borderline High"
        else:
            return "High"

    def clasificar_ritmo_cardiaco(self):
        """Clasifica la frecuencia cardíaca"""
        if self.heart_rate < 60:
            return "Bradycardia"
        elif 60 <= self.heart_rate <= 100:
            return "Normal"
        else:
            return "Tachycardia"

    def actualizar_datos(self, datos):
        """
        Actualiza los datos del paciente con la información proporcionada en el diccionario 'datos'.
        Valida los datos antes de la actualización.
        """
        for key, value in datos.items():
            if hasattr(self, key):
                if key in ["age", "weight", "height", "cholesterol", "heart_rate"]:
                    try:
                        setattr(self, key, float(value))
                    except ValueError:
                        print(f"Error: El valor para {key} debe ser numérico.")
                else:
                    setattr(self, key, value)

    def __str__(self):
        return (f"ID: {self.patient_id}, Nombre: {self.name}, Edad: {self.age}, "
                f"Peso: {self.weight}, Altura: {self.height}, Colesterol: {self.cholesterol}, "
                f"Ritmo Cardíaco: {self.heart_rate}")
