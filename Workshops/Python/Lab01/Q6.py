x = int(input("Enter Number: "))
i = 1
z = []
while i <=x:
    j = 1
    y = []
    while j <=i:
        y.append(i*j)
        j+=1
    z.append(y)
    i+=1
print(z)


