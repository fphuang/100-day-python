import pandas as pd


# TODO 1. Create a dictionary in this format:
data = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter: row.code for (_, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only enter alphabetic key")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()