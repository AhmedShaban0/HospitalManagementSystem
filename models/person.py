"""
Person Abstract Base Class module.
Demonstrates:
- Concept #1: Classes & Objects
- Concept #2: Constructors
- Concept #3: Inheritance (Base Class)
- Concept #4: Encapsulation (Properties/Getters/Setters)
- Concept #5: Abstraction (abc.ABC & @abstractmethod)
- Concept #9: Class Variables
- Concept #10: Class Methods
- Concept #12: Magic Methods (__str__, __repr__, __eq__)
- Concept #17: Type Hints
- Concept #18: Documentation (Docstrings)
"""

from abc import ABC, abstractmethod
from typing import Any
from utils.validator import Validator


class Person(ABC):
    """
    Abstract Base Class representing a general person in the hospital system.
    Cannot be instantiated directly.
    """

    # Concept #9: Class Variable tracking total person instances
    total_persons: int = 0

    def __init__(
        self,
        person_id: str,
        name: str,
        age: int,
        gender: str,
        contact_info: str
    ) -> None:
        """
        Constructor initializing common person attributes.
        Demonstrates Encapsulation with private/protected attributes.
        """
        self._id: str = Validator.validate_non_empty(person_id, "Person ID")
        self._name: str = Validator.validate_non_empty(name, "Name")
        self._age: int = Validator.validate_age(age)
        self._gender: str = Validator.validate_non_empty(gender, "Gender")
        self._contact_info: str = Validator.validate_non_empty(contact_info, "Contact Info")

        # Increment class variable
        Person.total_persons += 1

    # --- Concept #4: Encapsulation (Getters and Setters via Properties) ---

    @property
    def id(self) -> str:
        """Get person ID."""
        return self._id

    @property
    def name(self) -> str:
        """Get person name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set person name with validation."""
        self._name = Validator.validate_non_empty(value, "Name")

    @property
    def age(self) -> int:
        """Get person age."""
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        """Set person age with validation."""
        self._age = Validator.validate_age(value)

    @property
    def gender(self) -> str:
        """Get person gender."""
        return self._gender

    @gender.setter
    def gender(self, value: str) -> None:
        """Set person gender with validation."""
        self._gender = Validator.validate_non_empty(value, "Gender")

    @property
    def contact_info(self) -> str:
        """Get person contact info."""
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value: str) -> None:
        """Set person contact info with validation."""
        self._contact_info = Validator.validate_non_empty(value, "Contact Info")

    # --- Concept #5: Abstraction ---

    @abstractmethod
    def display_information(self) -> str:
        """
        Abstract method to display detailed information about the person.
        Must be overridden by all derived subclasses (Polymorphism).
        """
        pass

    # --- Concept #10: Class Methods ---

    @classmethod
    def get_total_persons(cls) -> int:
        """Class method returning the total number of Person objects created."""
        return cls.total_persons

    # --- Concept #12: Magic Methods ---

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"{self.__class__.__name__} [ID: {self._id}, Name: {self._name}, Age: {self._age}, Gender: {self._gender}]"

    def __repr__(self) -> str:
        """Developer-friendly string representation."""
        return (
            f"<{self.__class__.__name__}(id='{self._id}', name='{self._name}', "
            f"age={self._age}, gender='{self._gender}', contact='{self._contact_info}')>"
        )

    def __eq__(self, other: Any) -> bool:
        """Check equality based on person ID."""
        if isinstance(other, Person):
            return self._id == other._id
        return False
