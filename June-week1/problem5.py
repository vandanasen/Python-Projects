numbers = [2, 3, 4]
print(numbers)
print(3 >= 3)
def printHello():
    print("Hello")
a = printHello()
def outerFunction():
    global a
    a = 20
    def innerFunction():
        global a
        a = 30
        print('a =', a)
a = 10
outerFunction()
print('a =', a)
class Foo:
    def printLine(self, line='Python'):
        print(line)


o1 = Foo()
o1.printLine('Java')


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


p1 = Point(3, 4)
p2 = Point(1, 2)
result = p1 - p2
print(result.x, result.y)
def greetPerson(*name):
  print('Hello', name)
names = "{1}, {2} and {0}".format('John', 'Bill', 'Sean')
print(names)


my_list = [1, 3, 6, 10]
a = (x**2 for x in my_list)
print(next(a), next(a))


greetPerson('Frodo', 'Sauron')
print((1, 2) + (3, 4))
a='lam'
b='han'
c=a+b
print(c)