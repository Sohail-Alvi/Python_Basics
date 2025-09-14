# 13. Write a function to calculate the factorial of a number using a loop.


def calculate_factorial(no):
    factorial = 1
    for i in range(1, no + 1):
        factorial = factorial * i
    return factorial

result = calculate_factorial(3)
print(result)

