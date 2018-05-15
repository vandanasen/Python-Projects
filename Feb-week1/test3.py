
import json
import pymongo
from pymongo import MongoClient, response
client = MongoClient('localhost:27017')
db = client.dbone
array1=['grass', 2, 'haily', 4, 'lion', 9]
#post = client.dbone.post.insert_one({"name":"harry","age":26,"city":"LA"})
post = client.dbone.post.insert_one({'name' : 'harry'})
post = client.dbone.post.insert_one({'name' : 'mary','age':34,'city':'nyc'})
post=client.dbone.post.insert_many(array1)
