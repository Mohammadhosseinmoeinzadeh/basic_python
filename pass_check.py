pas = 1234
count = 0
while count < 3:
    inp = int(input("enter password: "))
    count = count + 1
    if inp == pas:
        print("wellcome")
        break
else :
    print("error")
