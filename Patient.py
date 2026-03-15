import re 
import matplotlib.pyplot as plt

class Patient:
    def __init__(self,first_name, last_name, DOB, blood_type, phone_number):
        first_name, last_name, DOB, blood_type, phone_number = first_name.strip(), last_name.strip(), DOB.strip().upper(), blood_type.strip(), phone_number.strip()
        valid_date = re.fullmatch(r"[1-31]/[1-12]/[1-2026]", DOB) #Validating the date of birth.
        valid_blood_type = re.fullmatch(r"A+|A-|B+|B-|O+|O-|AB+|AB-", blood_type) # Validating the blood type 
        if not(valid_date):
            print("Erorr:invalid Date Of Birth ")
        elif not(valid_blood_type): 
            print("Error:invalid blood type ")
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.DOB = DOB
            self.blood_type = blood_type
            self.phone_number = phone_number
            self.blood_pressure_history = []
            self.current_blood_pressure = None

    def updated_current_blood_pressure (self, new_blood_pressure):
        if new_blood_pressure < 0: 
            print("Erorr:invalid Blood Pressure ")
        else:
            self.current_blood_pressure = new_blood_pressure
            self.blood_pressure_history.append(new_blood_pressure)
            if len(self.blood_pressure_history) > 5:
                self.blood_pressure_history.pop(0) #Replaces oldest value with new one 

    def plot_blood_pressure(self):
        x_values = range(1, len(self.blood_pressure_history)+1)
        y_values = self.blood_pressure_history
        plt.plot(x_values, y_values)

            