#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:30:51 2023

@author: heera1.lal
"""
import pandas as pd
from faker import Faker
import random

from faculty_data import generate_faculty_data


fake = Faker()

def generate_courses_data(num_records, faculty_data):
    courses = []
    
    for _ in range(num_records):
        department_row = random.choice(faculty_data.index)
        department = faculty_data.loc[department_row, "Department"]
        instructor_id = faculty_data.loc[department_row, "InstructorID"]
        credits = random.randint(1, 3)
        course_name = fake.catch_phrase()
        description = fake.paragraph()
        
        # Generate a unique course code using the first three letters of department name
        course_code_initials = department[:2].upper()
        while True:
            course_code = f"{course_code_initials}{fake.unique.random_int(min=100, max=999)}"  # 3-digit course code
            if course_code not in [course["CourseCode"] for course in courses]:
                break
        
        course = {
            "CourseCode": course_code,
            "CourseName": course_name,
            "Department": department,
            "Credits": credits,
            "Description": description,
            "InstructorID": instructor_id,
        }
        courses.append(course)
    

    
    courses_data_df = pd.DataFrame(courses)
    return courses_data_df

if __name__ == "__main__":
    faculties_data = generate_faculty_data(num_records = 2, university_name = "University")
    
    courses_data = generate_courses_data(num_records = 2,faculty_data=faculties_data)

