from pymongo import MongoClient

client = MongoClient()
db     = client["first_db"]
col    = db["me"]


# Insert Operation
person_dict = {}
person_dict ["Name"]="Sachin"
person_dict ["Age"] =19

col.insert(person_dict)
