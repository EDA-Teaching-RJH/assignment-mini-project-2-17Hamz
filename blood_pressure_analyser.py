from Patient import Patient
import pandas as pd 

patients = []

def start_system():
    patient_df = pd.read_csv("patient_data.csv")
    for index, row in patient_df.iterrows(): # 
       first_name = row["First_name"]
       last_name = row["Last_name"]
       DOB = row["DOB"]
       blood_type = row["Blood Type"]
       phone_number = row["Phone Number"]
       current_bp = int(row["Current BP"])
       blood_pressure_history = [int(row["BP1"]), int(row["BP2"]), int(row["BP3"]), int(row["BP4"]), int(row["BP5"])]
       new_patient = Patient(first_name, last_name, DOB, blood_type, phone_number, blood_pressure_history, current_bp)
       patients.append(new_patient)


   
    