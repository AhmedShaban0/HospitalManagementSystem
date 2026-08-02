"""
Validation utilities for the Hospital Management System.
Demonstrates Concept #11: Static Methods.
"""
import re
from datetime import datetime
from exceptions.custom_exceptions import InvalidInputError


class Validator:
    """Helper class containing static methods for input validation."""

    @staticmethod
    def validate_non_empty(value: str, field_name: str) -> str:
        """Validate that a string value is non-empty and non-whitespace."""
        if not value or not value.strip():
            raise InvalidInputError(field_name, "Value cannot be empty.")
        return value.strip()

    @staticmethod
    def validate_age(age: int) -> int:
        """Validate age is between 0 and 130."""
        if not isinstance(age, int) or age < 0 or age > 130:
            raise InvalidInputError("Age", f"Must be an integer between 0 and 130. Got: {age}")
        return age

    @staticmethod
    def validate_phone(phone: str) -> str:
        """Validate phone number format (digits, optional +, hyphen, spaces, 7-15 chars)."""
        cleaned = phone.strip()
        pattern = r"^\+?[0-9\s\-]{7,15}$"
        if not re.match(pattern, cleaned):
            raise InvalidInputError("Contact Info / Phone", "Must contain 7 to 15 digits (plus sign, hyphens allowed).")
        return cleaned

    @staticmethod
    def validate_id_format(entity_id: str, prefix: str) -> str:
        """Validate that an ID starts with a specific prefix and is non-empty."""
        cleaned = entity_id.strip().upper()
        if not cleaned:
            raise InvalidInputError("ID", "ID cannot be empty.")
        if prefix and not cleaned.startswith(prefix.upper()):
            raise InvalidInputError("ID", f"ID should start with prefix '{prefix.upper()}'.")
        return cleaned

    @staticmethod
    def validate_datetime_str(datetime_str: str) -> str:
        """Validate datetime string format (YYYY-MM-DD HH:MM)."""
        cleaned = datetime_str.strip()
        try:
            datetime.strptime(cleaned, "%Y-%m-%d %H:%M")
        except ValueError:
            raise InvalidInputError(
                "Date & Time",
                "Format must be 'YYYY-MM-DD HH:MM' (e.g., 2026-08-15 10:30)."
            )
        return cleaned
