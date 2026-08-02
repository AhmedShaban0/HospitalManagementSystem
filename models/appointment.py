"""
Appointment Model Class.
Demonstrates:
- Concept #8: Aggregation (References Doctor and Patient which exist independently)
- Concept #4: Encapsulation (Private fields)
- Concept #12: Magic Methods (__str__, __repr__)
- Concept #17: Type Hints
- Concept #18: Documentation (Docstrings)
"""

from typing import Dict, Any, Optional
from .doctor import Doctor
from .patient import Patient
from utils.validator import Validator


class Appointment:
    """
    Represents an appointment between a Doctor and a Patient.
    Demonstrates Aggregation as Doctor and Patient exist independently outside of Appointment.
    """

    def __init__(
        self,
        appointment_id: str,
        patient_id: str,
        doctor_id: str,
        date_time: str,
        status: str = "Scheduled",
        notes: str = "",
        patient: Optional[Patient] = None,
        doctor: Optional[Doctor] = None
    ) -> None:
        """Initialize an Appointment instance."""
        self._appointment_id: str = Validator.validate_non_empty(appointment_id, "Appointment ID")
        self._patient_id: str = Validator.validate_non_empty(patient_id, "Patient ID")
        self._doctor_id: str = Validator.validate_non_empty(doctor_id, "Doctor ID")
        self._date_time: str = Validator.validate_datetime_str(date_time)
        self._status: str = status.strip() if status else "Scheduled"
        self._notes: str = notes.strip() if notes else ""

        # Concept #8: Aggregation references to Doctor and Patient instances
        self._patient: Optional[Patient] = patient
        self._doctor: Optional[Doctor] = doctor

    # --- Properties ---

    @property
    def appointment_id(self) -> str:
        """Get appointment ID."""
        return self._appointment_id

    @property
    def patient_id(self) -> str:
        """Get patient ID."""
        return self._patient_id

    @property
    def doctor_id(self) -> str:
        """Get doctor ID."""
        return self._doctor_id

    @property
    def date_time(self) -> str:
        """Get appointment date and time."""
        return self._date_time

    @date_time.setter
    def date_time(self, value: str) -> None:
        """Set appointment date and time."""
        self._date_time = Validator.validate_datetime_str(value)

    @property
    def status(self) -> str:
        """Get appointment status."""
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        """Set appointment status."""
        self._status = Validator.validate_non_empty(value, "Status")

    @property
    def notes(self) -> str:
        """Get appointment notes."""
        return self._notes

    @notes.setter
    def notes(self, value: str) -> None:
        """Set appointment notes."""
        self._notes = value.strip()

    @property
    def patient(self) -> Optional[Patient]:
        """Get aggregated Patient instance."""
        return self._patient

    @patient.setter
    def patient(self, p: Patient) -> None:
        """Set aggregated Patient instance."""
        self._patient = p
        self._patient_id = p.id

    @property
    def doctor(self) -> Optional[Doctor]:
        """Get aggregated Doctor instance."""
        return self._doctor

    @doctor.setter
    def doctor(self, d: Doctor) -> None:
        """Set aggregated Doctor instance."""
        self._doctor = d
        self._doctor_id = d.id

    # --- Methods ---

    def display_information(self) -> str:
        """Return formatted string detailing the appointment."""
        pat_name = self._patient.name if self._patient else f"ID: {self._patient_id}"
        doc_name = f"Dr. {self._doctor.name}" if self._doctor else f"ID: {self._doctor_id}"

        return (
            f"[APPOINTMENT INFO]\n"
            f"  ID:         {self._appointment_id}\n"
            f"  Patient:    {pat_name}\n"
            f"  Doctor:     {doc_name}\n"
            f"  Date/Time:  {self._date_time}\n"
            f"  Status:     {self._status}\n"
            f"  Notes:      {self._notes if self._notes else 'N/A'}"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert Appointment to dictionary for JSON persistence."""
        return {
            "appointment_id": self._appointment_id,
            "patient_id": self._patient_id,
            "doctor_id": self._doctor_id,
            "date_time": self._date_time,
            "status": self._status,
            "notes": self._notes
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Appointment":
        """Reconstruct Appointment from dictionary."""
        return cls(
            appointment_id=data["appointment_id"],
            patient_id=data["patient_id"],
            doctor_id=data["doctor_id"],
            date_time=data["date_time"],
            status=data.get("status", "Scheduled"),
            notes=data.get("notes", "")
        )

    # --- Concept #12: Magic Methods ---

    def __str__(self) -> str:
        return f"Appointment[{self._appointment_id}] (Patient: {self._patient_id}, Doctor: {self._doctor_id}, Date: {self._date_time}, Status: {self._status})"

    def __repr__(self) -> str:
        return f"<Appointment(id='{self._appointment_id}', datetime='{self._date_time}', status='{self._status}')>"
