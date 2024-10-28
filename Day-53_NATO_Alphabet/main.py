import pandas as pd

data = pd.read_csv("Day-53_NATO_Alphabet\\nato_alphabet.csv")

alphabet = {row.letter: row.code for index, row in data.iterrows()}

def generate_phonetics():
    user_input = input("Enter the word: ").upper()
    try:
        output_list = [alphabet[letter] for letter in user_input]
    except KeyError:
        print("You entered an invalid input! Only alphabetic characters are allowed.")
        generate_phonetics()
    else:
        print(output_list)


generate_phonetics()