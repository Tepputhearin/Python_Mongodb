import pymongo

client = pymongo.MongoClient()

# create a database named mydb
mydb = client["mydb"]
print("Database connected or created")

# collection named people created
mycol = mydb["people"]
print("Collection connected or created")

# inserting one record
data = {'name':'Don', 'age':31}
mycol.insert_one(data)
print("Record inserted")

# inserting records
data_new = [{'name':'lamb', 'age':22},{'name':'Jerry', 'age':18}]
mycol.insert_many(data_new)