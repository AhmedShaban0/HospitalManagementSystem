"""
Medical Record model class.
Used in Composition relationship with Patient.
Demonstrates Encapsulation, Type Hints, Serialization, Magic Methods, and Documentation.
"""

from typing import Dict, Any
from datetime import datetime
from utils.validator import Validator


class MedicalRecord:
    """
    Represents a medical record entry for a patient.
    Owned by Patient via Composition.
    """

    def __init__(
        self,
        record_id: str,
        patient_id: str,
        diagnosis: str,
        treatment: str,
        notes: str = "",
        date_str: str = ""
    ) -> None:
        """Initialize a MedicalRecord instance."""
        self._record_id: str = Validator.validate_non_empty(record_id, "Record ID")
        self._patient_id: str = Validator.validate_non_empty(patient_id, "Patient ID")
        self._diagnosis: str = Validator.validate_non_empty(diagnosis, "Diagnosis")
        self._treatment: str = Validator.validate_non_empty(treatment, "Treatment")
        self._notes: str = notes.strip() if notes else ""
        self._date: str = date_str.strip() if date_str else datetime.now().strftime("%Y-%m-%d %H:%M")

    # --- Properties ---

    @property
    def record_id(self) -> str:
        """Get record ID."""
        return self._record_id

    @property
    def patient_id(self) -> str:
        """Get patient ID."""
        return self._patient_id

    @property
    def diagnosis(self) -> str:
        """Get diagnosis."""
        return self._diagnosis

    @diagnosis.setter
    def diagnosis(self, value: str) -> None:
        """Set diagnosis."""
        self._diagnosis = Validator.validate_non_empty(value, "Diagnosis")

    @property
    def treatment(self) -> str:
        """Get treatment."""
        return self._treatment

    @treatment.setter
    def treatment(self, value: str) -> None:
        """Set treatment."""
        self._treatment = Validator.validate_non_empty(value, "Treatment")

    @property
    def notes(self) -> str:
        """Get notes."""
        return self._notes

    @notes.setter
    def notes(self, value: str) -> None:
        """Set notes."""
        self._notes = value.strip()

    @property
    def date(self) -> str:
        """Get record date."""
        return self._date

    # --- Methods ---

    def display_details(self) -> str:
        """Return formatted string of record details."""
        return (
            f"Record ID: {self._record_id} | Date: {self._date}\n"
            f"  Patient ID: {self._patient_id}\n"
            f"  Diagnosis:  {self._diagnosis}\n"
            f"  Treatment:  {self._treatment}\n"
            f"  Notes:      {self._notes if self._notes else 'N/A'}"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Serialize medical record to dictionary for JSON storage."""
        return {
            "record_id": self._record_id,
            "patient_id": self._patient_id,
            "diagnosis": self._diagnosis,
            "treatment": self._treatment,
            "notes": self._notes,
            "date": self._date,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MedicalRecord":
        """Factory class method to create a MedicalRecord from a dictionary."""
        return cls(
            record_id=data["record_id"],
            patient_id=data["patient_id"],
            diagnosis=data["diagnosis"],
            treatment=data["treatment"],
            notes=data.get("notes", ""),
            date_str=data.get("date", "")
        )

    # --- Magic Methods ---

    def __str__(self) -> str:
        return f"MedicalRecord[{self._record_id}] (Patient: {self._patient_id}, Diagnosis: {self._diagnosis})"

    def __repr__(self) -> str:
        return f"<MedicalRecord(id='{self._record_id}', patient='{self._patient_id}')>"
