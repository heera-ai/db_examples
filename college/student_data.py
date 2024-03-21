#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 23:26:21 2023

@author: heera1.lal
"""

import pandas as pd
from faker import Faker
import random


fake = Faker()

def generate_student_data(num_records, university_name):
    students = []
    university_initials = university_name[:3].upper()  # Get first three letters and convert to uppercase
    generated_enrollment_numbers = set()
    
    while len(students) < num_records:
        first_name = fake.first_name()
        last_name = fake.last_name()
        enrolment_number = f"{university_initials}{fake.random_int(min=10000, max=99999)}"
        
        # Check if the enrollment number is unique
        if enrolment_number not in generated_enrollment_numbers:
            generated_enrollment_numbers.add(enrolment_number)
            
            age = random.randint(18, 30)
            gender = random.choice(['Male', 'Female'])
            blood_group = random.choice(['A+', 'B+', 'AB+', 'O+', 'A-', 'B-', 'AB-', 'O-'])
            
            # Generate a 10-digit mobile number
            while True:
                contact_number = random.choice(['98', '70', '96']) + str(fake.random_int(min=10000000, max=99999999))
                if len(contact_number) == 10:
                    break
            
            email = f"{first_name.lower()}.{last_name.lower()}@{university_name.lower().replace(' ', '_')}.com"
            address = f"{fake.building_number()}, {fake.street_name()}, {fake.city()}, {fake.state_abbr()}, India. PIN: {fake.random_int(min=10000, max=99999)}"
            
            student = {
                "Enrollement_number": enrolment_number,
                "FirstName": first_name,
                "LastName": last_name,
                "Age": age,
                "Gender": gender,
                "BloodGroup": blood_group,
                "ContactNumber": contact_number,
                "Email": email,
                "Address": address,
            }
            students.append(student)
    
    student_data_df = pd.DataFrame(students)
    return student_data_df

if __name__ == "__main__":
    students_data = generate_student_data(num_records = 20,university_name="University")



