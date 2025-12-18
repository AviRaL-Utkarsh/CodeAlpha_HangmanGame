import random

words = ["apple", "banana", "grapes", "orange", "mango"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    guess = input("Guess a letter: ").lower()

    if guess in used_letters:
        print("Already guessed!")
        continue

    used_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in guessed:
    print("Congratulations! You guessed the word:", word)
else:
    print("You lost! The word was:", word)
