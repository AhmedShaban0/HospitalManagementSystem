"""
Hospital Management System - Main Entry Point & Console UI.
Implements user interface menu system and handles application lifecycle.
Demonstrates Concept #13 (Exception Handling), Concept #15 (File Handling), and user interaction.
"""

import sys
from services.hospital_service import HospitalService
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from exceptions.custom_exceptions import HospitalException


def print_header(title: str) -> None:
    """Print formatted section header."""
    print("\n" + "=" * 60)
    print(f" {title.center(58)} ")
    print("=" * 60)


def print_success(message: str) -> None:
    """Print formatted success message."""
    print(f"\n[SUCCESS] {message}")


def print_error(message: str) -> None:
    """Print formatted error message."""
    print(f"\n[ERROR] {message}")


# --- Sub-Menus ---

def patient_management_menu(service: HospitalService) -> None:
    """Handle Patient Management sub-menu operations."""
    while True:
        print_header("PATIENT MANAGEMENT")
        print("1. Add a new patient")
        print("2. Update patient information")
        print("3. Remove a patient")
        print("4. Search for a patient")
        print("5. Display all patients")
        print("6. Back to Main Menu")

        choice = input("\nSelect an option (1-6): ").strip()

        try:
            if choice == "1":
                print_header("ADD NEW PATIENT")
                patient_id = input("Enter Patient ID (e.g., P103): ").strip()
                name = input("Enter Name: ").strip()
                age = int(input("Enter Age: ").strip())
                gender = input("Enter Gender (Male/Female/Other): ").strip()
                contact = input("Enter Contact Info / Phone: ").strip()
                blood = input("Enter Blood Group (e.g., O+, A-): ").strip()

                patient = Patient(patient_id, name, age, gender, contact, blood)
                service.hospital.add_patient(patient)
                print_success(f"Patient '{name}' added successfully!")

            elif choice == "2":
                print_header("UPDATE PATIENT INFORMATION")
                patient_id = input("Enter Patient ID to update: ").strip()
                # Verify existence first
                service.hospital.get_patient(patient_id)

                print("Leave blank to keep existing value.")
                name = input("New Name: ").strip() or None
                age_str = input("New Age: ").strip()
                age = int(age_str) if age_str else None
                contact = input("New Contact Info: ").strip() or None
                blood = input("New Blood Group: ").strip() or None

                service.hospital.update_patient(
                    patient_id=patient_id,
                    name=name,
                    age=age,
                    contact_info=contact,
                    blood_group=blood
                )
                print_success(f"Patient ID '{patient_id}' updated successfully!")

            elif choice == "3":
                print_header("REMOVE PATIENT")
                patient_id = input("Enter Patient ID to remove: ").strip()
                removed = service.hospital.remove_patient(patient_id)
                print_success(f"Patient '{removed.name}' (ID: {patient_id}) removed successfully!")

            elif choice == "4":
                print_header("SEARCH PATIENTS")
                query = input("Enter Patient ID or Name to search: ").strip()
                results = service.hospital.search_patients(query)
                if results:
                    print(f"\nFound {len(results)} matching patient(s):")
                    for p in results:
                        print("-" * 40)
                        print(p.display_information())
                else:
                    print("\nNo matching patients found.")

            elif choice == "5":
                print_header("DISPLAY ALL PATIENTS")
                patients = service.hospital.get_all_patients()
                if patients:
                    print(f"Total Registered Patients: {len(patients)}\n")
                    for p in patients:
                        print("-" * 40)
                        print(p.display_information())
                else:
                    print("\nNo patients currently registered.")

            elif choice == "6":
                break
            else:
                print_error("Invalid option. Please choose between 1 and 6.")

        except ValueError:
            print_error("Invalid numeric input. Please enter a valid number.")
        except HospitalException as e:
            print_error(str(e))
        except Exception as e:
            print_error(f"An unexpected error occurred: {str(e)}")


