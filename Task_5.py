# 5. Write a program to check whether a number entered by the user is even or odd.

number = int(input("Please enter any number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
