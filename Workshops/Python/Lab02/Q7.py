# Word guessing game (hangman)
# A list of words will be hardcoded in your program, out of
# which the interpreter will
# choose 1 random word.
# The user first must input their names
# Ask the user to guess any alphabet. If the random word
# contains that alphabet, it will be shown as the output(with correct placement)
# Else the program will ask you to guess another alphabet.
# Give 7 turns maximum to guess the complete word.

myl = ["apple", "kiwi", "orange", "banana"]

def hangman():
    mys = set(myl)
    word = mys.pop()
    name = input("Enter your name: ")
    guessed = ["_"] * len(word)
    turns = 7

    while turns > 0 and "_" in guessed:
        guess = input("Guess any alphabet characters: ")

        if guess in word:
            for i in range(len(word)):
                 if word[i] == guess:
                     guessed[i] = guess
        else:
            turns -= 1
            print("Wrong guess, try again!")
            print(f"{turns} Tries Remaining")
        
        print("Word", " ".join(guessed))

    if "_" not in guessed:
        print(f"YOU WIN! {name}")
    else:
        print(f"YOU LOSE! {name}")
        print(f"The word was: {word}")


hangman()