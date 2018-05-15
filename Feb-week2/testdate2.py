import datetime
import calendar
today = datetime.date.today()
print (today)
this_year = today.year
print(this_year)
this_month=today.month
print(this_month)
this_week_no=today.weekday()
print(this_week_no)
thisdayofthe_year = today.strftime("%j")
print(thisdayofthe_year)
thisdayofthe_month = today.strftime("%d")
print(thisdayofthe_month)
thisdayofthe_week = today.strftime("%A")
print(thisdayofthe_week)
yr=int(input("enter the year"))
print(calendar.isleap(yr))




