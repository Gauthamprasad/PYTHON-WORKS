#Fetching values from string
name = 'Gautham'                    #here G corresponds to 0,a = 1, u = 2, etc..
print(name[0])
print(name[4])
print(name[-1])                     #here -1 means m, -2 means a, -3 means h,etc..
print(name[-4])
print(name[1:4])                    #here it's a range but it will not include 4=h, starting from 1=a.
print(name[0:2])                    #it will not include 2=u, starting from 0=G.

print(name[1:])                     #here 1=G is not printed.
print(name[:4])                     #here upto 4=H,therefore values before 4 and printed.
print(name[3:10])                   #here 3=t,and we have no 10 value, therefore upto 6=m is printed.