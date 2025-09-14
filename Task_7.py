# Write a program that accepts a username and password. If the username is 'admin' and the password is '1234', print 'Login Successful'. Otherwise, print 'Access Denied'

username = input("Please enter username: ")
password = input("Please enter password: ")

if username == "admin" and password == "1234":
    print("login successful")
else:
    print("Access denied")