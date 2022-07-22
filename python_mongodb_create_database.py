import pymongo

client = pymongo.MongoClient()

# create a database named mydb
mydb = client["mydb"]
print("Database connected or created")