"""
Patient Model Class.
Demonstrates:
- Concept #3: Inheritance (inherits from Person)
- Concept #4: Encapsulation (Private fields _blood_group, _medical_records)
- Concept #6: Polymorphism (Overrides display_information)
- Concept #7: Composition (Patient owns MedicalRecord instances)
- Concept #9: Class Variables (total_patients)
- Concept #10: Class Methods (get_total_patients, from_dict)
- Concept #12: Magic Methods (__len__ returns count of medical records)
"""

from typing import List, Dict, Any, Optional
from .person import Person
from .medical_record import MedicalRecord
from utils.validator import Validator


class Patient(Person):
    """
    Represents a hospital patient. Derived from Person.
    Owns its MedicalRecords via Composition.
    """

    # Concept #9: Class Variable tracking total patients
    total_patients: int = 0

    def __init__(
        self,
        patient_id: str,
        name: str,
        age: int,
        gender: str,
        contact_info: str,
        blood_group: str,
        medical_records: Optional[List[MedicalRecord]] = None
    ) -> None:
        """Initialize a Patient instance."""
        super().__init__(
            person_id=patient_id,
            name=name,
            age=age,
            gender=gender,
            contact_info=contact_info
        )
        self._blood_group: str = Validator.validate_non_empty(blood_group, "Blood Group")

        # Concept #7: Composition (Patient owns MedicalRecords)
        self._medical_records: List[MedicalRecord] = medical_records if medical_records is not None else []

        # Increment class variable count
        Patient.total_patients += 1

    # --- Properties ---

    @property
    def blood_group(self) -> str:
        """Get patient blood group."""
        return self._blood_group

    @blood_group.setter
    def blood_group(self, value: str) -> None:
        """Set patient blood group with validation."""
        self._blood_group = Validator.validate_non_empty(value, "Blood Group")

    @property
    def medical_records(self) -> List[MedicalRecord]:
        """Get patient medical records list."""
        return self._medical_records

    # --- Methods ---

    def add_medical_record(self, record: MedicalRecord) -> None:
        """Add a new medical record entry to this patient."""
        self._medical_records.append(record)

    def get_medical_history_summary(self) -> str:
        """Return formatted string of all medical records for this patient."""
        if not self._medical_records:
            return f"No medical history recorded for Patient '{self.name}' (ID: {self.id})."
        
        lines = [f"=== Medical History for Patient: {self.name} (ID: {self.id}) ==="]
        for idx, rec in enumerate(self._medical_records, 1):
            lines.append(f"\n[Record #{idx}]\n{rec.display_details()}")
        return "\n".join(lines)

    # --- Concept #6: Polymorphism ---

    def display_information(self) -> str:
        """Override display_information for Patient."""
        return (
            f"[PATIENT INFO]\n"
            f"  ID:           {self.id}\n"
            f"  Name:         {self.name}\n"
            f"  Age:          {self.age}\n"
            f"  Gender:       {self.gender}\n"
            f"  Contact:      {self.contact_info}\n"
            f"  Blood Group:  {self._blood_group}\n"
            f"  Total Records:{len(self._medical_records)}"
        )

    # --- Concept #10: Class Methods ---

    @classmethod
    def get_total_patients(cls) -> int:
        """Get total number of Patient instances created."""
        return cls.total_patients

    # --- Concept #12: Magic Methods ---

    def __len__(self) -> int:
        """Magic method __len__ returns total number of medical records owned."""
        return len(self._medical_records)

    # --- Serialization ---

    def to_dict(self) -> Dict[str, Any]:
        """Convert Patient instance to dictionary for JSON persistence."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "contact_info": self.contact_info,
            "blood_group": self._blood_group,
            "medical_records": [rec.to_dict() for rec in self._medical_records]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Patient":
        """Reconstruct Patient instance from dictionary."""
        records = [MedicalRecord.from_dict(r) for r in data.get("medical_records", [])]
        return cls(
            patient_id=data["id"],
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            contact_info=data["contact_info"],
            blood_group=data["blood_group"],
            medical_records=records
        )
