class Record:
    """
    This is my first class
    """
    def __init__(self,symb,value):
        self.symb = symb
        self.value = value
reclist=[]
for i in range(5):
    new_rec= Record('gbr',89)
    reclist.append(new_rec)
for rock in reclist:
    print(rock.symb)
    print(rock.value)


rec1 = Record('usd',13)
rec2 = Record('eur',35)
print(rec1.symb)
print(rec1.value)
print(rec2.symb)
print(rec2.value)












