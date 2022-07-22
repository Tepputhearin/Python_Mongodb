import pymongo

client = pymongo.MongoClient()

mydb = client["mydb"]
mycol = mydb["people"]

myquery = {"age":31}

delete = mycol.delete_many(myquery)
# delete many doc name NO and Debbie which age was 31
for x in mycol.find():
    print(x)