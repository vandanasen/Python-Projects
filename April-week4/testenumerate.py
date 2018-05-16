grocery=['bread','milk','washing powder','butter']
bettergrocery = enumerate(grocery)
print(type(bettergrocery))
print(list(bettergrocery))
bettergrocery2 = enumerate(grocery,20)
print(list(bettergrocery2))
a1=range(10)
print("**********")
print(a1)
for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 500):
  print(count, item)
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)