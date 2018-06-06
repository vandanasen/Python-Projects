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
    my_list=[]
    my_list.append(list(alpha))
    my_list.append(list(digits))
    my_list.append(list(punch))
    print(my_list)
    pswd=input("Enter the passwords to be verified with commas:")
    pswd1,pswd2,pswd3=pswd.split(",")
    print(pswd1)
    pswd_list = list(pswd)
    for item in pswd_list:
        print(item)
        for item in my_list:
            print(item)
            if item in my_list:
                print("Valid Password")
                pass
            else:
                print("Invalid Password")
    print(pswd)

def main():
    validate_pswd()
if __name__=="__main__":
    main()

