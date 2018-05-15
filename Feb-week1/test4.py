import json
import requests
#import pymongo
from pymongo import MongoClient
#from bson import json_util
client = MongoClient('localhost:27017')
db = client.dbone
url ='https://currencydatafeed.com/api/data.php?token=y5khafix4yfhp7ebydcl&currency=EUR/USD+USD/JPY+EUR/NOK+AUD/USD+USD/SGD+USD/MXN+XAU/USD+GBP/CAD'
#url = 'https://currencydatafeed.com/api/data.php?token=of4h4kfktm9q9iwpu1gq&currency=EUR/USD+USD/JPY+EUR/NOK+AUD/USD+USD/SGD+USD/MXN+XAU/USD+GBP/CAD'
datareq1 = requests.get(url)
datareq2 = datareq1.content
datareq3 = datareq1.json()['currency']
print(datareq3)
jasondata = json.loads(datareq2.decode('utf-8'))
#datareq["date"] = datetime.datetime(datareq["date"])
table1 = client.dbone.table1.insert_many(datareq3)

