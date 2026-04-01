num = input("Enter pyramid height: ")
if num.isdigit():
    num = int(num)
    i = 1
    for i in range(num):
        print(" " * (num - (i+1)) + "*" * (i+1))
        i+=1
else:
    print("Enter a valid number: ")