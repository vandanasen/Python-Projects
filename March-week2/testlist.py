a = [1, 3, 5]
b = [2, 4, 6]
c = a + b
print(c)
d = sorted(c)
d.reverse()
print(d)
c.insert(3, 42)
print(c)
d.append(10)
#c.append(7)
#c.append(8)
#c.append(9)
c+=[7,8,9]
print(c)
print(c[0:3])
print(d[5])
print(len(d))