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
cursor = connection.cursor(dictionary=True)
read_mysql = cursor.execute("SELECT * FROM dse10")
students = cursor.fetchall()

# create a database named Task in mongodb
mydb = client["New"]
print("Database connected or created")

# collection named people created
mycol = mydb["students"]
print("Collection connected or created")

if len(students) > 0:
    x = mycol.insert_many(students)
#     print(len(x.inserted_ids))
for y in mycol.find():
    print(y)