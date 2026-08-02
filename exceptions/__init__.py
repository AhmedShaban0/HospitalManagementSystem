"""
Custom Exception package initialization.
"""
from .custom_exceptions import (
    HospitalException,
    PatientNotFoundError,
    DoctorNotFoundError,
    AppointmentNotFoundError,
    DuplicateIDError,
    SchedulingConflictError,
    InvalidInputError,
)

__all__ = [
    "HospitalException",
    "PatientNotFoundError",
    "DoctorNotFoundError",
    "AppointmentNotFoundError",
    "DuplicateIDError",
    "SchedulingConflictError",
    "InvalidInputError",
]
