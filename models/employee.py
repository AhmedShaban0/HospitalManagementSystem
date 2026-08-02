"""
Employee Model Class.
Demonstrates:
- Concept #3: Inheritance (inherits from Person)
- Concept #4: Encapsulation (_role, _salary, _department)
- Concept #6: Polymorphism (Overrides display_information)
"""

from typing import Dict, Any
from .person import Person
from utils.validator import Validator


class Employee(Person):
    """
    Represents a general hospital staff employee. Derived from Person.
    """

    def __init__(
        self,
        employee_id: str,
        name: str,
        age: int,
        gender: str,
        contact_info: str,
        role: str,
        department: str,
        salary: float
    ) -> None:
        """Initialize an Employee instance."""
        super().__init__(
            person_id=employee_id,
            name=name,
            age=age,
            gender=gender,
            contact_info=contact_info
        )
        self._role: str = Validator.validate_non_empty(role, "Role")
        self._department: str = Validator.validate_non_empty(department, "Department")
        self._salary: float = float(salary) if salary >= 0 else 0.0

    @property
    def role(self) -> str:
        """Get role."""
        return self._role

    @role.setter
    def role(self, value: str) -> None:
        """Set role."""
        self._role = Validator.validate_non_empty(value, "Role")

    @property
    def department(self) -> str:
        """Get department."""
        return self._department

    @department.setter
    def department(self, value: str) -> None:
        """Set department."""
        self._department = Validator.validate_non_empty(value, "Department")

    @property
    def salary(self) -> float:
        """Get salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Set salary."""
        self._salary = float(value) if value >= 0 else 0.0

    # --- Concept #6: Polymorphism ---

    def display_information(self) -> str:
        """Override display_information for Employee."""
        return (
            f"[EMPLOYEE INFO]\n"
            f"  ID:          {self.id}\n"
            f"  Name:        {self.name}\n"
            f"  Role:        {self._role}\n"
            f"  Department:  {self._department}\n"
            f"  Age:         {self.age}\n"
            f"  Gender:      {self.gender}\n"
            f"  Contact:     {self.contact_info}\n"
            f"  Salary:      ${self._salary:,.2f}"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert Employee to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "contact_info": self.contact_info,
            "role": self._role,
            "department": self._department,
            "salary": self._salary,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Employee":
        """Factory method to construct Employee from dict."""
        return cls(
            employee_id=data["id"],
            name=data["name"],
            age=data["age"],
            gender=data["gender"],
            contact_info=data["contact_info"],
            role=data["role"],
            department=data["department"],
            salary=data["salary"]
        )
