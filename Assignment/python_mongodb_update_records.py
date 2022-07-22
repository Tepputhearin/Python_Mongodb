import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = client["mydb"]
mycol = mydb["people"]
# before
for y in mycol.find():
    print(y)
myquery = {'age':30}
new = {"$set":{"name":"Me"}}
updater = mycol.update_many(myquery, new)  # update two
print("Updated")