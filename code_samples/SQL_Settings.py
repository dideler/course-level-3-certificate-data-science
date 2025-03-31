''' 
Importable Module to define connecting to MySQL Server and its Database.

Define your database connection parameters here and then import this file into 
your own code

'''

import mysql.connector

def connectSQL():
    ''' Connect to SQL Server'''
    return mysql.connector.connect(
    host='localhost', 
    user='root',
    password='mysql')

def connectDB():
    ''' Connect to SQL Database'''
    return mysql.connector.connect(
        host='localhost', 
        user='root',
        password='mysql',
        database='myDB'     # connect to this database
    )

def connectDBSakila():
    ''' Connect to SQL Database'''
    return mysql.connector.connect(
        host='localhost', 
        user='root',
        password='mysql',
        database='sakila'     # connect to this database
    )



