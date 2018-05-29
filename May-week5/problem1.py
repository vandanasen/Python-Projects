#String split and join
#make changes to an immutable string
def main():
    def stringsplit():
        str1="This is a great day"
        splitstr1=str1.split(" ")
        print(splitstr1)
        joinstr1= "-".join(splitstr1)
        print(joinstr1)
    def mutation():
        #l = list(string)
        #l[5] = 'k'
        #string = ''.join(l)
        str2="abcdeghijklmnop"
        my_list=list(str2)
        my_list[5] = "F"
        print(my_list)
    stringsplit()
    mutation()
if __name__=="__main__":
    main()


