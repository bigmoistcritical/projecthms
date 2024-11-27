# HMS System

# Initialize empty lists to store patients, doctors, and appointments
patients = [
    {"name": "John Doe", "age": 30},
    {"name": "Jane Smith", "age": 25},
    {"name": "Bob Johnson", "age": 40},
    {"name": "Alice Brown", "age": 35},
]

doctors = [
    {"name": "Dr. Smith", "specialty": "Cardiology"},
    {"name": "Dr. Johnson", "specialty": "Neurology"},
    {"name": "Dr. Brown", "specialty": "Oncology"},
    {"name": "Dr. Davis", "specialty": "Pediatrics"},
]

appointments = [
    {"patient": "John Doe", "doctor": "Dr. Smith", "date": "2023-03-01", "time": "10:00 AM"},
    {"patient": "Jane Smith", "doctor": "Dr. Johnson", "date": "2023-03-02", "time": "2:00 PM"},
    {"patient": "Bob Johnson", "doctor": "Dr. Brown", "date": "2023-03-03", "time": "10:30 AM"},
    {"patient": "Alice Brown", "doctor": "Dr. Davis", "date": "2023-03-04", "time": "3:00 PM"},
]

def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    patients.append({"name": name, "age": age})
    print("Patient added successfully!")

def delete_patient():
    name = input("Enter patient name to delete: ")
    for patient in patients:
        if patient["name"] == name:
            patients.remove(patient)
            print("Patient deleted successfully!")
            return
    print("Patient not found!")

def add_doctor():
    name = input("Enter doctor name: ")
    specialty = input("Enter doctor specialty: ")
    doctors.append({"name": name, "specialty": specialty})
    print("Doctor added successfully!")

def add_appointment():
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    date = input("Enter appointment date: ")
    time = input("Enter appointment time: ")
    for patient in patients:
        if patient["name"] == patient_name:
            for doctor in doctors:
                if doctor["name"] == doctor_name:
                    appointments.append({"patient": patient_name, "doctor": doctor_name, "date": date, "time": time})
                    print("Appointment added successfully!")
                    return
            print("Doctor not found!")
            return
    print("Patient not found!")

def view_appointments():
    for appointment in appointments:
        print(f"Patient: {appointment['patient']}, Doctor: {appointment['doctor']}, Date: {appointment['date']}, Time: {appointment['time']}")

def main_menu():
    while True:
        print("HMS System")
        print("1. Add Patient")
        print("2. Delete Patient")
        print("3. Add Doctor")
        print("4. Add Appointment")
        print("5. View Appointments")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_patient()
        elif choice == 2:
            delete_patient()
        elif choice == 3:
            add_doctor()
        elif choice == 4:
            add_appointment()
        elif choice == 5:
            view_appointments()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
