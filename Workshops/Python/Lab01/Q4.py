word = input("Enter a word: ")
newword = ""
for i in word:
    if i not in "aeiou":
        newword += i
print(newword)