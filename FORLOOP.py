# To print a list one by one

x = ['Gautham', 65, 2.5]
for i in x:
    print(i)

# To print a string one by one

x = 'GAUTHAM'
for i in x:
    print(i)

# To print 0-10 one by one

for i in range(11):
    print(i)

for i in range(11, 21, 1):       # 11 = starting , 21 = we need 20, for that write 21, 1 = difference between each number
    print(i)

for i in range(20, 10, -1):
    print(i)

#If we don't need multiples of 5

for i in range(1, 21, 1):
    if i % 5 != 0:
        print(i)