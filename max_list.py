def max_num(num_list):
    max_num = num_list[0]
    for i in num_list:
        if max_num < i:
            max_num = i
    return max_num

my_list= [1,2,5,100,1000]
print(max_num(my_list))