def doctor_management_menu(service: HospitalService) -> None:
    """Handle Doctor Management sub-menu operations."""
    while True:
        print_header("DOCTOR MANAGEMENT")
        print("1. Add a new doctor")
        print("2. Update doctor information")
        print("3. Remove a doctor")
        print("4. Search for a doctor")
        print("5. Display all doctors")
        print("6. Back to Main Menu")

        choice = input("\nSelect an option (1-6): ").strip()

        try:
            if choice == "1":
                print_header("ADD NEW DOCTOR")
                doctor_id = input("Enter Doctor ID (e.g., D203): ").strip()
                name = input("Enter Doctor Name: ").strip()
                age = int(input("Enter Age: ").strip())
                gender = input("Enter Gender: ").strip()
                contact = input("Enter Contact Info: ").strip()
                spec = input("Enter Specialization (e.g., Cardiology, Surgery): ").strip()
                salary = float(input("Enter Salary: ").strip())

                doctor = Doctor(doctor_id, name, age, gender, contact, spec, salary)
                service.hospital.add_doctor(doctor)
                print_success(f"Doctor 'Dr. {name}' added successfully!")

            elif choice == "2":
                print_header("UPDATE DOCTOR INFORMATION")
                doctor_id = input("Enter Doctor ID to update: ").strip()
                service.hospital.get_doctor(doctor_id)

                print("Leave blank to keep existing value.")
                name = input("New Name: ").strip() or None
                spec = input("New Specialization: ").strip() or None
                contact = input("New Contact Info: ").strip() or None
                sal_str = input("New Salary: ").strip()
                salary = float(sal_str) if sal_str else None

                service.hospital.update_doctor(
                    doctor_id=doctor_id,
                    name=name,
                    specialization=spec,
                    contact_info=contact,
                    salary=salary
                )
                print_success(f"Doctor ID '{doctor_id}' updated successfully!")

            elif choice == "3":
                print_header("REMOVE DOCTOR")
                doctor_id = input("Enter Doctor ID to remove: ").strip()
                removed = service.hospital.remove_doctor(doctor_id)
                print_success(f"Doctor 'Dr. {removed.name}' (ID: {doctor_id}) removed successfully!")

            elif choice == "4":
                print_header("SEARCH DOCTORS")
                query = input("Enter Doctor ID, Name, or Specialization to search: ").strip()
                results = service.hospital.search_doctors(query)
                if results:
                    print(f"\nFound {len(results)} matching doctor(s):")
                    for d in results:
                        print("-" * 40)
                        print(d.display_information())
                else:
                    print("\nNo matching doctors found.")

            elif choice == "5":
                print_header("DISPLAY ALL DOCTORS")
                doctors = service.hospital.get_all_doctors()
                if doctors:
                    print(f"Total Registered Doctors: {len(doctors)}\n")
                    for d in doctors:
                        print("-" * 40)
                        print(d.display_information())
                else:
                    print("\nNo doctors currently registered.")

            elif choice == "6":
                break
            else:
                print_error("Invalid option. Please choose between 1 and 6.")

        except ValueError:
            print_error("Invalid numeric/salary input. Please enter valid numbers.")
        except HospitalException as e:
            print_error(str(e))
        except Exception as e:
            print_error(f"An unexpected error occurred: {str(e)}")


def appointment_management_menu(service: HospitalService) -> None:
    """Handle Appointment Management sub-menu operations."""
    while True:
        print_header("APPOINTMENT MANAGEMENT")
        print("1. Schedule an appointment")
        print("2. Cancel an appointment")
        print("3. Display all appointments")
        print("4. Back to Main Menu")

        choice = input("\nSelect an option (1-4): ").strip()

        try:
            if choice == "1":
                print_header("SCHEDULE AN APPOINTMENT")
                appt_id = input("Enter Appointment ID (e.g., A402): ").strip()
                patient_id = input("Enter Patient ID: ").strip()
                doctor_id = input("Enter Doctor ID: ").strip()
                datetime_str = input("Enter Date & Time (YYYY-MM-DD HH:MM): ").strip()
                notes = input("Enter Notes / Reason for visit (optional): ").strip()

                appointment = Appointment(
                    appointment_id=appt_id,
                    patient_id=patient_id,
                    doctor_id=doctor_id,
                    date_time=datetime_str,
                    status="Scheduled",
                    notes=notes
                )
                service.hospital.schedule_appointment(appointment)
                print_success(f"Appointment '{appt_id}' scheduled successfully!")

            elif choice == "2":
                print_header("CANCEL AN APPOINTMENT")
                appt_id = input("Enter Appointment ID to cancel: ").strip()
                cancelled = service.hospital.cancel_appointment(appt_id)
                print_success(f"Appointment '{cancelled.appointment_id}' has been set to Status: Cancelled.")

            elif choice == "3":
                print_header("DISPLAY ALL APPOINTMENTS")
                appointments = service.hospital.get_all_appointments()
                if appointments:
                    print(f"Total Appointments: {len(appointments)}\n")
                    for a in appointments:
                        print("-" * 40)
                        print(a.display_information())
                else:
                    print("\nNo appointments scheduled.")

            elif choice == "4":
                break
            else:
                print_error("Invalid option. Please choose between 1 and 4.")

        except HospitalException as e:
            print_error(str(e))
        except Exception as e:
            print_error(f"An unexpected error occurred: {str(e)}")


