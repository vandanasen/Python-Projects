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
        #self.datarecord=Record(datarecord)
        rec= Record (rawdata)
        self.records.append(rec)



srvc=Dataservice()
srvc.add(symbol='IBM', price=100)
srvc.add(symbol='GOOG', price=200)

for rec in srvc.records:
    print(rec)


