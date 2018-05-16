import datetime
from datetime import timedelta
print(datetime.datetime.now().time())
today=datetime.date.today()
#print(today+timedelta(days=-5))
print('today')
print(today)
print('yesterday')
print(today+timedelta(days=-1))
print('tommorow')
print(today+timedelta(days=+1))
dt =datetime.datetime.today()
dt1 = datetime.datetime.min.time()
print(dt, dt1)
for i in range(5):
    today = today + timedelta(days=+1)
    print(today)
t1=datetime.datetime.now().time()
