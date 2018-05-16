import math
import this
'''
#input multiple values from user in one line
x,y=[int(x) for x in input().split()]
print(x)
print(y)
'''
#trunc()
print (math.floor(3.5)) # floor
print (math.trunc(3.5)) # work as floor
print (math.ceil(3.5))  # ceil
print (math.floor(-3.5)) # floor
print (math.trunc(-3.5)) # work as ceil
print (math.ceil(-3.5))  # floor
#printing multiple variable in python
print(1)
print((1))
print(1,2)
print((1,2))
# Multiple Return Values in Python!
def func():
    return 1, 2, 3, 4, 5

one, two, three, four, five = func()

print(one, two, three, four, five)

# Know the index faster
vowels=['a','e','i','o','u']
for i, letter in enumerate(vowels):
    print (i, letter)
# Chaining Comparison Operators
i = 5;
ans = 1 < i < 10
print(ans)

ans = 10 > i <= 9
print(ans)

ans = 5 == i
print(ans)

# Positive Infinity
p_infinity = float('Inf')

if 99999999999999 > p_infinity:
    print("The number is greater than Infinity!")
else:
    print("Infinity is greatest")

# Negetive Infinity
n_infinity = float('-Inf')
if -99999999999999 < n_infinity:
    print("The number is lesser than Negative Infinity!")
else:
    print("Negative Infinity is least")

# Simple List Append
a = []
for x in range(0, 10):
    a.append(x)
print(a)

# List Comprehension
print([x for x in a])

# Slice Operator
a = [1, 2, 3, 4, 5]

print(a[0:2])  # Choose elements [0-2), upper-bound noninclusive

print(a[0:-1])  # Choose all but the last

print(a[::-1])  # Reverse the list

print(a[::2])  # Skip by 2

print(a[::-2])  # Skip by -2 from the back


