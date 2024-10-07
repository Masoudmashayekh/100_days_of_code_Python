import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
game_is_on = True
while game_is_on:
    word = input("Enter a word: ").upper()
    if word == "EXIT":
        game_is_on = False
    else:
        output_list = [new_dict[letter] for letter in word]
        print(output_list)
