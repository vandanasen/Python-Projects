import calendar
from datetime import datetime,timedelta
def f1(year):
    no_of_sat = 0
    #no_of_sun = 0
    for i in range(7):
     d = calendar.weekday(year,1,1)
     if d == 6:
          for i in range(365):
             no_of_sat = no_of_sat + 1
             d = d + timedelta(days=+7)
     print(no_of_sat)
f1(2010)


