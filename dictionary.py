student = {
    "name": "Ali",
    "age": 18,
    "grade": 20
}
print(student["name"])
print(student["age"])

#change_value

student["age"] = 19
print(student)

student["city"] = "Tehran"
print(student)

#delete valvue
del student["grade"]
print(student)
