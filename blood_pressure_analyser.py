from Patient import Patient
import pandas as pd 

patients = []

def start_system():
    patient_df = pd.read_csv("patient_data.csv")
    for index, row in patient_df.iterrows(): # 
       first_name = row["First Name"]
       last_name = row["Last Name"]
       DOB = row["DOB"]
       blood_type = row["Blood Type"]
       phone_number = row["Phone Number"]
       current_bp = int(row["Current BP"])
       raw_bps = [row["BP1"], row["BP2"], row["BP3"], row["BP4"], row["BP5"]]
       blood_pressure_history = [int(bp) for bp in raw_bps if str(bp).strip().upper() != "N/A" and str(bp) != "nan"]
       new_patient = Patient(first_name, last_name, DOB, blood_type, phone_number, blood_pressure_history, current_bp)
       patients.append(new_patient)

def welcome():
    print("Welcome to the health admin system")
    print("Current patient information")
    for patient in patients:
       print(f"First name:{patient.first_name} Last name:{patient.last_name} DOB:{patient.DOB} blood_pressure_history:{patient.blood_pressure_history} current_bp:{patient.current_blood_pressure} ")
    run_programme = True
    while run_programme:
        print("Enter 1 to create a new patient")
        print("Enter 2 to update blood pressure history")
        print("Enter 3 to plot a chart of a patient blood pressure history")
        print("Enter 4 to get a patient current blood pressure")
        print("Enter 5 to get a patient blood pressure category")
        print("Enter 6 to save all patient information to a csv file")
        print("Enter 7 to Quit")
        user_choice = input("Enter a menu option ").strip()

        if user_choice == "1":
            first_name = input("Enter the new user's first name").strip()
            last_name = input("Enter the new user's last name: ").strip()
            phone_number = input("Enter the new user's phone number: ").strip()
            DOB = input("Enter the new user's Date of Birth (DD/MM/YYYY): ").strip()
            blood_type = input("Enter the new user's blood type (e.g., A+, O-): ").strip().upper()
            current_bp = int(input("Enter the new user's current blood pressure: ").strip())
            new_patient = Patient(first_name, last_name, DOB, blood_type, phone_number, [], current_bp)
            if new_patient.first_name:
                patients.append (new_patient)
                print("Patient created successfully")
            else:
                print("Error creating patient")
                
        elif user_choice == "2":
            for index in range(len(patients)):
                patient = patients[index]
                print(f"Index:{index} Name:{patient.first_name} {patient.last_name} DOB:{patient.DOB}")
                
            patient_to_update = int(input("Enter the index of the user you want to update: ").strip())
            updated_blood_pressure = int(input("Enter the new blood pressure: ").strip())
            patients[patient_to_update].updated_current_blood_pressure(updated_blood_pressure)
            print("Blood pressure updated successfully!")
        
        elif user_choice == "3":
            for index in range(len(patients)):
                patient = patients[index]
                print(f"Index:{index} Name:{patient.first_name} {patient.last_name}")
                
            chosen_patient = int(input("Enter the index of the patient to plot history: ").strip())
            patients[chosen_patient].plot_blood_pressure()
            print("Graph saved as BP-chart.png!")
            
        elif user_choice == "4":
            for index in range(len(patients)):
                patient = patients[index]
                print(f"Index:{index} Name:{patient.first_name} {patient.last_name}")
                
            chosen_patient = int(input("Enter the index of the patient: ").strip())
            current_bp = patients[chosen_patient].current_blood_pressure
            print(f"{patients[chosen_patient].first_name}'s current blood pressure is: {current_bp}")

        elif user_choice == "5":
            for index in range(len(patients)):
                patient = patients[index]
                print(f"Index:{index} Name:{patient.first_name} {patient.last_name}")
                
            chosen_patient = int(input("Enter the index of the patient: ").strip())
            patients[chosen_patient].get_blood_pressure_category()

        elif user_choice == "6":
            with open("patient_data.csv", "w") as file:
                file.write("First Name,Last Name,DOB,Blood Type,Phone Number,BP1,BP2,BP3,BP4,BP5,Current BP\n")
                
                for index in range(len(patients)):
                    p = patients[index]
                    history = p.blood_pressure_history.copy()
                    
                    while len(history) < 5:
                        history.append("N/A")
                    
                    csv_line = f"{p.first_name},{p.last_name},{p.DOB},{p.blood_type},{p.phone_number},{history[0]},{history[1]},{history[2]},{history[3]},{history[4]},{p.current_blood_pressure}\n"
                    
                    file.write(csv_line)
                    
                print("Success! All patient data saved to 'patient_data.csv'.")

        elif user_choice == "7":
            print("Exiting Hospital Management System. Goodbye!")
            break 
            
        else:
         print("Invalid choice. Please enter a number between 1 and 7.")




start_system()
welcome()



   
    