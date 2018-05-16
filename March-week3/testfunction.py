a = int(input("enter the number you want to double"))
def double(x):
    return x*2
b = double(a)
print(b)

output2 = [double(x) for x in range(10)]
print(output2)
output3 = [double(x) for x in range(10)if x%2==0]
print(output3)
output4 = [x+y for x in [10,30,50] for y in [20,40,60]]
print(output4)

output5 = [[1 if mat_colid == mat_rowid else 0 for mat_colid in range(0,3)] for mat_rowid in range(0,3)]
print(output5)