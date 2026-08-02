"""
Hospital Service class managing application logic and JSON file persistence.
Demonstrates:
- Concept #15: File Handling (JSON save/load)
- Concept #13: Exception Handling
- Service pattern separating UI from domain logic.
"""

import json
import os
from typing import Dict, Any
from models.hospital import Hospital
from models.patient import Patient
from models.doctor import Doctor
from models.employee import Employee
from models.appointment import Appointment
from exceptions.custom_exceptions import HospitalException


class HospitalService:
    """
    Service layer providing persistence and high-level workflows.
    """

    def __init__(self, data_file_path: str = "files/hospital_data.json") -> None:
        """Initialize service with data file path and Hospital instance."""
        self._data_file_path: str = data_file_path
        self._hospital: Hospital = Hospital()
        
        # Ensure parent directory exists
        os.makedirs(os.path.dirname(self._data_file_path), exist_ok=True)

    @property
    def hospital(self) -> Hospital:
        """Get underlying Hospital container."""
        return self._hospital

    # --- Concept #15: File Handling (JSON Save / Load) ---

    def save_data(self) -> bool:
        """Save all hospital state to JSON file."""
        data: Dict[str, Any] = {
            "hospital_name": self._hospital.name,
            "patients": [p.to_dict() for p in self._hospital.get_all_patients()],
            "doctors": [d.to_dict() for d in self._hospital.get_all_doctors()],
            "employees": [e.to_dict() for e in self._hospital.employees.values()],
            "appointments": [a.to_dict() for a in self._hospital.get_all_appointments()]
        }

        try:
            with open(self._data_file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            raise HospitalException(f"Failed to save data file '{self._data_file_path}': {str(e)}")

    def load_data(self) -> bool:
        """Load hospital state from JSON file if exists."""
        if not os.path.exists(self._data_file_path):
            # Seed default demo data if file does not exist yet
            self._seed_initial_data()
            self.save_data()
            return True

        try:
            with open(self._data_file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if "hospital_name" in data:
                self._hospital.name = data["hospital_name"]

            # Load Patients
            for p_dict in data.get("patients", []):
                patient = Patient.from_dict(p_dict)
                self._hospital.add_patient(patient)

            # Load Doctors
            for d_dict in data.get("doctors", []):
                doctor = Doctor.from_dict(d_dict)
                self._hospital.add_doctor(doctor)

            # Load Employees
            for e_dict in data.get("employees", []):
                emp = Employee.from_dict(e_dict)
                self._hospital.employees[emp.id] = emp

            # Load Appointments
            for a_dict in data.get("appointments", []):
                appt = Appointment.from_dict(a_dict)
                try:
                    self._hospital.schedule_appointment(appt)
                except Exception:
                    # In case of load order or duplicate, store directly into dict
                    self._hospital.appointments[appt.appointment_id] = appt

            return True

        except Exception as e:
            raise HospitalException(f"Failed to load data file '{self._data_file_path}': {str(e)}")

    def _seed_initial_data(self) -> None:
        """Seed demo data for initial run."""
        p1 = Patient("P101", "John Doe", 34, "Male", "555-0101", "O+")
        p2 = Patient("P102", "Alice Smith", 28, "Female", "555-0102", "A+")
        self._hospital.add_patient(p1)
        self._hospital.add_patient(p2)

        d1 = Doctor("D201", "Sarah Connor", 45, "Female", "555-0201", "Cardiology", 120000.0)
        d2 = Doctor("D202", "Gregory House", 50, "Male", "555-0202", "Neurology", 150000.0)
        self._hospital.add_doctor(d1)
        self._hospital.add_doctor(d2)

        self._hospital.create_medical_record(
            patient_id="P101",
            record_id="MR301",
            diagnosis="Hypertension",
            treatment="Prescribed Lisinopril 10mg daily",
            notes="Regular blood pressure checks recommended."
        )

        appt1 = Appointment("A401", "P101", "D201", "2026-08-10 10:00", "Scheduled", "Routine Checkup")
        self._hospital.schedule_appointment(appt1)
