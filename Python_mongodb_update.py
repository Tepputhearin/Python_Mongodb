import pymongo

client = pymongo.MongoClient()

mydb = client["mydb"]
mycol = mydb["people"]
# before
for y in mycol.find():
    print(y)
myquery = {"name":"Debbie"}
new = {"$set":{"name": "NO"}}
updater = mycol.update_one(myquery, new)  # update one
print("Updated")
# after
for x in mycol.find():
    print(x)
