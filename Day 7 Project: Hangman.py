from replit import clear
import random
end_of_game = False
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
from hangman_art import logo, stages
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter in display and letter ==guess:
            print(f"You've already guessed {guess}")
        if letter == guess:    
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
