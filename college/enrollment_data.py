#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:52:07 2023

@author: heera1.lal
"""

from faker import Faker
import random
import pandas as pd

from course_data import generate_courses_data
from student_data import generate_student_data
from faculty_data import generate_faculty_data

fake = Faker()

def generate_enrollments_data(num_records, student_data, courses_data):
    enrollments = []
    valid_grades = ['A', 'B', 'C', 'D', 'E']
    generated_enrollment_ids = set()
    
    while len(enrollments) < num_records:
        enrollment_id = fake.unique.random_int(min=10000, max=99999)  # 5-digit enrollment ID
        
        if enrollment_id not in generated_enrollment_ids:
            generated_enrollment_ids.add(enrollment_id)
            
            student_row = random.choice(student_data.index)
            student_id = student_data.loc[student_row, "Enrollement_number"]
            course_row = random.choice(courses_data.index)
            course_code = courses_data.loc[course_row, "CourseCode"]
            enrollment_date = fake.date_between(start_date='-1y', end_date='today')
            grade = random.choice(valid_grades)
            
            enrollment = {
                "CourseEnrollmentID": enrollment_id,
                "StudentID": student_id,
                "CourseCode": course_code,
                "EnrollmentDate": enrollment_date,
                "Grade": grade,
            }
            enrollments.append(enrollment)
    
    enrollments_data_df = pd.DataFrame(enrollments)
    enrollments_data_df["EnrollmentDate"] = enrollments_data_df["EnrollmentDate"].astype(str)
    return enrollments_data_df


if __name__ == "__main__":
    faculties_data = generate_faculty_data(num_records = 2, university_name = "University")
    courses_data = generate_courses_data(2, faculty_data = faculties_data)
    students_data = generate_student_data(num_records = 2, university_name="University")
    enrollments_data = generate_enrollments_data(num_records =2 , student_data = students_data, courses_data = courses_data)
