#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 17:54:11 2023

@author: heera1.lal
"""

from create_database import createDB
from all_data_sets import main_data_generation
from table_data_queries import table_creation_quires,data_insertion_quires


def createTable(conn,curr,query,table_name):
    try:
        curr.execute("DROP TABLE {0}".format(table_name))
        print("Dropping Existing Table: ",table_name)
    except:
        print("Creating New Table: ",table_name)
    curr.execute(query)
    

def data_insertion(curr,data_insertion_query,table_name,data_frame):
    for _,row in data_frame.iterrows():
        curr.execute(data_insertion_query.format(table_name,tuple(list(row))))
    print("data insertion completed: ",table_name)
    

def main(db_name = "college",university = "University"):

    conn, curr = createDB(db_name=db_name)
    
    table_names = ['students','faculties','courses','enrollments']
    number_of_records = [20,10,15,20]
    data_available = main_data_generation(university_name=university,number_of_records=number_of_records)
    
    for name,create_query,data_query,data in zip(table_names,table_creation_quires,data_insertion_quires,data_available):
        
        createTable(conn,curr,create_query,name)
        data_insertion(curr,data_query,name,data)
        print("Database is ready to use!")
        
        
if __name__ =="__main__":
    main(db_name="universityHyd",university="JioInst")
        
    
    
