import json
import datetime
import requests
#import pymongo
from pymongo import MongoClient
#from bson import json_util
client = MongoClient('localhost:27017')
db = client.dbone
url ='https://currencydatafeed.com/api/data.php?token=y5khafix4yfhp7ebydcl&currency=EUR/USD+USD/JPY+EUR/NOK+AUD/USD+USD/SGD+USD/MXN+XAU/USD+GBP/CAD'
datareq1 = requests.get(url).content
datareq2 = json.loads(datareq1.decode('utf-8'))
datareqcurrency = datareq2.get('currency')
#print('first:',datareqcurrency)
for x in datareqcurrency:
    x["value"] = float(x.get('value',0))
    #x["date"] = x.get('date')[0:10]
    x["date"] = x.get('date')
table2 = client.dbone.table2.insert_many(datareqcurrency)

#def query_mongo():
#     cursor = client.dbone.table2.find({'currency':{'$in':['EUR/USD','GBP/CAD']}})
#     for doc in cursor:
#         print(doc)
#query_mongo()
#query_mongo('EUR/USD')
def query_mongo(symbol):
    #api_data_mongodb()
    cursor = client.dbone.table2.find({'currency': {'$in': [symbol]}})
    for doc in cursor:
        print(doc)

query_mongo('EUR/USD')

