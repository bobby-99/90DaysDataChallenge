import random 

word_bank = [
    "affair", "admire", "amour", "belove", "cuddle",
    "desire", "devote", "embrace", "fondly", "hearts",
    "infuse", "kissed", "longer", "lovers", "lovely",
    "passion", "romance", "serene", "smiles", "smitten",
    "sparkle", "sweetly", "tender", "trusty", "warmth"
]

word = random.choice(word_bank)
attempts = 10
guessWord = ['_'] * len(word)

print(" Welcome to the Word Guessing Game")
print(f"The word has {len(word)} letters.")

while attempts > 0:
    print("\nCurrent word: " + ' '.join(guessWord))

    guess = input("Guess a letter: ").lower()

   
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single letter.")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessWord[i] = guess
        print("Great guess!")

    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    # Win condition
    if '_' not in guessWord:
        print(f"\n Congratulations! You guessed the word '{word}' in {10 - attempts} attempts.")
        break

    # Lose condition
    if attempts == 0:
        print(f"\n 💀 You lost! The word was '{word}'.")