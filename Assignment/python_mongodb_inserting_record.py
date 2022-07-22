import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# create a database named mydb
mydb = client["mydb"]
print("Database connected or created")

# collection named people created
mycol = mydb["people"]
print("Collection connected or created")

# inserting one record
# data = {'name':'Dan', 'age':35}
# mycol.insert_one(data)
# print("Record inserted")

# inserting records
data_new = [{'name':'Larry', 'age':28},{'name':'Jacob', 'age':48}]
mycol.insert_many(data_new)