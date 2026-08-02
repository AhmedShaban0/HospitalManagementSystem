"""
Hospital Container Model Class.
Demonstrates:
- Concept #7: Composition & Aggregation Management
- Concept #9: Class Variables
- Concept #10: Class Methods
- Concept #12: Magic Methods (__len__, __str__)
- Concept #17: Type Hints
- Concept #18: Documentation (Docstrings)
"""

from typing import Dict, List, Optional, Any
from .patient import Patient
from .doctor import Doctor
from .employee import Employee
from .appointment import Appointment
from .medical_record import MedicalRecord
from exceptions.custom_exceptions import (
    PatientNotFoundError,
    DoctorNotFoundError,
    AppointmentNotFoundError,
    DuplicateIDError,
    SchedulingConflictError,
)


class Hospital:
    """
    Main Hospital container managing Patients, Doctors, Employees, and Appointments.
    """

    # Concept #9: Class Variable
    hospital_name: str = "Central City General Hospital"
    version: str = "1.0.0"

    def __init__(self, name: str = "Central City General Hospital") -> None:
        """Initialize Hospital storage containers."""
        self._name: str = name
        # Composition containers
        self._patients: Dict[str, Patient] = {}
        self._doctors: Dict[str, Doctor] = {}
        self._employees: Dict[str, Employee] = {}
        self._appointments: Dict[str, Appointment] = {}

    # --- Properties ---

    @property
    def name(self) -> str:
        """Get hospital name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set hospital name."""
        if value and value.strip():
            self._name = value.strip()

    @property
    def patients(self) -> Dict[str, Patient]:
        """Get copy/reference of patients dict."""
        return self._patients

    @property
    def doctors(self) -> Dict[str, Doctor]:
        """Get copy/reference of doctors dict."""
        return self._doctors

    @property
    def employees(self) -> Dict[str, Employee]:
        """Get copy/reference of employees dict."""
        return self._employees

    @property
    def appointments(self) -> Dict[str, Appointment]:
        """Get copy/reference of appointments dict."""
        return self._appointments

    # --- Patient Operations ---

    def add_patient(self, patient: Patient) -> None:
        """Add a new patient to the hospital."""
        if patient.id in self._patients:
            raise DuplicateIDError("Patient", patient.id)
        self._patients[patient.id] = patient

    def update_patient(self, patient_id: str, name: Optional[str] = None, age: Optional[int] = None,
                       contact_info: Optional[str] = None, blood_group: Optional[str] = None) -> Patient:
        """Update existing patient details."""
        patient = self.get_patient(patient_id)
        if name:
            patient.name = name
        if age is not None:
            patient.age = age
        if contact_info:
            patient.contact_info = contact_info
        if blood_group:
            patient.blood_group = blood_group
        return patient

    def remove_patient(self, patient_id: str) -> Patient:
        """Remove a patient from the hospital."""
        if patient_id not in self._patients:
            raise PatientNotFoundError(patient_id)
        # Also cancel or handle appointments associated with this patient
        return self._patients.pop(patient_id)

    def get_patient(self, patient_id: str) -> Patient:
        """Retrieve patient by ID."""
        if patient_id not in self._patients:
            raise PatientNotFoundError(patient_id)
        return self._patients[patient_id]

    def search_patients(self, query: str) -> List[Patient]:
        """Search patients by ID or name substring."""
        q = query.lower().strip()
        return [p for p in self._patients.values() if q in p.id.lower() or q in p.name.lower()]

    def get_all_patients(self) -> List[Patient]:
        """Return list of all registered patients."""
        return list(self._patients.values())

    # --- Doctor Operations ---

    def add_doctor(self, doctor: Doctor) -> None:
        """Add a new doctor to the hospital."""
        if doctor.id in self._doctors:
            raise DuplicateIDError("Doctor", doctor.id)
        self._doctors[doctor.id] = doctor

    def update_doctor(self, doctor_id: str, name: Optional[str] = None, specialization: Optional[str] = None,
                      contact_info: Optional[str] = None, salary: Optional[float] = None) -> Doctor:
        """Update existing doctor details."""
        doctor = self.get_doctor(doctor_id)
        if name:
            doctor.name = name
        if specialization:
            doctor.specialization = specialization
        if contact_info:
            doctor.contact_info = contact_info
        if salary is not None:
            doctor.salary = salary
        return doctor

    def remove_doctor(self, doctor_id: str) -> Doctor:
        """Remove a doctor from the hospital."""
        if doctor_id not in self._doctors:
            raise DoctorNotFoundError(doctor_id)
        return self._doctors.pop(doctor_id)

    def get_doctor(self, doctor_id: str) -> Doctor:
        """Retrieve doctor by ID."""
        if doctor_id not in self._doctors:
            raise DoctorNotFoundError(doctor_id)
        return self._doctors[doctor_id]

    def search_doctors(self, query: str) -> List[Doctor]:
        """Search doctors by ID, name, or specialization."""
        q = query.lower().strip()
        return [
            d for d in self._doctors.values()
            if q in d.id.lower() or q in d.name.lower() or q in d.specialization.lower()
        ]

    def get_all_doctors(self) -> List[Doctor]:
        """Return list of all registered doctors."""
        return list(self._doctors.values())

    # --- Appointment Operations ---

    def schedule_appointment(self, appointment: Appointment) -> None:
        """Schedule a new appointment checking for ID & Doctor schedule conflicts."""
        if appointment.appointment_id in self._appointments:
            raise DuplicateIDError("Appointment", appointment.appointment_id)

        # Verify Patient and Doctor exist
        patient = self.get_patient(appointment.patient_id)
        doctor = self.get_doctor(appointment.doctor_id)

        # Check for scheduling conflict (Doctor booked at exact same date_time)
        for appt in self._appointments.values():
            if appt.doctor_id == appointment.doctor_id and appt.date_time == appointment.date_time and appt.status != "Cancelled":
                raise SchedulingConflictError(appointment.doctor_id, appointment.date_time)

        # Link Aggregation references
        appointment.patient = patient
        appointment.doctor = doctor

        self._appointments[appointment.appointment_id] = appointment

    def cancel_appointment(self, appointment_id: str) -> Appointment:
        """Cancel an existing appointment."""
        if appointment_id not in self._appointments:
            raise AppointmentNotFoundError(appointment_id)
        appointment = self._appointments[appointment_id]
        appointment.status = "Cancelled"
        return appointment

    def get_all_appointments(self) -> List[Appointment]:
        """Return list of all appointments."""
        return list(self._appointments.values())

    # --- Medical Record Operations ---

    def create_medical_record(self, patient_id: str, record_id: str, diagnosis: str, treatment: str, notes: str = "") -> MedicalRecord:
        """Create and attach a medical record to a patient (Composition)."""
        patient = self.get_patient(patient_id)
        # Check if record_id already exists in this patient's history
        for rec in patient.medical_records:
            if rec.record_id == record_id:
                raise DuplicateIDError("Medical Record", record_id)

        rec = MedicalRecord(
            record_id=record_id,
            patient_id=patient_id,
            diagnosis=diagnosis,
            treatment=treatment,
            notes=notes
        )
        patient.add_medical_record(rec)
        return rec

    def update_medical_record(self, patient_id: str, record_id: str, diagnosis: Optional[str] = None,
                              treatment: Optional[str] = None, notes: Optional[str] = None) -> MedicalRecord:
        """Update an existing medical record for a patient."""
        patient = self.get_patient(patient_id)
        target_record: Optional[MedicalRecord] = None
        for rec in patient.medical_records:
            if rec.record_id == record_id:
                target_record = rec
                break

        if not target_record:
            raise InvalidInputError("Medical Record ID", f"Record '{record_id}' not found for patient '{patient_id}'.")

        if diagnosis:
            target_record.diagnosis = diagnosis
        if treatment:
            target_record.treatment = treatment
        if notes is not None:
            target_record.notes = notes
        return target_record

    # --- Statistics & Summary ---

    def get_statistics(self) -> Dict[str, Any]:
        """Return key operational statistics of the hospital."""
        active_appointments = sum(1 for a in self._appointments.values() if a.status == "Scheduled")
        cancelled_appointments = sum(1 for a in self._appointments.values() if a.status == "Cancelled")
        total_medical_records = sum(len(p.medical_records) for p in self._patients.values())
        total_doctor_payroll = sum(d.salary for d in self._doctors.values())

        return {
            "hospital_name": self._name,
            "total_patients": len(self._patients),
            "total_doctors": len(self._doctors),
            "total_employees": len(self._employees),
            "total_appointments": len(self._appointments),
            "active_appointments": active_appointments,
            "cancelled_appointments": cancelled_appointments,
            "total_medical_records": total_medical_records,
            "total_doctor_payroll": total_doctor_payroll,
        }

    # --- Concept #10: Class Method ---

    @classmethod
    def get_system_version(cls) -> str:
        """Return application version string."""
        return f"{cls.hospital_name} System v{cls.version}"

    # --- Concept #12: Magic Methods ---

    def __len__(self) -> int:
        """Magic method __len__ returns total number of patients managed."""
        return len(self._patients)

    def __str__(self) -> str:
        return f"Hospital('{self._name}') [Patients: {len(self._patients)}, Doctors: {len(self._doctors)}, Appointments: {len(self._appointments)}]"
