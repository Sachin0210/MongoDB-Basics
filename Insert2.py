from pymongo import MongoClient
import pprint
client = MongoClient()
db            = client["new_db"]
collection    = db["my_collection"]


# Insert Operation 
sd = {"Name": "Sachin"}
collection.insert_one(sd)

# Other Method to insert into MOngoDB DataBase
collection.insert_many([{"Name": "A", "Age":  20}, {"Name": "B", "Age":  21}, {"Name": "C","Age":23}])
