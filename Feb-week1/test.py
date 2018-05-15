import urllib.request
import json
import datetime
import pymongo
from pymongo import MongoClient
from bson import json_util
client = MongoClient('localhost:27017')
db = client.dbone
data = json.load()
client.dbone.test.insert_one(""'name', 'geeta'"")
#'age', 34, 'city', 'nyc')