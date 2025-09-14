# 3. Write a program to count how many vowels are present in a given string. Example: 'automation' → 5 vowels.

s_str = "I am learning python"
s_str = s_str.lower()   # convert to lower case
count = 0
for char in s_str:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print(char)
        count = count + 1
print("Total: ", count)


# 2nd approach
s_str = "I am learning python"
s_str = s_str.lower()

vowels = "aeiou"
count = 0

for char in s_str:
    if char in vowels:
        print(char)
        count += 1

print("Total vowels:", count)



