import random, sys
from typing import List

WORD_LIST = [
    "lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
    "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
]

GUESS_WORD = []
SECRET_WORD = random.choice(WORD_LIST)  # lets randomize single word from the list
LENGTH_WORD = len(SECRET_WORD)
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def print_word_to_guess(letters: List) -> None:
    print("Word to guess: {0}".format(" ".join(letters)))


def print_guesses_taken(current: int, total: int) -> None:
    print("You are on guess {0}/{1}.".format(current, total))


def prepare_secret_word() -> None:
    for character in SECRET_WORD:  # printing blanks for each letter in secret word
        GUESS_WORD.append("-")
    print("The word You need to guess has", LENGTH_WORD, "characters!")
    print_word_to_guess(GUESS_WORD)


def game() -> None:
    guess_taken = 1
    MAX_GUESS = 10
    print_guesses_taken(guess_taken, MAX_GUESS)

    while guess_taken < MAX_GUESS:
        guess = input("Pick a letter\n: ")
        if not guess in ALPHABET:  # checking input
            print("Enter a letter from a-z ALPHABET")
        elif guess in letter_storage:  # checking if letter has been already used
            print("You have already guessed that letter!")
        else:
            letter_storage.append(guess)
            if guess in SECRET_WORD:
                print("You guessed correctly!")
                for i in range(0, LENGTH_WORD):
                    if SECRET_WORD[i] == guess:
                        GUESS_WORD[i] = guess
                print_word_to_guess(GUESS_WORD)
                print_guesses_taken(guess_taken, MAX_GUESS)
                if '-' not in GUESS_WORD:
                    print("You won!")
                    print("Game Over!")
                    break
            else:
                print("That letter is not in the word. Try Again!")
                guess_taken += 1
                print_guesses_taken(guess_taken, MAX_GUESS)
                if guess_taken == 10:
                    print(" Aw, you lost :(! The secret word was:",SECRET_WORD)


prepare_secret_word()
game()
