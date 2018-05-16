from collections import Counter
def fun1():
    list1=[1,2,3,2,3]
    #list1=[1,1,1,1,1]
    #print(Counter(list1))
    print(list1.count(2))
    #print(type(Counter.value(2)))
    #print(type(list1))
    for i in range(5):
         if (Counter.value(i) == 2):
              no_of_pairs = no_of_pairs + 1
    print(no_of_pairs)

fun1()
#main():
#if __name__ = __main__:
#   main()