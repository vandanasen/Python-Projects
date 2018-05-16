
class Record:
    """
    This is my first class
    """
    def __init__(self,rawdata,symbol=None):
        self.symbol = rawdata.get("symbol")

        self.price = rawdata.get("price")


    def __str__(self):
        return "" \
               "symbol {} price {}".format(self.symbol,self.price)

class Dataservice():
    def __init__(self):
        self.records =[]

    def add(self,**rawdata):
        rec= Record (rawdata)
        for r in self.records:
            if r.symbol == rec.symbol:
                print("symbol exists {}".format(rec.symbol))
                return
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



srvc=Dataservice()
srvc.add(symbol='IBM', price=100)
srvc.add(symbol='Google', price=200)
srvc.add(symbol='Apple',price=390)
srvc.add(symbol='Wipro',price=332)
srvc.add(symbol='AMEH',price=234)
srvc.add(symbol='Facebook',price=321)
srvc.add(symbol='Prudential',price=361)

#srvc.add(symbol='Wipro',price=332)

for rec in srvc.records:
    print(rec)

#a = srvc.find('IBM')
a = srvc.find("google")
a = srvc.find('Wipro')
a = srvc.find('Facebook')
c=srvc.findall('IBM' ,'mmm' ,'Wipro','AMEH','hhha','Facebook')




