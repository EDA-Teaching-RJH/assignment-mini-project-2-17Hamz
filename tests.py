import pytest
from Patient import Patient 

def test_bp_categories(capsys): #Check that BP catergories are correct 
    test_patient = Patient('Mike', 'Davies', '20/3/1992', 'O-', '01403528781')
    test_patient.updated_current_blood_pressure(161) 
    test_patient.get_blood_pressure_category()
    function_output = capsys.readouterr().out.strip()
    assert function_output == "Your blood pressure is high please seek medical attention"
    
