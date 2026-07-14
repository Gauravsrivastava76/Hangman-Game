import random

# List of predefined words
words = ["python", "computer", "college", "student", "keyboard"]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses
wrong_guesses = 0
max_wrong = 6

print("=" * 40)
print("        WELCOME TO HANGMAN")
print("=" * 40)
print("Guess the hidden word.")
print("You have only 6 wrong guesses.\n")

# Game Loop
while wrong_guesses < max_wrong:

    display_word = ""

    # Show guessed letters and underscores
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord :", display_word)
    print("Wrong Guesses Left :", max_wrong - wrong_guesses)
    print("Guessed Letters :", guessed_letters)

    # Check if player has won
    if "_" not in display_word:
        print("\n🎉 Congratulations!")
        print("You guessed the word:", secret_word)
        break

    # Take input
    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")

# Game Over
if wrong_guesses == max_wrong:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")