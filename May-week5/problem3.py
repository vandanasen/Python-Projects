"""
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program
"""
def main():
    def fun():
        a=int(input("Enter a number:"))
        a2=int(str(a)+str(a))
        a3=int(str(a)+str(a)+str(a))
        a4=int(str(a)+str(a) +str(a)+str(a))
        sum = a+a2+a3+a4
        print(sum)
    fun()
"""
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program
"""
def main():
     def fun2():
        gv_list=(1,2,3,4,5,6,7,8,9)
        new_list=()
        for i in range(len(gv_list)):
             if (i%2==0):
                 pass
             else:
                 new_list.append(gv_list(i))
                 print(new_list())
     fun2()


if __name__=='__main__':
    main()