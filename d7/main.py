import random
from hangman_words import word_list
from hangman_art import stages, logo


def main():
    lives = 6
    end_of_game = False
    chosen_word = random.choice(word_list)
    display = ["_" for _ in range(0, len(chosen_word))]

    while not end_of_game:  # or set a while loop using boolean variable
        guess = input("Guess a letter: ").lower()
        if guess in display:
            print("You already guess this word")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

        if guess not in chosen_word:
            print(f"Your guess {guess} is not in a word. You lose a life")
            lives -= 1
            if lives == 0:
                print("You lose")
                end_of_game = True

        if "_" not in display:
            print("You have won")
            print(f'This is your word {"".join(display)}')
            break
        print(stages[lives])
        print(" ".join(display))


if __name__ == "__main__":
    main()
