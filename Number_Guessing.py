import random 
num = random.randrange(1,11)
user_num = 0
count = 0
while num != user_num:
    user_num = int(input("enter num: "))
    if user_num == num :
        print("yes that's it! your count ",count)
        break
    else:
        
        count +=1
        print("no try again, count: ",count)
