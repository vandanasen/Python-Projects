
import json
import requests
#import pymongo
from pymongo import MongoClient
#from bson import json_util
client = MongoClient('localhost:27017')
db = client.dbone
url = 'https://currencydatafeed.com/api/data.php?token=of4h4kfktm9q9iwpu1gq&currency=EUR/USD+USD/JPY+EUR/NOK+AUD/USD+USD/SGD+USD/MXN+XAU/USD+GBP/CAD'
datareq = requests.get(url).content
datareq = datareq.decode('utf-8')
#datareq = datareq
jasondata = json.loads(datareq)
post =client.dbone.post.insert_one(jasondata)
print(jasondata)

