import pandas as pd

data = pd.read_csv("Day-53_NATO_Alphabet\\nato_alphabet.csv")

alphabet = {row.letter: row.code for index, row in data.iterrows()}

user_input = input("Enter the word: ").upper()
output_list = [alphabet[letter] for letter in user_input]
print(output_list)
