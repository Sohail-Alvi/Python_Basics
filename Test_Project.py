def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


while True:
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Exit")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(add(num1, num2))
            elif choice == "2":
                print(subtract(num1, num2))
            elif choice == "3":
                print(multiply(num1, num2))
            elif choice == "4":
                print(divide(num1, num2))
        except ValueError:
            print("Please enter valid numbers only.")
    else:
        print("Invalid choice")
