username=input("Enter username: ")
password=input("Enter password: ")

if username=='Admin' and password=='Admin':
    print("You can reset the password")
else:
    print("You cannot reset password")