#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:22:18 2023

@author: heera1.lal
"""
import pandas as pd
from faker import Faker
import random

fake = Faker()

def generate_faculty_data(num_records, university_name):
    faculty = []
    department_names = ['Mechanical', 'Civil', 'Computer Science', 'Physics', 'Maths', 'Chemistry']
    generated_instructor_ids = set()
    
    for _ in range(num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        department = random.choice(department_names)
        
        # Generate a unique instructor ID using the first three letters of department name
        instructor_id_initials = department[:3].upper()
        while True:
            instructor_id = f"{instructor_id_initials}{fake.unique.random_int(min=100, max=999)}"  # 3-digit instructor ID
            if instructor_id not in generated_instructor_ids:
                generated_instructor_ids.add(instructor_id)
                break
            
        gender = random.choice(['Male', 'Female'])
        
        # Generate a 10-digit mobile number
        while True:
            contact_number = random.choice(['98', '70', '96']) + str(fake.random_int(min=10000000, max=99999999))
            if len(contact_number) == 10:
                break
            
        email = f"{first_name.lower()}.{last_name.lower()}@{university_name.lower().replace(' ', '_')}.com"
        address = f"{fake.building_number()}, {fake.street_name()}, {fake.city()}, {fake.state_abbr()}, India. PIN: {fake.random_int(min=10000, max=99999)}"
        join_date = fake.date_between(start_date='-5y', end_date='today')
        
        faculty_member = {
            "InstructorID": instructor_id,
            "FirstName": first_name,
            "LastName": last_name,
            "Gender": gender,
            "ContactNumber": contact_number,
            "Email": email,
            "Address": address,
            "Department": department,
            "JoinDate": join_date,
        }
        faculty.append(faculty_member)
    faculty_data_df = pd.DataFrame(faculty)
    faculty_data_df["JoinDate"] = faculty_data_df["JoinDate"].astype('str')
    return faculty_data_df

if __name__ == "__main__":
    faculties_data = generate_faculty_data(num_records = 2, university_name ="University")

