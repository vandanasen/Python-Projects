"""
A website requires the users to input username and password to register.
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and
will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
"""
def validate_pswd():
    import string
    alpha = string.ascii_letters
    digits = string.digits
    punch ='$','#','@'
    print(alpha)
    print(digits)
    print(punch)
    my_list_alpha=[]
    my_list_digits = []
    my_list_punch= []
    my_list_alpha.append(alpha)
    my_list_digits.append(digits)
    my_list_punch.append(punch)
    #_print(my_list)
    pswd=input("Enter the passwords to be verified with commas:")
    #pswd1,pswd2,pswd3=pswd.split(",")
    print(pswd)
    #pswd_list = list(pswd)
    #valid_pswd =[]
    #list_all=my_list_alpha+my_list_digits+my_list_punch
    print(list_all)
    for i in range(len(pswd)):
        #print(item)
        pw=pswd[i]
        print(pw)
            if pw == str(my_list_alpha):
               elif pw == str(my_list_digits):
                   elif pw == str(my_list_punch):
                       return
                             else:
                                 print("")




            else:
                print("Invalid Password")
                break
    print(pswd)

def main():
    validate_pswd()
if __name__=="__main__":
    main()

