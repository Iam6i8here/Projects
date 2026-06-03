import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

lives = 6

chosen_word = random.choice(word_list)

display = "_" * len(chosen_word)

print("Word to guess: " + display)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print(f"\n**************************** {lives}/6 LIVES LEFT ****************************")

    guess = input("Guess a letter: ").lower()

    # Check for duplicate guesses
    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'.")
        continue

    guessed_letters.append(guess)

    # Wrong guess
    if guess not in chosen_word:
        lives -= 1

        print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        if lives == 0:
            print(stages[lives])
            print("*********************** YOU LOSE **********************")
            print(f"The correct word was: {chosen_word}")
            break

    # Correct guess
    if guess in chosen_word:
        correct_letters.append(guess)

    # Rebuild display
    display = ""

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    print(stages[lives])

    # Win condition
    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")
