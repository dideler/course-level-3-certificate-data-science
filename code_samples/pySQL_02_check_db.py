from SQL_Settings import connectSQL 

mydb = connectSQL()
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
