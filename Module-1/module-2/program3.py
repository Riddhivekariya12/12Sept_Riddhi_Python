r=int(input("enter any range for fibonacci series:"))
a=0
b=1
if r < 0:
    print("error...enter valid range")

elif r == 0:
    print(0)

elif r == 1:
    print(1)
else:
    for i in range(2,r):
        c = a + b
        a = b
        b = c 
        print(b)       