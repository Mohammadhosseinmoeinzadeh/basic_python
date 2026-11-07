def sum_list(my_list):
    total = 0
    for i in my_list:
        total = total + i
    return total

a = []

count = int(input("enter counter: "))

for i in range (count):
    num = int(input("enter number: "))
    a.append(num)
print(sum_list(a))
