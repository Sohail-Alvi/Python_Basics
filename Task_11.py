# 11. Write a program to reverse a string using a loop. Example: 'Python' → 'nohtyP'.

demo_str = "Python"
reversed_str = ""

for char in demo_str:
    reversed_str = char + reversed_str 

print(demo_str)
print(reversed_str)
