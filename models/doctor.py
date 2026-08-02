"""
Doctor Model Class.
Demonstrates:
- Concept #3: Inheritance (inherits from Person)
- Concept #4: Encapsulation (_specialization, _salary)
- Concept #6: Polymorphism (Overrides display_information)
- Concept #9: Class Variables (total_doctors)
- Concept #10: Class Methods (get_total_doctors, from_dict)
"""

from typing import Dict, Any
from .person import Person
from utils.validator import Validator


class Doctor(Person):
    """
    Represents a doctor in the hospital system. Derived from Person.
    """

    # Concept #9: Class Variable tracking total doctors
    total_doctors: int = 0

    def __init__(
        self,
        doctor_id: str,
        name: str,
        age: int,
        gender: str,
        contact_info: str,
        specialization: str,
        salary: float
    ) -> None:
        """Initialize a Doctor instance."""
        super().__init__(
            person_id=doctor_id,
            name=name,
            age=age,
            gender=gender,
            contact_info=contact_info
        )
        self._specialization: str = Validator.validate_non_empty(specialization, "Specialization")
        self._salary: float = self._validate_salary(salary)

        # Increment class variable count
        Doctor.total_doctors += 1

    # --- Private validation helper ---

    @staticmethod
    def _validate_salary(salary: float) -> float:
        """Validate that salary is positive."""
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Salary must be a non-negative number.")
        return float(salary)

    # --- Properties ---

    @property
    def specialization(self) -> str:
        """Get doctor specialization."""
        return self._specialization

    @specialization.setter
    def specialization(self, value: str) -> None:
        """Set doctor specialization with validation."""
        self._specialization = Validator.validate_non_empty(value, "Specialization")

    @property
    def salary(self) -> float:
        """Get doctor salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Set doctor salary with validation."""
        self._salary = self._validate_salary(value)

    # --- Concept #6: Polymorphism ---

    def display_information(self) -> str:
        """Override display_information for Doctor."""
        return (
            f"[DOCTOR INFO]\n"
            f"  ID:             {self.id}\n"
            f"  Name:           Dr. {self.name}\n"
            f"  Specialization: {self._specialization}\n"
            f"  Age:            {self.age}\n"
            f"  Gender:         {self.gender}\n"
            f"  Contact:        {self.contact_info}\n"
            f"  Salary:         ${self._salary:,.2f}"
        )

    # --- Concept #10: Class Methods ---

    @classmethod
    def get_total_doctors(cls) -> int:
        """Get total number of Doctor instances created."""
        return cls.total_doctors

    # --- Serialization ---

    def to_dict(self) -> Dict[str, Any]:
        """Convert Doctor instance to dictionary for JSON persistence."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "contact_info": self.contact_info,
            "specialization": self._specialization,
            "salary": self._salary
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Doctor":
        """Reconstruct Doctor instance from dictionary."""
        return cls(
            doctor_id=data["id"],
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            contact_info=data["contact_info"],
            specialization=data["specialization"],
            salary=data["salary"]
        )
