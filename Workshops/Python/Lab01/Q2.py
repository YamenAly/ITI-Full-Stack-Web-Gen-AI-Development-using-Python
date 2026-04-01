print('Enter 5 numbers')
x = []
for i in range(5):
    x.append(input(f"Enter number {i+1}: "))
x.sort()
print("Ascending: ", x)
x.sort(reverse=True)
print("Descending: ", x)