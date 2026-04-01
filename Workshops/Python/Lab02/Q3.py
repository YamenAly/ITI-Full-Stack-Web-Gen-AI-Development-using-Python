def reverseStr(str):
    string = list(str)
    string.reverse()
    result = "".join(string)
    return result

s = input("Enter string: ")
print(reverseStr(s))

