num = input("Enter pyramid height: ")
if num.isdigit():
    num = int(num)
    i = 1
    while i <= num:
        print(" " * (num - i) + "*" * i)
        i+=1
else:
    print("Enter a valid number: ")