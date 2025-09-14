# 6. Ask the user to enter their age. If age < 18, print 'Minor'. If 18–60, print 'Adult'. If above 60, print 'Senior Citizen'.

age = int(input("Please enter your age: "))

if age < 18:
    print("Minor")
elif age > 60:
    print("Senior Citizen")
else:
    print("Adult")