# Write a program which repeatedly reads numbers until the user
# enters “done”.
# Once “done” is entered, print out the total, count, and
# average of the numbers.
# If the user enters anything other than a number, detect their
# mistake, print an error message and skip to the next number.


total = 0
count = 0
average = 0
while True:
    x = input("Enter a number(to exit enter done): ")
    
    if x == "done":
        print(f"Total: {total}")
        print(f"Count: {count}")
        print(f"Average: {average}")
        break
    elif not x.isdigit():
        print("Number Invalid")
        continue

    total += int(x)
    count += 1
    average = total/count
