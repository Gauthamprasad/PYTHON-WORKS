# IF, IF ELSE, IF ELSE IF, NESTED IF


# IF
x = 6
r = x % 2
if r == 0:
    print("Even number")

# IF ELSE
x = 7
r = x % 2
if r == 0:
    print("Even number")
else:
    print("Odd number")

# Nested IF
x = 8
r = x % 2
if r == 0:
    print("Even number")
    if x > 5:
        print("Greater than 5")
    else:
        print("Less than 5")
else:
    print("Odd number")

# IF ELSE IF
x = 3
if (x == 1):
    print("One")
elif (x == 2):
    print("Two")
elif (x == 3):
    print("Three")
elif (x == 4):
    print("Four")
else:
    print("Wrong input")
