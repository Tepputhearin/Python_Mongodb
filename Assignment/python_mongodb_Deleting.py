import pymongo

client = pymongo.MongoClient()

mydb = client["mydb"]
mycol = mydb["people"]

myquery = {"age":18}

delete = mycol.delete_one(myquery)
# delete first doc name Thearin which age was 18
for x in mycol.find():
    print(x)