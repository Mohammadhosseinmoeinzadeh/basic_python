def moghayese(my_list):
    max_number = 0
    for i in my_list:
        if max_number < i:
            max_number = i
    return max_number


a = [1,2,3,4,5,10]
print(moghayese(a))
