from SQL_Settings import connectDB     # my module for connect to SQL DB

mydb = connectDB()
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for table in mycursor:
  print(table)
