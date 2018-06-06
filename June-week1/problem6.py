my_list = [1, 3, 6, 10]
a = (x**2 for x in my_list)
print(next(a), next(a))
def Foo(n):
    def multiplier(x):
        return x * n
    return multiplier

a = Foo(5)
b = Foo(5)

print(a(b(2)))

def i_return(x):
    print(x)
    return x

def i_dont(x):
    print (x)

i_return(5)        # prints 5
i_dont(5)          # prints 5
print(i_return(5) +2)
print(i_dont(5) +2)
