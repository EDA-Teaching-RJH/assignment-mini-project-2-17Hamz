# Developer Journal: Mini Project 2 - Hospital Management System

## Project Overview
* For this assignment, I decided to build a Hospital Management System. This project allowed me to showcase my skills by focusing on the core elements taught in the second half of the module. The system handles patient data, validates medical inputs, tracks blood pressure history, and generates visual medical reports.


# How my code links to workshops and lectures during the second half of term 

**Object-Oriented Programming (OOP) - Lecture/Workshop 9**
Workshop 9 taught us about Object-Oriented Programming. I used this to make a `Patient` class. Instead of having a messy list of variables, the class uses an `__init__` constructor to organize the patient's name, birthday, blood type, and blood pressure all in one place. I also added methods inside the class, like `get_blood_pressure_category()`, which keeps the main menu code really clean and easy to read.

**Regular Expressions (REGEX) - Lecture/Workshop 8**
Workshop 8 taught me that basic string checking isn't always enough. To make sure my medical data was correct, I used the `re` module. I used `re.fullmatch(r"(A|B|AB|O)[+-]", blood_type)` to check that blood types were entered perfectly (like A+ or O-), otherwise the patient wouldn't be created. I also used `datetime.strptime` to make sure the birthdays were entered in the exact right format.

**File Input/Output (I/O) - Lecture/Workshop 8**
To save data so it isn't lost when the program closes, I used File I/O. When the system starts, it loads patient info from `patient_data.csv`. I also added a way to save updates using `with open("patient_data.csv", "w") as file:`, which overwrites the old file with the newest information. I even added a fix to put "N/A" in empty spots if a patient didn't have 5 blood pressure readings yet, which stopped the CSV file from breaking.

**Unit Testing - Lecture/Workshop 8**
To make sure my code actually worked correctly, I used `pytest` instead of just printing things to the screen to check them. In my `tests.py` file, I used `capsys` and `assert` to test my `get_blood_pressure_category()` method. This let me prove that inputting a high number would actually trigger the right warning message (like "Your blood pressure is high please seek medical attention").

**Libraries & Extra Features - Lecture/Workshop 7**
Workshop 7 showed us how to use external libraries like `matplotlib` to make charts. I used this to go above and beyond the basic requirements. My `plot_blood_pressure()` method automatically makes a line graph of a patient's history and saves it as an image called `BP-chart.png`. I also researched how to use the `pandas` library to read my CSV file, which was an extra step beyond the normal `csv` tool we learned in class.

## How I Built It & Solved Problems
Making the interactive menu was challenging but really rewarding. One big problem I ran into was loading the blood pressure history from the CSV file. If a patient had fewer than 5 readings, the blank spots were read as "N/A" or "nan". When the code tried to turn those into numbers, the whole program crashed. 

To fix it, I wrote a list comprehension: `[int(bp) for bp in raw_bps if str(bp).strip().upper() != "N/A" and str(bp) != "nan"]`. This safely ignored the text and only grabbed the real numbers, which stopped the crashes and made the system run perfectly when starting up.