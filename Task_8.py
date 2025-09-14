# 8. Print the multiplication table of a number entered by the user (from 1 to 10).

number = int(input("Please enter a number: "))

count = 1
while count <= 10:
    print(f"{number} x {count} = {number * count}")
    count += 1
