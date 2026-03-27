import re 
import matplotlib.pyplot as plt
from datetime import datetime

class Patient:
    def __init__(self,first_name, last_name, DOB, blood_type, phone_number, blood_pressure_history, current_blood_pressure):
        first_name, last_name, DOB, blood_type = first_name.strip(), last_name.strip(), DOB.strip().upper(), blood_type.strip()
        valid_date = False 
        try:
            datetime.strptime(DOB, "%d/%m/%Y") #Validating the date of birth.
            valid_date = True 
        except ValueError:
            pass 
        valid_blood_type = re.fullmatch(r"(A|B|AB|O)[+-]", blood_type) # Validating the blood type 
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
            self.blood_pressure_history = blood_pressure_history
            self.current_blood_pressure = current_blood_pressure

    def updated_current_blood_pressure(self, new_blood_pressure):
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
        plt.savefig("BP-chart.png")

    def get_blood_pressure_category(self):
        if self.current_blood_pressure>140:
            print("Your blood pressure is high please seek medical attention")
        elif self.current_blood_pressure>=120:
            print("Your blood pressure is slighly high")
        elif self.current_blood_pressure>=90:
            print("Your blood pressure is fine")
        else:
            print("Your blood pressure is too low seek medical attention")
            