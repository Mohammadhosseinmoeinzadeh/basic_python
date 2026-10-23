#pizza = 200
#sandwich = 100
#salad = 50
#coca = 20

food = input("choice food : pizza / sandwich")
des = input("choice deser : salad / coca / nothing")
food_price = 0
des_price = 0

if food == "pizza":
    food_price = 200
elif food == "sandwich":
    food_price = 100
else :
    print("food not found")


if des == "salad":
    des_price = 50 
elif des == "coca":
    des_price = 20
elif des == "nothing":
    des_price = 0
else :
    print("food not found")
    
print("You must pay the amount of ",des_price + food_price,"$")
