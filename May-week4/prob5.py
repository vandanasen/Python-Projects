"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""
class myclass:
    def __init__(self,str1):
        self.str1 = str1
    def __str__(self):
        return "" \
               "string".format(self.str1)
    def getstring(self):
        self.str1=input('Enter a String:')

    def printstring(self):
        print(self.str1)
ob=myclass('')
f=ob.getstring()
g=ob.printstring()


