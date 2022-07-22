import mysql.connector
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="1234",
    database="kit"
)
# read mysql table
cursor = connection.cursor()
read_mysql = cursor.execute("SELECT * FROM dse10")
students = cursor.fetchall()

# create a database named Task in mongodb
mydb = client["Task"]
print("Database connected or created")

# collection named people created
mycol = mydb["Students"]
print("Collection connected or created")
# convert tuple of mysql to {} in mongodb
data = []
for i in students:
    item = {'Sid': i[0], 'Sname': i[1], 'SAge': i[2]}
    data.append(item)
# insert the converted mysql to mongodb records
mycol.insert_many(data)
print("Table from mysql inserted to Mongodb")
for y in mycol.find():
    print(y)