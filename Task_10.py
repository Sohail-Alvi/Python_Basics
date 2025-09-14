# 10. Given a list of numbers, print only the even numbers. Example: [10, 15, 22, 33, 40] → 10, 22, 40

demo_list = [5, 10, 15, 22, 33, 40, 42, 45, 46, 50]

for e in demo_list:
    if e % 2 == 0:
        print(e)
