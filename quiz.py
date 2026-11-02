menu = {"1":"riyazi","2":"python","0":"exit"}
quiz_riyazi = {"2*2":"4","2/2":"1","2*3":"6"}
quiz_python = {"shomaresh horof?":"len","data taype adad sahih? ":"int"}

score = 0
for i in menu:
    print(i,menu[i])
x = input("enter quiz number: ")
if x == "1":
    print("soalat riyazi")
    for qu in quiz_riyazi:
        ans = input(qu+" ")
        if ans == quiz_riyazi[qu]:
            print("done!")
            score +=1
        else:
            print("wrong!")
elif x == "2":
       print("soalat python")
       for qu1 in quiz_python:
            ans1 = input(qu1+" ")
            if ans1 == quiz_python[qu1]:
                print("done!")
                score +=1
            else:
                print("wrong!")
elif x == "0":
    print("your exit game!")
print(score)
