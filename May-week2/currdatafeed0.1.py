# This is program to acccept data from an api and load it into a mongodb
import urllib.request
import json
import datetime
import pymongo
from pymongo import MongoClient, response
from bson import json_util
client = MongoClient('localhost:27017')
db = client.dbone
url = 'https://currencydatafeed.com/api/data.php?token=of4h4kfktm9q9iwpu1gq&currency=EUR/USD+USD/JPY+EUR/NOK+AUD/USD+USD/SGD+USD/MXN+XAU/USD+GBP/CAD'
json_obj = urllib.request.urlopen(url)
currdatafeed_data = json.load(json_obj)
json_status = currdatafeed_data['status']
print('API Status:' + str(json_status))
json_currency = currdatafeed_data['currency']
#data = json.loads(json_currency)
for i in range(0, 8):
    json_value = json_currency[i].values()
    #posts = client.dbone.post.insert_many(data)
    print(json_value)
    #posts = client.dbone.posts
    #data = json_util.loads(json_value)
    #posts = client.dbone.post.insert_many(data)
    # print("\n")
print(currdatafeed_data)
