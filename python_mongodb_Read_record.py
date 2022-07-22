import pymongo

client = pymongo.MongoClient()

mydb = client["mydb"]
mycol = mydb["people"]
# Show collection
print(mydb.list_collection_names())

# Show single record without _id
mydoc = mycol.find({'name':'Jack'},{"_id":0, "name":1, "age":1})
print("Single Record Shown:")
for x in mydoc:
    print(x)

# Show all records without _id
print("All Record Shown:")
for y in mycol.find({},{"_id":0, "name":1, "age":1}):
    print(y)