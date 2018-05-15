# This is a program which adds different symbols and their values
from datetime import datetime
from datetime import date
# This is a class of Records of symbols
class Record:
    """
    This is a class of records of symbols
    """
    def __init__(self,rawdata,symbol=None,date=''):
        self.symbol = rawdata.get("symbol")

        self.price = rawdata.get("price")

        self.date = rawdata.get("date")
        self.date2 = rawdata.get("date")

    def __str__(self):
        return "" \
               "symbol {} price {} date {}".format(self.symbol,self.price,self.date)

class Dataservice():
    def __init__(self):
        self.records =[]

    def add(self,**rawdata):
        datelst=[]
        rec= Record (rawdata)
        #print(rec.date)
        for r in self.records:
            if r.symbol == rec.symbol:
                print("symbol exists {}".format(rec.symbol))
                return
        #print(rec.date)
        rec.date = datetime.strptime(rec.date,'%m-%d-%Y')

        rec.date2 = rec.date
        rec.date = rec.date.strftime('%m-%d-%Y')
        #print(rec.date2)
        self.records.append(rec)
    def find(self,sym):
        for rec in srvc.records:
            if rec.symbol == sym:
                print("The price for the", rec.symbol,"is", rec.price)
                return rec
        print("symbol not found")
    def findall(self,*findlst):
        newfindlst=[]
        for rec in srvc.records:
            if  rec.symbol in findlst:
                newfindlst.append(rec.symbol)
        print("The list of symbols present", newfindlst)
        return rec
    def finddate(self,*gvdt):
        newlst=[]
        if len(gvdt) == 1:
            for rec in srvc.records:
                if rec.date in gvdt:
                    print("The price for the", rec.symbol, "is", rec.price,"for the given date")
                    return rec
            print("no symbol was not found for the given date")
            #return rec
        if len(gvdt) == 2:
             for rec in srvc.records:
                  stdt = gvdt[0]
                  enddt = gvdt[1]
                  if rec.date2 >= stdt and rec.date2 <= enddt:
                        newlst.append(rec.symbol)
                        print("The price for the", rec.symbol, "is", rec.price,"for the given date range")

             return rec
             print("no symbol in this date range")
    def search(self,**kwargs1):
             newlst = []
             sym = kwargs1.get('symbol')
             gvdt = kwargs1.get('date')
             stdt = kwargs1.get('st_date')
             enddt = kwargs1.get('end_date')
             if sym is not None:
                for rec in srvc.records:
                    if rec.symbol == sym:
                            print("The price for the", rec.symbol, "is", rec.price)
                            return rec
                print("symbol not found")
             #gvdt = kwargs1.get('date')
             if sym == None :
                for rec in srvc.records:
                    if gvdt is not None and rec.date in gvdt:
                        print("The price for the", rec.symbol, "is", rec.price, "for the given date")
                        return rec
                #print("no symbol was not found for the given date")
                    elif gvdt == None and (rec.date2 >= stdt and rec.date2 <= enddt):
                        newlst.append(rec.symbol)
                        print("The price for the", rec.symbol, "is", rec.price, "for the given date range")
                return rec
             print("No symbol found for this date or date range")

srvc=Dataservice()
srvc.add(symbol='IBM', price=100,date ='4-15-2017')
srvc.add(symbol='Google', price=200,date ='12-20-2017')
srvc.add(symbol='Apple',price=390,date ='3-17-2017')
srvc.add(symbol='Wipro',price=332,date ='7-18-2016')
srvc.add(symbol='AMEH',price=234,date ='10-10-2017')
srvc.add(symbol='Facebook',price=321,date ='2-19-2018')
srvc.add(symbol='Prudential',price=361,date ='8-19-2017')


for rec in srvc.records:
    print(rec)

#a = srvc.find('IBM')
print("Results of test data for finding a symbol ")
a = srvc.find("Google")
a = srvc.find('Wipro')
a = srvc.find('Facebook')
print("Results of test data for finding list of symbols")
c=srvc.findall('IBM' ,'mmm' ,'Wipro','AMEH','hhha','Facebook')
print("Results of test data for finding list of symbols in the given date range")
d=srvc.finddate(datetime(2017,2,1),datetime(2017,10,10))
print("Results of test data for finding list of symbols for a given date")
e=srvc.finddate('04-15-2017')
f=srvc.finddate('25-06-2015')
print("XXXXXXXXXXXXXXX")
#symbol
dict1 = {'symbol': 'kdjdj'}
dict2 = {'symbol': 'Wipro'}
srvc.search(**dict1)
srvc.search(**dict2)
#date
dict3 = {'date': '04-15-2017'}
srvc.search(**dict3)
dict4 = {'date': '02-19-2018'}
srvc.search(**dict4)
dict5 = {'date': '07-14-2015'}
srvc.search(**dict5)
#date range
dict6 = {'st_date':datetime(2017,2,1),'end_date':datetime(2017,10,10)}
srvc.search(**dict6)




