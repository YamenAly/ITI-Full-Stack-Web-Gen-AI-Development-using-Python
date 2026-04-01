# Write a function that takes a string and prints the
# longest alphabetical ordered substring occurred For example, if
# the string is 'abdulrahman' then the output is: Longest substring in alphabetical order is: abdu

def sub(str):
    current =str[0]
    longest = current    
    for i in range(1, len(str)):
        if str[i] >= str[i-1]:
            current += str[i]
        else:
            current = str[i]
        if len(current) > len(longest):
            longest = current

    print(f"Longest substring is: {longest}")

str = "abdelrahman"

sub(str)