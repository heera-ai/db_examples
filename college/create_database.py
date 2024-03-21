#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 19:25:28 2023

@author: heera1.lal
"""
import mysql.connector
from secure_data import username,password_for_user

def createDB(db_name):
    conn = mysql.connector.connect(user=username, password=password_for_user,
                                  host='127.0.0.1',
                                  database='sys',
                                  auth_plugin='mysql_native_password')
    conn.autocommit=True
    curr  = conn.cursor()
    curr.execute("DROP DATABASE IF EXISTS {0}".format(db_name))
    curr.execute("CREATE DATABASE {0}".format(db_name))
    
    curr.close()
    conn.close()
    
    conn = mysql.connector.connect(user=username, password=password_for_user,
                                  host='127.0.0.1',
                                  database=db_name,
                                  auth_plugin='mysql_native_password')
    
    conn.autocommit = True
    curr = conn.cursor()
    
    return conn, curr

if __name__ =="__main__":
    conn,curr = createDB("accounts")
    
    
    
    