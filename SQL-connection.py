import mysql.connector as ms

mydb = ms.connect(host='',user='', passwd='', database = )

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS customers")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO customers(name,address) VALUE (%s,%s)"
val1 = ("John", "Highway 21")
val2 = ("tina", "Nothernway 007")
mycursor.execute(sql,val1)
mycursor.execute(sql,val2)
mydb.commit()

sql = "UPDATE customers SET address = 'canyon 21' WHERE address = 'Highway 21'"
mycursor.execute(sql)
mydb.commit()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)


