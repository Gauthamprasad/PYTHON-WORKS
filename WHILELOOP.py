# WHILE LOOP
#INCREMENTING
i = 1
while i <= 5:
    print("Hello")
    i = i + 1

i = 1
while i <= 5:
    print(i)
    i = i + 1

#DECREMENTING
i = 5
while i >= 1:
    print("Hello")
    i = i - 1

i = 5
while i >= 1:
    print(i)
    i = i - 1

#Nested While
i = 1
while i <= 5:
    print("Gautham ", end="")
    j = 1
    while j <= 4:
        print("Prasad ", end="")
        j = j + 1
    i = i + 1
    print()
