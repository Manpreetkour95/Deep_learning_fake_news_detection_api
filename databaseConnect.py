# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 22:03:04 2022

@author: Manpreet Kour
"""

import pyodbc 

server_name='----enter sql server name ---------'
database='--------enter database name----------'
table_name='-----enter table name-----------'

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      f"Server=f{server_name};"
                      f"Database={database};"
                      "Trusted_Connection=yes;")

class DataBaseConnection:
    
    def push_to_db(self,input, output):
        cursor = cnxn.cursor()
        cursor.execute(f"insert into [{table_name}] values({input},{output})" )
        cursor.commit()
