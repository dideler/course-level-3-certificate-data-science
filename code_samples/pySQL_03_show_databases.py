from SQL_Settings import connectSQL     # my module for connect to SQL DB

mydb = connectSQL()
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for database in mycursor:
    print(database)
