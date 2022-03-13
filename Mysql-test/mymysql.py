import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="flutter",
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM wp_posts")

result = mycursor.fetchall()

for x in result:
    print(x)
