# Hospital Management System (OOP Assignment)

A modular, maintainable, reusable, and scalable console-based **Hospital Management System** implemented in Python using Object-Oriented Programming (OOP) principles.

---

## 📁 Project Structure

```text
HospitalManagementSystem/
├── main.py                     # Console UI Entry Point & Menu System
├── models/
│   ├── __init__.py
│   ├── person.py              # Abstract Base Class (Inheritance, Abstraction, Polymorphism)
│   ├── patient.py             # Patient subclass (Composition with MedicalRecord)
│   ├── doctor.py              # Doctor subclass
│   ├── employee.py            # Staff Employee subclass
│   ├── appointment.py         # Appointment class (Aggregation with Doctor & Patient)
│   ├── medical_record.py      # Medical Record class
│   └── hospital.py           # Hospital container class
├── services/
│   ├── __init__.py
│   └── hospital_service.py    # Service Layer & JSON Persistence Engine
├── exceptions/
│   ├── __init__.py
│   └── custom_exceptions.py   # Custom Exception Classes
├── utils/
│   ├── __init__.py
│   └── validator.py           # Input Validation Static Methods
├── files/
│   └── hospital_data.json     # Saved JSON Data Storage
└── README.md                  # Project Documentation
```

---

## 🎯 Functional Requirements Implemented

1. **Patient Management**:
   - Add a new patient
   - Update patient information
   - Remove a patient
   - Search for a patient (by ID or Name)
   - Display all patients

2. **Doctor Management**:
   - Add a new doctor
   - Update doctor information
   - Remove a doctor
   - Search for a doctor (by ID, Name, or Specialization)
   - Display all doctors

3. **Appointment Management**:
   - Schedule an appointment (with doctor schedule conflict checking)
   - Cancel an appointment
   - Display all appointments

4. **Medical Records**:
   - Create a medical record (Composition owned by Patient)
   - Update a medical record
   - Display a patient's medical history

5. **Hospital Management**:
   - Display hospital statistics (counts, payroll, active appointments)
   - Save all data before exiting
   - Automatically load saved data when application starts

---

## 🛠️ Mapping of the 18 Technical OOP Requirements

| # | Technical Concept | Implementation Location & Explanation |
|---|---|---|
| 1 | **Classes & Objects** | Defined in `models/`: `Person`, `Patient`, `Doctor`, `Employee`, `Appointment`, `MedicalRecord`, `Hospital`. |
| 2 | **Constructors** | Explicit `__init__()` constructors in all model classes with type hints and validation. |
| 3 | **Inheritance** | `Person` is the base class; `Patient`, `Doctor`, and `Employee` inherit from `Person`. |
| 4 | **Encapsulation** | Private/protected attributes (e.g. `_id`, `_age`, `_salary`, `_medical_records`) accessed via `@property` getters and setters with validation rules. |
| 5 | **Abstraction** | `Person` inherits from `abc.ABC` and defines the abstract method `@abstractmethod def display_information(self) -> str`. |
| 6 | **Polymorphism** | Overridden `display_information()` implementations in `Patient`, `Doctor`, and `Employee`. |
| 7 | **Composition** | `Patient` owns a list of `MedicalRecord` objects (if patient is deleted, records belong to patient). `Hospital` contains collections of objects. |
| 8 | **Aggregation** | `Appointment` references `Doctor` and `Patient` instances (which can exist independently). |
| 9 | **Class Variables** | `Person.total_persons`, `Patient.total_patients`, `Doctor.total_doctors`, `Hospital.hospital_name`. |
| 10 | **Class Methods** | `@classmethod` methods like `get_total_patients()`, `from_dict()`, and `get_system_version()`. |
| 11 | **Static Methods** | `@staticmethod` methods in `utils/validator.py` (e.g., `validate_age()`, `validate_phone()`, `validate_datetime_str()`). |
| 12 | **Magic Methods** | Implemented `__str__`, `__repr__`, `__len__` (e.g. `len(patient)` returns medical record count, `len(hospital)` returns patient count), and `__eq__`. |
| 13 | **Exception Handling** | Application wraps operations in `try-except` blocks in `main.py` so runtime errors never crash the program unexpectedly. |
| 14 | **Custom Exceptions** | Defined in `exceptions/custom_exceptions.py`: `HospitalException`, `PatientNotFoundError`, `DoctorNotFoundError`, `DuplicateIDError`, `SchedulingConflictError`, `InvalidInputError`. |
| 15 | **File Handling** | Data persistence using JSON (`files/hospital_data.json`). Data automatically loads on startup and saves on exit. |
| 16 | **Packages & Modules** | Organized cleanly into subdirectories/packages (`models/`, `services/`, `utils/`, `exceptions/`, `files/`). |
| 17 | **Type Hints** | Python `typing` annotations (`Optional`, `List`, `Dict`, `Any`, `Tuple`) across all methods. |
| 18 | **Documentation** | Google/Numpy style Docstrings for all classes and functions. |

---

## 🚀 How to Run

1. Open a terminal in the project directory:
   ```bash
   cd HospitalManagementSystem
   ```
2. Run the application using Python 3:
   ```bash
   python main.py
   ```
3. Follow the console menu instructions to manage patients, doctors, appointments, medical records, and view statistics.
