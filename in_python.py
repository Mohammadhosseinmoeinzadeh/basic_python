number = {10,15,11,12,100,157,45}
if 10 in number :
    print ("number 10 is available")
else :
    print("number is not available")
#---------------------------------------------
name = {"ali","abdolah","akbar","mohseni"}
en = input("enter name: ")
if en in name :
    print("ok")
else:
    print("name is not found! but insert name now to the set!")
    name.add(en)
    print(name)
