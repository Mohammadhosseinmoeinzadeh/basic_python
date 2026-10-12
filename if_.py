user = input("enter user name: ") #admin

if user == "admin" : 
    print("wellcome")
else:
    print("error")
#-------------------------------------------
a = 150
b = 100

if a > b:
    print(a)
else: 
    print(b)
#-------------------------------------------
a = 10 

if a > 5 : 
    print("a bozorg tar az 5 ast")
#------------------------------------------
num = int(input("enter a number : "))

if num % 2 == 0 :
    print("zoj")
else :
    print("fard")
#------------------------------------------
x = int(input("enter a number x: "))
y = int(input("enter a number y: "))
z = int(input("enter a number z: "))
a = 0
if x > y:
    a = x
else : 
    a = y 
    
if a > z:
    print(a)
else:
    print(z)
