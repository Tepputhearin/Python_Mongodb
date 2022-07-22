import pymongo

client = pymongo.MongoClient()

mydb = client["mydb"]
mycol = mydb["people"]
# before
for y in mycol.find():
    print(y)
myquery = {"age":31}
new = {"$set":{"name":"Debbie"}}
updater = mycol.update_many(myquery, new)  # update two
print("Updated")