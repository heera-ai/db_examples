#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 22:57:09 2023

@author: heera1.lal
"""

students_table_query = '''CREATE TABLE students(
Enrollement_number VARCHAR(20) PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Age INT,
Gender VARCHAR(10),
BloodGroup VARCHAR(10),
ContactNumber VARCHAR(15),
Email VARCHAR(100),
Address TEXT)
'''

faculties_table_query = '''CREATE TABLE faculties
(InstructorID VARCHAR(20) PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Gender VARCHAR(10),
ContactNumber VARCHAR(15),
Email VARCHAR(100),
Address TEXT,
Department VARCHAR(50),
JoinDate DATE)
'''

courses_table_query = '''CREATE TABLE courses(
CourseCode VARCHAR(20) PRIMARY KEY,
CourseName VARCHAR(100),
Department VARCHAR(50),
Credits INT,
Description TEXT,
InstructorID VARCHAR(20))
'''

enrollments_table_query = '''CREATE TABLE enrollments
(CourseEnrollmentID INT PRIMARY KEY,
StudentID VARCHAR(20), 
CourseCode VARCHAR(10), 
EnrollmentDate DATE,
Grade VARCHAR(5))
'''

students_data_query = '''INSERT INTO {0}(
Enrollement_number,
FirstName,
LastName,
Age,
Gender,
BloodGroup,
ContactNumber,
Email,
Address)
VALUES {1}'''

faculties_data_query = '''INSERT INTO {0}
(InstructorID,
FirstName,
LastName,
Gender,
ContactNumber,
Email,
Address,
Department,
JoinDate) 
VALUES {1}
'''

courses_data_query = '''INSERT INTO {0}
(CourseCode,
CourseName,
Department,
Credits,
Description,
InstructorID)
VALUES {1}
'''

enrollments_data_query = '''INSERT INTO {0}
(CourseEnrollmentID,
StudentID, 
CourseCode, 
EnrollmentDate,
Grade)
VALUES {1}
'''

table_creation_quires = [students_table_query,
                   faculties_table_query,
                   courses_table_query,
                   enrollments_table_query]

data_insertion_quires = [students_data_query,
                         faculties_data_query,
                         courses_data_query,
                         enrollments_data_query]