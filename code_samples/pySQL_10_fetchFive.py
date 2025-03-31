from SQL_Settings import connectDB     # my module for connect to SQL DB

mydb = connectDB()
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()
for actor in myresult:
    print(actor)