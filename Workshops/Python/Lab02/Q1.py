def filled(length, start):
    x =[]
    for i in range(length):
        x.append(i+start)
    return x

z = int(input("Enter start number: "))
y = int(input("Enter length number: "))

print (filled(y,z))    