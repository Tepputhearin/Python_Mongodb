import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mydb"]
mycol = mydb["people"]
# before
for y in mycol.find():
    print(y)
myquery = {"name":"Jack"}
new = {"$set":{"age": 30}}
updater = mycol.update_one(myquery, new)  # update one
print("Updated")
# after
for x in mycol.find():
    print(x)
