#INPUT
pswd = input("Write your password: ")
#PROCESS
flag = True #For exiting the loop
while flag:
    if len(pswd) < 8:
        print("Write a longer password (8 characters or more)")
        pswd = input("New password: ")
    elif not (any(char.isupper() for char in pswd)):
        print("Your password must contain an upper case letter")
        pswd = input("New password: ")
    elif not (any(char.islower() for char in pswd)):
        print("Your password must contain a lower case letter")
        pswd = input("New password: ")
    elif not (any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in pswd)):
        print("Your password must contain a special character")
        pswd = input("New password: ")
    elif not (any(char.isdigit() for char in pswd)):
        print("Your password must contain a digit")
        pswd = input("New password: ")
    elif sum(int(char) for char in pswd if char.isdigit()) != 25:
        print("Your password digits need to add up to 25")
        pswd = input("New password: ")
    elif len(pswd) not in [2,3,5,7,11,13,17,19,23,29,31,37]:
        print("Your password length needs to be a prime number")
        pswd = input("New password: ")
    elif "june" not in pswd.lower():
        print("Your password needs to have the current month")
        pswd = input("New password: ")
    else:
        flag = False
#OUTPUT
print("Your password is secure")