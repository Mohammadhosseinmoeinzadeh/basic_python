def taghsim(a,b):
    return a / b
    
def taghsim_baghi(a,b):
    return a % b

print("Simple Calculator")
print("1- Addition")
print("2- Absolute Difference")
print("3- Power")
print("4- Division (Quotient & Remainder)")
print("5- Round a Number")
print("6- Max & Min")
print("7- Convert to Integer (int)")
print("8- Convert to Float (float)")
choice = int(input("select an option (1-8)"))
if choice == 1:
    a = int(input("enter num a: "))
    b = int(input("enter num b: "))
    print(sum([a,b]))
elif choice == 2 :
    a = int(input("enter num a: "))
    print(abs(a))
elif choice == 3 :
    a = int(input("enter num : "))
    b = int(input("enter power: "))
    print(pow(a,b))
elif choice == 4 :
    a = int(input("enter num a: "))
    b = int(input("enter num b: "))
    print ("kharj ghesmat: ",taghsim(a,b))
    print ("baghimande taghsim", taghsim_baghi(a,b))
elif choice == 5:
    a = float(input("enter num a: "))
    b = int(input("enter num b: "))
    print(round(a,b))
elif choice == 6 :
    a = int(input("enter num a: "))
    b = int(input("enter num b: "))
    print ("max",max(a,b))
    print ("min",min(a,b))
elif choice == 7:
    a = input("enter a number: ")
    print(int(a))
elif choice == 8:
    a = input("enter a number: ")
    print(float(a))
else : 
    print("your choice out of range")
