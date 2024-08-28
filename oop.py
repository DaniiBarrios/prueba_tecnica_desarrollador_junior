import logging
import pydicom

# Configurar el logging
logging.basicConfig(filename='patient_records.log', level=logging.INFO)

class PatientRecord:
    def __init__(self, name, age, birth_date, gender, weight, patient_id, id_type):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.gender = gender
        self.weight = weight
        self.patient_id = patient_id
        self.id_type = id_type
        self.diagnosis = None

    def update_diagnosis(self, new_diagnosis):
        """Actualiza el diagnóstico y registra el cambio"""
        old_diagnosis = self.diagnosis
        self.diagnosis = new_diagnosis
        logging.info(f"Updated diagnosis from '{old_diagnosis}' to '{new_diagnosis}' for patient {self.patient_id}")

    def __str__(self):
        return (f"PatientRecord(name={self.name}, age={self.age}, birth_date={self.birth_date}, "
                f"gender={self.gender}, weight={self.weight}, patient_id={self.patient_id}, "
                f"id_type={self.id_type}, diagnosis={self.diagnosis})")

class StudyRecord(PatientRecord):
    def __init__(self, name, age, birth_date, gender, weight, patient_id, id_type,
                 modality=None, study_date=None, study_time=None, study_uid=None,
                 series_number=None, number_of_frames=None):
        super().__init__(name, age, birth_date, gender, weight, patient_id, id_type)
        self.modality = modality
        self.study_date = study_date
        self.study_time = study_time
        self.study_uid = study_uid
        self.series_number = series_number
        self.number_of_frames = number_of_frames

    def load_study_from_dicom(self, dicom_file_path):
        """Carga detalles del estudio desde un archivo DICOM"""
        try:
            dicom_data = pydicom.dcmread(dicom_file_path)
            self.modality = dicom_data.Modality
            self.study_date = dicom_data.StudyDate
            self.study_time = dicom_data.StudyTime
            self.study_uid = dicom_data.StudyInstanceUID
            self.series_number = dicom_data.SeriesNumber
            self.number_of_frames = dicom_data.NumberOfFrames
        except Exception as e:
            logging.error(f"Error loading DICOM file: {e}")

    def __str__(self):
        return (super().__str__() + 
                f", modality={self.modality}, study_date={self.study_date}, study_time={self.study_time}, "
                f"study_uid={self.study_uid}, series_number={self.series_number}, number_of_frames={self.number_of_frames}")
