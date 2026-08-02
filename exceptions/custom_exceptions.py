"""
Custom exception classes for the Hospital Management System.
Demonstrates Concept #14: Custom Exceptions.
"""

class HospitalException(Exception):
    """Base exception class for all hospital management errors."""
    def __init__(self, message: str = "An error occurred in the Hospital Management System."):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"[Hospital Error] {self.message}"


class PatientNotFoundError(HospitalException):
    """Raised when a patient cannot be found in the system."""
    def __init__(self, patient_id: str):
        super().__init__(f"Patient with ID '{patient_id}' was not found.")
        self.patient_id = patient_id


class DoctorNotFoundError(HospitalException):
    """Raised when a doctor cannot be found in the system."""
    def __init__(self, doctor_id: str):
        super().__init__(f"Doctor with ID '{doctor_id}' was not found.")
        self.doctor_id = doctor_id


class AppointmentNotFoundError(HospitalException):
    """Raised when an appointment cannot be found in the system."""
    def __init__(self, appointment_id: str):
        super().__init__(f"Appointment with ID '{appointment_id}' was not found.")
        self.appointment_id = appointment_id


class DuplicateIDError(HospitalException):
    """Raised when attempting to add an entity with an existing ID."""
    def __init__(self, entity_name: str, entity_id: str):
        super().__init__(f"{entity_name} with ID '{entity_id}' already exists.")
        self.entity_name = entity_name
        self.entity_id = entity_id


class SchedulingConflictError(HospitalException):
    """Raised when an appointment time conflicts with another appointment."""
    def __init__(self, doctor_id: str, date_time: str):
        super().__init__(f"Doctor '{doctor_id}' is already booked at '{date_time}'.")
        self.doctor_id = doctor_id
        self.date_time = date_time


class InvalidInputError(HospitalException):
    """Raised when provided user input is invalid."""
    def __init__(self, field_name: str, reason: str):
        super().__init__(f"Invalid input for field '{field_name}': {reason}")
        self.field_name = field_name
        self.reason = reason
