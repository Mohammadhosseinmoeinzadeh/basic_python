def char_check(inputer):
    low_count=0
    up_count=0
    dig_count=0
    for i in inputer:
        if i.islower():
            low_count +=1
        elif i.isupper():
            up_count +=1
        elif i.isdigit():
            dig_count +=1
    print("up counter:",up_count)
    print("low counter:",low_count)
    print("digit counter:",dig_count)


a = input("entet a text:")

char_check(a)
