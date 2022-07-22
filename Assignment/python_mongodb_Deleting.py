import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mydb"]
mycol = mydb["people"]

myquery = {"age":35}

delete = mycol.delete_one(myquery)
# delete first doc name Thearin which age was 18
for x in mycol.find():
    print(x)