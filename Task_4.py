# Create a dictionary that stores the names of 3 testers and their years of experience. Print the name of the tester with maximum experience.

demo_dic = {
            "Tester 1" :
                {
                    "name" : "Sohail",
                    "Exp" : 3
                },
            "Tester 2" :
                {
                    "name" : "Haris",
                    "Exp" : 3
                },
            "Tester 3" :
                {
                    "name" : "Ijaz",
                    "Exp" : 6
                },
            }
print(demo_dic)
print(demo_dic.keys())
print(demo_dic.values())
print(demo_dic.items())

# Find tester with maximum experience
max_exp = 0
max_name = ""

for tester, details in demo_dic.items():
    if details["Exp"] > max_exp:
        max_exp = details["Exp"]
        max_name = details["name"]

print("Tester with maximum experience:", max_name, " Years: ", max_exp)
