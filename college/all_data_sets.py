#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 15:56:43 2023

@author: heera1.lal
"""

from student_data import generate_student_data
from faculty_data import generate_faculty_data
from course_data import generate_courses_data
from enrollment_data import generate_enrollments_data

def main_data_generation(university_name="University",number_of_records =[2,2,2,2]):
    students_data = generate_student_data(num_records = number_of_records[0],
                                     university_name = university_name)
    
    faculties_data = generate_faculty_data(num_records = number_of_records[1],
                                           university_name = university_name)
    
    courses_data = generate_courses_data(num_records =number_of_records[2] ,
                                         faculty_data = faculties_data)
    
    enrollments_data = generate_enrollments_data(num_records = number_of_records[3],
                                                 student_data = students_data,
                                                 courses_data = courses_data)

    return [students_data,
            faculties_data,
            courses_data,
            enrollments_data]

if __name__ =="__main__":
    data= main_data_generation()

