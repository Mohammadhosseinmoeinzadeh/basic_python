def takhfif(tedad,gheymat):
    if tedad > 5:
        return tedad * gheymat * 0.9
    else:
        return tedad * gheymat

a = int(input("enter tedad: "))
b = int(input("enter mablagh: "))

print(takhfif(a,b))
