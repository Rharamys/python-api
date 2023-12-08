var = -51
validator = True

if var >= 0 and var < 50:
    print("it's a positive value and lesser than 50")
elif var >= 0 and var > 50:
    print("it's a positive value and greater than 50")
elif var == 50:
    print("it's 50")
else:
    print("it's a negative value")

print("it's a positive value 2") if var >=0 else print("it's a negative value 2")