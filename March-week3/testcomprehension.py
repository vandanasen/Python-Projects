my_string = [num**2 for num in range(10)]
print(my_string)
list1=[4,7,5]

list2 = [i*3 for i in list1]
print(list2)

list_of_words=['this','is','a','list','of','word']
output = [i[0] for i in list_of_words]
print (output)
list3 = ["K","i","P","i","J","B"]
list4=[x.lower() for x in list3 ]
print(list4)
list5=["D","j","b","H","m","X"]
list6=[x.upper() for x in list5]
print(list6)
liststr = "HELLO8976world"
liststrout = [i for i in liststr if i.isdigit()]
print(liststrout)
listdigout = [i for i in liststr if i.isalpha()]
print(listdigout)