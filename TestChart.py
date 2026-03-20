from Patient import Patient

patient_1 = Patient('Ike', 'Hamzat', '13/4/2006', 'A-', '079')
patient_2 = Patient('Ike', 'Hamzat', '13/04/2006', 'AB-', '079') 

patient_1.updated_current_blood_pressure(60)
patient_1.updated_current_blood_pressure(80)
patient_1.updated_current_blood_pressure(100)
patient_1.updated_current_blood_pressure(60)

patient_1.get_blood_pressure_category()