from SQL_Settings import connectDB     # my module for connect to SQL DB

mydb = connectDB()
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for customer in myresult:
  print(customer)