def medical_records_menu(service: HospitalService) -> None:
    """Handle Medical Records sub-menu operations."""
    while True:
        print_header("MEDICAL RECORDS MANAGEMENT")
        print("1. Create a medical record")
        print("2. Update a medical record")
        print("3. Display a patient's medical history")
        print("4. Back to Main Menu")

        choice = input("\nSelect an option (1-4): ").strip()

        try:
            if choice == "1":
                print_header("CREATE MEDICAL RECORD")
                patient_id = input("Enter Patient ID: ").strip()
                record_id = input("Enter Record ID (e.g., MR302): ").strip()
                diagnosis = input("Enter Diagnosis: ").strip()
                treatment = input("Enter Treatment: ").strip()
                notes = input("Enter Additional Notes (optional): ").strip()

                rec = service.hospital.create_medical_record(
                    patient_id=patient_id,
                    record_id=record_id,
                    diagnosis=diagnosis,
                    treatment=treatment,
                    notes=notes
                )
                print_success(f"Medical Record '{rec.record_id}' added to Patient ID '{patient_id}'!")

            elif choice == "2":
                print_header("UPDATE MEDICAL RECORD")
                patient_id = input("Enter Patient ID: ").strip()
                record_id = input("Enter Record ID: ").strip()

                print("Leave blank to keep existing value.")
                diagnosis = input("New Diagnosis: ").strip() or None
                treatment = input("New Treatment: ").strip() or None
                notes = input("New Notes: ").strip() or None

                rec = service.hospital.update_medical_record(
                    patient_id=patient_id,
                    record_id=record_id,
                    diagnosis=diagnosis,
                    treatment=treatment,
                    notes=notes
                )
                print_success(f"Medical Record '{rec.record_id}' updated successfully!")

            elif choice == "3":
                print_header("DISPLAY PATIENT MEDICAL HISTORY")
                patient_id = input("Enter Patient ID: ").strip()
                patient = service.hospital.get_patient(patient_id)
                print("\n" + patient.get_medical_history_summary())

            elif choice == "4":
                break
            else:
                print_error("Invalid option. Please choose between 1 and 4.")

        except HospitalException as e:
            print_error(str(e))
        except Exception as e:
            print_error(f"An unexpected error occurred: {str(e)}")


def display_hospital_statistics(service: HospitalService) -> None:
    """Display overall hospital statistics."""
    print_header("HOSPITAL STATISTICS")
    stats = service.hospital.get_statistics()
    print(f" Hospital Name:          {stats['hospital_name']}")
    print(f" System Version:         {service.hospital.get_system_version()}")
    print("-" * 50)
    print(f" Total Registered Patients: {stats['total_patients']}")
    print(f" Total Registered Doctors:  {stats['total_doctors']}")
    print(f" Total Staff Employees:     {stats['total_employees']}")
    print(f" Total Appointments:       {stats['total_appointments']}")
    print(f"   - Active Scheduled:      {stats['active_appointments']}")
    print(f"   - Cancelled:             {stats['cancelled_appointments']}")
    print(f" Total Medical Records:     {stats['total_medical_records']}")
    print(f" Total Doctor Payroll:      ${stats['total_doctor_payroll']:,.2f}")
    print("=" * 50)


# --- Main Application Loop ---

def main() -> None:
    """Main application loop."""
    print_header("WELCOME TO HOSPITAL MANAGEMENT SYSTEM")
    
    # Initialize service and load data automatically on startup (Concept #15)
    service = HospitalService()
    try:
        service.load_data()
        print("\n[INFO] Application data loaded successfully.")
    except Exception as e:
        print_error(f"Could not load data file: {str(e)}")

    while True:
        print_header("MAIN MENU")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Medical Records")
        print("5. Hospital Statistics")
        print("6. Save Data")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            patient_management_menu(service)
        elif choice == "2":
            doctor_management_menu(service)
        elif choice == "3":
            appointment_management_menu(service)
        elif choice == "4":
            medical_records_menu(service)
        elif choice == "5":
            display_hospital_statistics(service)
        elif choice == "6":
            try:
                service.save_data()
                print_success("Data saved successfully to files/hospital_data.json!")
            except Exception as e:
                print_error(str(e))
        elif choice == "7":
            # Save data before exiting (Concept #15)
            try:
                service.save_data()
                print("\n[INFO] Data saved automatically before exit.")
            except Exception as e:
                print_error(f"Error saving data on exit: {str(e)}")
            
            print("\nThank you for using Hospital Management System. Goodbye!")
            sys.exit(0)
        else:
            print_error("Invalid selection. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
