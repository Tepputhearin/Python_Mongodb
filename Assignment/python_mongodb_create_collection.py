import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# create a database named mydb
mydb = client["mydb"]
print("Database connected or created")
# collection named people created
mycol = mydb["people"]
print("Collection connected or created")