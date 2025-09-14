# 15. Write a function that accepts a list of numbers and returns the largest number.

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


s_list = [35, 18, 251, 97, 130, 182]
result = find_largest(s_list)
print(result)

