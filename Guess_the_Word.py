import random

word = ["ali",'apple','banana']

x = random.choice(word)

y = len(x)
while y >= 0:
    user_input = input("enter text: ")
    if user_input == x :
        print("yes that's it!", x)
        break
    else:
        print("no try again")
    y -= 1
